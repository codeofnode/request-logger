#!/usr/bin/env python

import sys, BaseHTTPServer
from mylogger import logging
logger = logging.getLogger(__name__)

class RESTRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        logger.warn({ 'dic' : 12})
        self.send_response(200)
        self.end_headers()

def rest_server(port):
    'Starts the REST server'
    http_server = BaseHTTPServer.HTTPServer(('', port), RESTRequestHandler)
    print 'Starting HTTP server at port %d' % port
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
        print 'Stopping HTTP server'
        http_server.server_close()

def main(argv):
    rest_server(8080)

if __name__ == '__main__':
    main(sys.argv[1:])
