from flask import render_template, jsonify
from FlaskWebProject import app
import logging

@app.route('/')
def home():
    logging.warn("Warning, log working!!!")
    return jsonify({
        "test": "hello"
    })
