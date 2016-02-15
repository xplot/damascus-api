"""
Routes for the damascus-api.
"""

from flask import render_template, jsonify
from FlaskWebProject import app

@app.route('/')
def home():
    return jsonify({"test": "hello"})
