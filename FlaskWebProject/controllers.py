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
    #log("warn test ajadex")
    return jsonify({"test": "hello"})
