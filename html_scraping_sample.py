import json
import urllib2
import MySQLdb


# To use bs4, run this command in the vagrant box
# sudo pip install beautifulsoup4
from bs4 import BeautifulSoup




# A simple function to grab a webpage
def fetch():
    link = "https://www.reddit.com/"
    text = urllib2.urlopen(link).read()
    return text


# Function used to scrape links from reddit
# Returns a list of tuples containing the link
# and its title
def extract_links(text):
    soup = BeautifulSoup(text, "html.parser")

    # Find all of the links with a class of "title"
    links = soup.find_all('a', class_="title")

    output = []
    for link in links:
        # Print each link
        print(link.get_text() + " " + link['href'])
        data = (link['href'], link.get_text())
        output.append(data)

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
    text = fetch()
    links = (extract_links(text))
    store(links)

