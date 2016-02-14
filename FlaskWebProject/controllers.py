"""
Routes for the damascus-api.
"""

from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return jsonify({"test": "hello"})
