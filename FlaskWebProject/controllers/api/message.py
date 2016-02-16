from flask import render_template, jsonify, request
from FlaskWebProject import app
from lib.query.message_info import MessageInfoQuery
from lib.command.process_message_command import ProcessMessageCommand

@app.route('/api/message')
def get_message():
    return jsonify({
        "message": [

        ]
    })

@app.route('/api/message/<message_type>', methods=['POST'])
def post_message(message_type):

    message_info = MessageInfoQuery(message_type).query()

    if message_info['async']:
        return jsonify(
            "Not able to handle async yet"
        )
    else:
        a = ProcessMessageCommand(
                message_info,
                request.get_json(force=True) or {}
            ).execute()
        return jsonify(
            a
        )
