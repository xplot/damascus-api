from ..query.pipeline_query import PipelineQuery


class ProcessMessageCommand(object):

    def __init__(self, pipeline, input):
        self.pipeline = pipeline
        self.input = input

    def execute(self):
        pipeline = PipelineQuery(self.pipeline).query()
        return pipeline(self.input)