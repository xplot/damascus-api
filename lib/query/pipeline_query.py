import logging
import importlib
import logging
from types import ModuleType


class MissingTransformationError(Exception):
    pass


class PipelineQuery(object):

    def __init__(self, message_type):
        self.message_type = message_type

    def query(self):
        transform_module = "pipeline.%s" % self.message_type
        try:
            mod = importlib.import_module(transform_module)
            return getattr(mod, 'execute', None)

        except Exception, e:
            logging.exception(e)
            raise MissingTransformationError(self.message_type)