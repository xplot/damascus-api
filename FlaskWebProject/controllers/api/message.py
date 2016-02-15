from flask import render_template, jsonify, request
from init import webApp

@webApp.route('/api/message')
def get_message():
    return jsonify({
        "message": [

        ]
    })

@webApp.route('/api/message', methods=['POST'])
def post_message():
    input_json = request.get_json(force=True)
    return jsonify(input_json)