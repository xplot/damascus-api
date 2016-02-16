import logging
import importlib
import logging
from types import ModuleType


class MissingTransformationError(Exception):
    pass


class FileTransformerQuery(object):

    def __init__(self, partner_id, message_type):
        self.partner_id = partner_id
        self.message_type = message_type

    def query(self):
        transform_module = "pipeline.%s" % self.message_type
        try:
            mod = importlib.import_module(transform_module)
            return getattr(mod, 'transform', None)

        except Exception, e:
            logging.exception(e)
            raise MissingTransformationError(self.partner_id, self.message_type)