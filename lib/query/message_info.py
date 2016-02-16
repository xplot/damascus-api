

class MessageInfoQuery(object):

    def __init__(self, message_type):
        self.message_type = message_type

    def query(self):
        """
            As you can imagine this is a silly implementation in memory
            In the future database can be used
        """
        messages = {
            'shift_response': {
                'pipeline': 'shift_response',
                'async': True
            },
            'send_notifications': {
                'pipeline': 'send_notifications',
                'async': True
            },
            'callin': {
                'pipeline': 'callin',
                'async': False
            },
        }

        return messages[self.message_type]