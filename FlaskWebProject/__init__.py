"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
import logging
logging.basicConfig(filename='logs.txt',level=logging.DEBUG)

import FlaskWebProject.controllers
