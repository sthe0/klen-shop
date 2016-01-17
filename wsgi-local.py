#!/usr/bin/env python2
import flask_app
from wsgiref import simple_server
import sys

port = 8051
if len(sys.argv) > 1:
    port = int(sys.argv[1])

httpd = simple_server.make_server('localhost', port, flask_app.app)
httpd.serve_forever()

