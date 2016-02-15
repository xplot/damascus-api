from flask import render_template, jsonify
from init import webApp
import logging

@webApp.route('/')
def home():
    logging.warn("Warning, log working!!!")
    return jsonify({
        "test": "hello"
    })
