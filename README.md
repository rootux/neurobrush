About the project
Weekend long Hackathon @google, Tel Aviv.
we decided to create a machine that output the users feeling
into the web.

we "accidently" created a by-product that exposes the emotiv
data to the web in a json format.

by doing so we allow javascript developer write on top of what
we did and create a real-time unique experience

Demo
----
the demo is live http://neurobrush.com - data doesn't get updated, but its just to get the idea

Project Structure
-----------------

data_publisher (Java Code)
--------------
Runs this one locally.
Reads data from Emotiv helmet or Emotiv emulator, sanitize it, encode it,
and send it to the server

neurobrush_web (Django)
--------------
Djano app that act as the server endpoint
It exposes 2 methods: collect and getlatestdata
collect will recieve data from your local computer
getlatestdata will output the latest data in a json format
the base.html also contains a live socket that updates when getlatestdata updates


How do I make it run?
-----------------------
Configuration

Locally:
Update EmoStateLog.java. set targetURL

Server:
Setup a server (We've used Heroku) that runs the django neurobrush_web.
Under neurobrush_web->site->templates->collect.py set REDIS_URL
Under neurobrush_web->site->templates->getlatestdata.py set REDIS_URL

Others
------

cpp_web_socket
-------------
a half baked work - you can hack it if you prefer c++ over java as the data_publisher
