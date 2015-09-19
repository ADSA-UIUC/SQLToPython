import urllib2
import json
import MySQLdb


# Function to fetch json of reddit front page
def fetch():
    link = "https://www.reddit.com/.json"
    # Get the text version
    text = urllib2.urlopen(link).read()

    # Turn it into a dictionary
    data = json.loads(text)
    return data

# Returns a list of tuples of titles and links
def extract_links(data):
    data = data["data"]['children']
    output = []
    for post in data:
        link = post['data']['url']
        title = post['data']['title']
        output.append((title, link))
    return output


# Puts the data into the MySQL database defined in tables.sql
def store(data):
    host = "localhost"
    user = "root"
    passwd = "adsauiuc"
    db = "adsa"
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    # Creates a cursor that can execute SQL commands
    cursor = db.cursor()

    table = "reddit"
    columns = "link, title"
    for link in data:
        sql = """ INSERT INTO reddit ( link, title ) VALUES ( %s, %s ) """
        cursor.execute(sql, (link[0].encode("latin-1", "replace"), link[1].encode("latin-1", "replace")))

    # Commit the changes only after all have succeeded without errors
    db.commit()

    # Always close the connection
    db.close()



if __name__ == "__main__":
    data = fetch()
    links = extract_links(data)
    store(links)
