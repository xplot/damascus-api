"""
Routes for the damascus-api.
"""

from flask import render_template, jsonify
from FlaskWebProject import app
import logging

@app.route('/')
def home():
    print "this is a test log"
    logging.warn("Warning, log working!!!")
    return jsonify({"test": "hello"})
