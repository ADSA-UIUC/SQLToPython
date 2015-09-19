# Using a web API (Work In Progress)

## Introduction
An API (Application Programmable Interface) is a way that a developer can write
client code that will interact with another piece of software. In the case of
the web, most API's are ways to interact with the data that the software has 
available. In Facebook's API, you can interact with your profile (the data) in a
couple of ways. You can send friend requests, like posts, and post statuses, but
when you do these things, you do them in the language that the code understands.
The Facebook website doesn't inherently understand what clicking a button is 
supposed to do. Facebook has programmed their website to talk to their servers 
in a represenation that their server can understand. Like ASCII is a way of
sharing textual information via binary, a web API is a way of sending encoded
information to a server. To start, lets look at the language they use.


## HTTP
When you make most web requests on the internet, an HTTP request is sent to a
remote location, determined by IP address. The HTTP request has a predefined,
agreed upon, and standard format. It usually involves a message header and a 
message body. The request involves a couple components, which I will go into 
more detail here. 

First, it contains the URL that you are trying to reach. URL's are one of the 
most important parts of  any web API. They give the remote server information 
on what you are trying to  access, and how it should respond.

Next, you have an HTTP verb. There are many HTTP verbs, but the only ones that
are standard in web API's are GET and POST. A GET request does just that, it
gets information in many different forms. When you view a website in a web
browser like Chrome, Firefox or Safari, the browser makes a GET request for all
the URL that you gave it. Then, it proceeds to GET all the information it needs
to display the page. POST is the other side of the coin. It is used to send 
information to the remote server. In the web browser, forms where you input data
usually make a POST request to the server with the information that you put into
the forms within. These both have the same usage in web API's.


As an example, take a look at the Twitter API documentation.
![Twitter API](/images/Twitter API_annotated.png)

As you can see, the API contains both a VERB and what is called an *endpoint*. 
Endpoints are another form of a URL that omits the base URL. For this API, the
base URL is ``` https://api.twitter.com/1.1/ ```, so a URL would be formed by
appending the *endpoint* to the base URL. The end result would look like 
```https://api.twitter.com/1.1/statuses/retweet/:id.json```. In the Twitter API
specifically, the ```:id``` is just a placeholder for the information that you
are giving to the server. In this case, the server wants an id of the tweet to
retweet.


## More about URL's
URL's have a couple parts to them. This diagram shows the structure, taken from
[tutsplus.com](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)
![URL Structure](/images/http1-url-structure.png)
