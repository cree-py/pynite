import aiohttp
from .utils import API, _to_snake_case
from box import Box


class Client:

    def __init__(self, token, session=None):
        self.token = token
        self.session = session or aiohttp.ClientSession()
        self.headers = {
            'TRN-Api-token': token
        }

    def __repr__(self):
        return '<FortniteBR-Client>'

    async def get_player(self, platform, name):
        platform = platform.lower()
        if platform not in ('xbl', 'psn', 'pc'):
            raise ValueError('Incorrect platform passed. Options: xbl, psn, pc')
        async with self.session.get(f'{API.PLAYER}/{platform}/{name}', headers=self.headers) as resp:
            try:
                raw_data = await resp.json()
            except Exception as e:
                return e  # until we implement errors

        data = Box(raw_data)

        return data
