from flask import render_template, jsonify, request
from FlaskWebProject import app

@app.route('/api/message')
def get_message():
    return jsonify({
        "message": [

        ]
    })

@app.route('/api/message', methods=['POST'])
def post_message():
    input_json = request.get_json(force=True)
    return jsonify(input_json)