from flask import Flask
app = Flask(__name__)
from mylogger import logging
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    app.logger.error('%s failed to log in', 'User1')
    return 'Hello, World!'
