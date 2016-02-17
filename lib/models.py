
class WebHook(object):

    def __init__(self, endpoint_template=None, method=None, headers_template=None, params_template=None, body_template=None, username=None, password=None):
        self.endpoint_template = endpoint_template
        self.method = method
        self.params_template = params_template
        self.headers_template = headers_template
        self.body_template = body_template
        self.username = username
        self.password = password


class Publication(object):

    def __init__(self, endpoint_template=None, method=None, headers=None, params=None, body=None, username=None, password=None, timeout=None):
        self.endpoint_template = endpoint_template
        self.method = method
        self.headers = headers
        self.params = params
        self.body = body
        self.username = username
        self.password = password
        self.timeout = timeout
