import aiohttp
import json


class Client:
    '''
    A client that gets data from fortnitetracker.com
    This is async.

    Parameters
    -------------
    token: str
        The API key that can be requested from fortnitetracker.com
    session: Optional[Session]
        The http (client)session to be used for requests. Must be an aiohttp.ClientSession because this is async.
    camel_case: Optional(bool)
        Whether or not to access data keys in snake_case or camelCase,
        this defaults to False (snake_case)
    '''

    def __init__(self, token, session=None, camel_case=False):
        self.token = token
        self.session = session or aiohttp.ClientSession()
        self.camel_case = camel_case
        self.headers = {
            'TRN-Api-token': token,
            'user-agent': 'python-fortnite-client (SharpBit)'
        }

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.session.close()

    def __repr__(self):
        return f'<FortniteBRClient>'
