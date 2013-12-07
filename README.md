About the project
=================
At a weekend long Hackathon @Google Campus, Tel Aviv (<http://brainihack.org/>)
we decided to create a machine that reads brainwaves of users using an Emotiv device,
and output those users’ feeling into the web.


A project by [@galbracha](https://twitter.com/galbracha) [@bArmageddon](https://twitter.com/bArmageddon) [@Jishai](https://twitter.com/Jishai) [@daniik](https://twitter.com/DaniiK) [@yitzikc](https://twitter.com/yitzikc)
![The team](https://raw.github.com/rootux/neurobrush/master/demo/images/the_team.jpg "The team")

We "accidently" created a by-product that exposes the Emotiv data to the web in a JSON format.

By doing so we allow JavaScript developers to write on top of what we did and create a unique real-time experience.

Demo
====
The demo is live <http://neurobrush.com> - the data doesn't get updated, but it gives you the idea and feeling of the project. 
![Live demo](https://raw.github.com/rootux/neurobrush/master/demo/images/demo.png "Live demo")

Project Structure
================

Local - data_publisher (Java Code)
--------------
Run this one locally. Reads data from Emotiv helmet or Emotiv emulator, sanitize it, encode it, and send it to the server.

Server - neurobrush_web (Django)
--------------
Django app that acts as the server endpoint. It exposes 2 methods: `collect()` and `getlatestdata()`
collect() will receive data from your local computer
getlatestdata() will output the latest data in a JSON format. The base.html also contains a live socket that updates when getlatestdata updates.



How to make it run?
====================
Configuration

**Locally**:

 1.Connect a Emotiv helmet, or use EmoCompser (the emulator)

 2.Update EmoStateLog.java. set targetURL

**Server**:

 1.Setup a server (We've used Heroku) that runs the django neurobrush_web.

 2.Under neurobrush_web->site->templates->collect.py set REDIS_URL

 3.Under neurobrush_web->site->templates->getlatestdata.py set REDIS_URL

Released under MIT license (see LICENSE).

ENJOY! 
