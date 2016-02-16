import logging

def execute(input_message):

    logging.warn(input_message)

    return {
        'output': "Hello world of input!!!!",
        'your_incomming_message': input_message
    }