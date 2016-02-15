import logging

from flask import Flask
webApp = Flask(__name__)
logging.basicConfig(filename='logs.txt', level=logging.DEBUG)

import FlaskWebProject


if __name__ == '__main__':
    print "running"
    webApp.run(debug=True)


