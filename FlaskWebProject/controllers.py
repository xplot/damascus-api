"""
Routes for the damascus-api.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app, jsonify

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return jsonify({"test": "hello"})
