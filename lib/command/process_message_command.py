from ..query.pipeline_query import PipelineQuery


class ProcessMessageCommand(object):

    def __init__(self, message_info, input):
        self.message_info = message_info
        self.input = input

    def execute(self):
        pipeline = PipelineQuery(self.message_info['pipeline']).query()
        return pipeline(input)