from lib.models import WebHook

class EventWebhookQuery(object):

    def __init__(self, event):
        self.event = event

    def query(self):

        event_webhooks = {
            'smsout': [
                WebHook(
                    endpoint_template='http://iwanttodemo.appspot.com/event',
                    body_template='phone={{ phone }}&message={{message}}',
                    method='POST'
                )
            ]
        }

        return event_webhooks[self.event]