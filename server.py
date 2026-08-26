#!/usr/bin/env python3
"""Static file server that listens on the port portless assigns via $PORT.
Usage: python server.py   (serves the directory containing this file)
"""
import http.server
import os
import socketserver

port = int(os.environ.get("PORT", "8000"))
host = os.environ.get("HOST", "127.0.0.1")
webroot = os.path.dirname(os.path.abspath(__file__))

os.chdir(webroot)

Handler = http.server.SimpleHTTPRequestHandler

class Quiet(Handler):
    def log_message(self, *args):
        pass

with socketserver.TCPServer((host, port), Quiet) as httpd:
    print(f"Serving {webroot} on {host}:{port}", flush=True)
    httpd.serve_forever()
