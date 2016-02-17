from flask import render_template, jsonify, request
from FlaskWebProject import app
from lib.command.process_message_command import ProcessMessageCommand
from lib.command.process_event_command import ProcessEventCommand
from lib.command.send_publication_command import SendPublicationViaHttpCommand

class NotImplemented(Exception):
    pass

@app.route('/api/message/<message_type>', methods=['GET'])
def get_message(message_type):
    raise NotImplemented

@app.route('/api/message/<message_type>', methods=['POST'])
def post_message(message_type):

    event = ProcessMessageCommand(
        message_type,
        request.get_json(force=True) or {}
    ).execute()

    publications = ProcessEventCommand(message_type, event).execute()

    #This will go in a queue...
    for publication in publications:
        SendPublicationViaHttpCommand(publication).execute()

    return jsonify({
        'status': 200,
        'message': 'Processed'
    })
