__all__ = ['logging']

FORMAT = '%(asctime)s | %(tid)s | %(message)s'

import logging
import BaseHTTPServer
org = BaseHTTPServer.BaseHTTPRequestHandler

current_class = None

class LoggerRequestClass(BaseHTTPServer.BaseHTTPRequestHandler, object):

   def parse_request(self):
       global current_class
       current_class = self
       value =  super(LoggerRequestClass, self).parse_request()
       return value

BaseHTTPServer.BaseHTTPRequestHandler = LoggerRequestClass

def req_extractor(*args, **kargs):
    global current_class
    if current_class and 'X-App-Tid' in current_class.headers:
        return {'tid': current_class.headers['X-App-Tid']}
    return {'tid': 'Nil'}

class CustomLogger(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None):
        reqObj = req_extractor()
        if extra is None: extra = {}
        reqObj.update(extra)
        super(CustomLogger, self)._log(level, msg, args, exc_info, reqObj)

logging.setLoggerClass(CustomLogger)

logging.basicConfig(
        filename='python.log',
        format=FORMAT,
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.DEBUG)
