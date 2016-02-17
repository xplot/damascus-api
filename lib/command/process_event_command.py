import json
from lib.command.template_replace_command import TemplateReplaceCommand
from lib.command.send_publication_command import SendPublicationViaHttpCommand
from lib.query import EventWebhookQuery
from lib.models import Publication

class ProcessEventCommand(object):

    def __init__(self, event_type, event):
        self.event_type = event_type
        self.event = event

    def execute(self):

        publications = []

        for webhook in EventWebhookQuery(self.event_type).query():
            publication = Publication(
                method=webhook.method,
                username=webhook.username,
                password=webhook.password
            )

            publication.endpoint = TemplateReplaceCommand(webhook.endpoint_template, self.event).execute()

            if webhook.params_template:
                publication.params = TemplateReplaceCommand(webhook.params_template, self.event).execute()

            if webhook.body_template:
                publication.body = TemplateReplaceCommand(webhook.body_template, self.event).execute()

            if webhook.headers_template:
                print TemplateReplaceCommand(webhook.headers_template, self.event).execute()
                publication.headers = json.loads(TemplateReplaceCommand(webhook.headers_template, self.event).execute())

            publications.append(publication)

        return publications