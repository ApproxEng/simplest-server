# Simplest Server

This is about as simple as it's possible to make a fully functional Python web server. It uses
Flask and GEvent, returns a single bit of static HTML and shows how the server can receive and
handle URL parameters. Hacked up quickly during a Raspberry Pi Pioneers session to allow one of
the teams to control their USB missile launcher from a web page.

## Dependencies

This uses GEvent and Flask, so you'll need to install those. As usual, I recommend working in a virtual environment - in this case I'm using Python3.6 on my mac, but it should be similar with any other setup.

```
Tengu:~ tom$ virtualenv server-env --python=python3.6
Running virtualenv with interpreter /usr/local/bin/python3.6
Using base prefix '/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/tom/server-env/bin/python3.6
Also creating executable in /Users/tom/server-env/bin/python
Installing setuptools, pip, wheel...done.
Tengu:~ tom$ source server-env/bin/activate
(server-env) Tengu:~ tom$ pip install gevent
Collecting gevent
  Using cached gevent-1.2.2-cp36-cp36m-macosx_10_6_intel.whl
Collecting greenlet>=0.4.10 (from gevent)
Installing collected packages: greenlet, gevent
Successfully installed gevent-1.2.2 greenlet-0.4.12
(server-env) Tengu:~ tom$ pip install flask
Collecting flask
  Using cached Flask-0.12.2-py2.py3-none-any.whl
Collecting Jinja2>=2.4 (from flask)
  Using cached Jinja2-2.10-py2.py3-none-any.whl
Collecting itsdangerous>=0.21 (from flask)
Collecting click>=2.0 (from flask)
  Using cached click-6.7-py2.py3-none-any.whl
Collecting Werkzeug>=0.7 (from flask)
  Using cached Werkzeug-0.12.2-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
Installing collected packages: MarkupSafe, Jinja2, itsdangerous, click, Werkzeug, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.12.2 click-6.7 flask-0.12.2 itsdangerous-0.24
(server-env) Tengu:~ tom$ 
```

## Running

You'll probably want to use this code as an example for your own project, but if you really want to run it as is you can - just do:

```
(server-env) Tengu:simplest-server tom$ python server.py 
```

Now go to http://localhost:8000 in your browser. You'll see a couple of links, clicking them should show some stuff on the console you used to launch the server:

```
::ffff:127.0.0.1 - - [2017-11-28 08:11:11] "GET / HTTP/1.1" 200 435 0.005507
::ffff:127.0.0.1 - - [2017-11-28 08:11:11] "GET /favicon.ico HTTP/1.1" 404 342 0.012747
Yes selected!
::ffff:127.0.0.1 - - [2017-11-28 08:11:13] "GET /?action=yes HTTP/1.1" 200 435 0.001039
No selected!
::ffff:127.0.0.1 - - [2017-11-28 08:11:14] "GET /?action=no HTTP/1.1" 200 435 0.000873
```
