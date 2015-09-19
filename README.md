# SeQueL to Python

This repository constitutes the first beginner project. It includes sample
code as well as a vagrant box development environment for you to use.





## High Level Instructions
1. Fork this repository on github to track the changes you make
2. Set up vagrant ([for Mac](https://github.com/ADSA-UIUC/Resources/blob/master/dev-environment/vagrant/mac-setup.md), [for Windows](https://github.com/ADSA-UIUC/Resources/blob/master/dev-environment/vagrant/windows-setup.md))
3. Gather data from any source on the web (Be careful of rate limits!)
4. Store that data into the MySQL database installed on the vagrant box
5. Push the code back to github!



## Detailed Instructions

The two samples in this repository do the same thing in two different ways.
Both print a list of the titles and links on the front page of reddit. The 
first, ```html_scraping_sample.py``` uses the BeautifulSoup4 library to read
the html that reddit gives to web browsers. If you take a look at the 
code, the important part is the usage of BeautifulSoup to extract all the
links in the page that have a class of "title". This is the html scraping
method. The other file, ```json_scraping_sample.py``` is how to do it
using the json that reddit is nice enough to provide for you. By adding
```.json``` to any reddit link, you can get it as a json document. It can
be used to get all the links a bit easier, in json format.


We would like you to write code to work with any data source on the web, be it
html, json or another format. Get it into python first, then work on getting into
MySQL.


In order to use MySQL, the first thing you need to do is create a table that 
will store your data. For a tutorial on creating a table, see [here]
(http://www.tutorialspoint.com/mysql/mysql-create-tables.htm). Make sure that 
the table you design has columns for every piece of information that you want. 
Once you have that done, you can use the MySQLdb library to store the data you 
gathered in the first part. The code samples include how to do this.


