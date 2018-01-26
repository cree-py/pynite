class NotResponding(Exception):
    def __init__(self):
        self.code = 504
        self.error = 'API request timed out, please be patient.'
        super().__init__(self.error)


class RequestError(Exception):
    '''Base class for request errors'''

    def __init__(self, resp, data):
        self.response = resp
        self.code = getattr(resp, 'status', None) or getattr(resp, 'status_code')
        self.method = getattr(resp, 'method', None)
        self.reason = resp.reason
        if isinstance(data, dict):
            self.error = data.get('error')
            if 'message' in data:
                self.error = data.get('message')
        else:
            self.error = data
        self.fmt = '{0.reason} ({0.code}): {0.error}'.format(self)
        super().__init__(self.fmt)


class Unauthorized(RequestError):
    '''Raised when an invalid or blocked API key is passed'''
    pass
