from jinja2 import Template


class TemplateReplaceCommand(object):

    def __init__(self, template, data):
        self.template = template
        self.data = data

    def execute(self):
        if not self.template:
            return None
        self.template = self.template.decode('string_escape')
        template = Template(self.template)
        return template.render(self.data).replace('"', '')