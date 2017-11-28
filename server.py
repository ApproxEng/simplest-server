from datetime import datetime
from functools import wraps, update_wrapper

from flask import Flask, request, make_response
from gevent.wsgi import WSGIServer

app = Flask(__name__, static_url_path='')


def nocache(view):
    """
    A bit of magic - adding this as a decorator to a route will absolutely prevent the returned content being cached
    by the browser. You should only use this if you're certain that this is what you want! Caching is generally a good
    thing for performance.
    """

    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


@app.route('/')
@nocache
def hello_world():
    """
    Dead simple. Always returns the same actual HTML content, but if called with ?action=yes or ?action=no will print
    a message on the console of the server to that effect. Obviously in reality you'd want to put something more useful
    like driving your robot forward or something.
    """
    action = request.args.get('action')
    if action is not None:
        if action == 'yes':
            print('Yes selected!')
        if action == 'no':
            print('No selected!')
    return app.send_static_file('index.html')


http_server = WSGIServer(('', 8000), app)
http_server.serve_forever()
