import requests
import json
import MySQLdb
import datetime
import sys

# Script to call the UIUC EWS lab utilization api
# DOES NOT ACCOUNT FOR TIMEZONE!!!

# MYSQL datetime format
time_format = '%Y-%m-%d %H:%M:%S'






def fetch(link):
    """
    Parameters: URL to page to read
    Returns: JSON from page  
    """
    # Use requests library to request the file
    r = requests.get(link)
    # Make sure status code is within acceptable range. See: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
    if(r.status_code >= 200 and r.status_code < 300):
        # Throw it as error if not in 2xx
        r.raise_for_status()
    # Convert from JSON to python dictionary
    data = json.loads(r.text)
    return data


def store(json, config):
    """
    Parameters: JSON DB Config object of for 
        {
            "host": ...,
            "user": ...,
            "passwd": ...,
            "db": ...,
        }
    """
    # Snag the data from the "data" key
    data = json["data"]

    # Connect to the mysql database from config dictionary
    # Note: ** is the unwinding operator. Turns a dictionary into named parameters
    # Documentation for MySQLdb is here: http://mysql-python.sourceforge.net/MySQLdb.html
    db = MySQLdb.connect(**config)
    cursor = db.cursor()
    for lab in data:
        table = lab["strlabname"].replace(" ", "_")
        columns = ", ".join(["timestamp", "inusecount" , "machinecount"])
        values = ", ".join(["'" + str(datetime.datetime.now().strftime(time_format)) + "'", str(lab["inusecount"]), str(lab["machinecount"])])
        # SQL Insert statement: see http://www.w3schools.com/sql/sql_insert.asp
        # """ Means keep the formatting of the string
        sql = """
        INSERT INTO %s
        ( %s ) 
        VALUES ( %s )
        """ % (table, columns, values)
        # "Executes" the sql string but doesn't actually commit the result
        cursor.execute(sql)
    # Commits the change to the database
    db.commit()
    db.close()
    return True
    

# Code the is equivalent to "int main() {}"
if __name__=="__main__":
    """
    Called from cron job, get and store data
    """
    link = "https://my.engr.illinois.edu/labtrack/util_data_json.asp"
    if len(sys.argv) != 2:
        print """
        Usage: python %s <path to json config file>
        """ % sys.argv[0]
        sys.exit(1)
    with open(sys.argv[1], "r") as conf:
        config = json.load(conf)

    try:
        # Use the defined functions
        data = fetch(link)
        # Store the value
        success = store(data, config)
        if not success:
            print "%s" % datetime.datetime.now().strftime(time_format)
    except Exception as e:
        print e
