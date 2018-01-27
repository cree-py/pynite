'''
MIT License

Copyright (c) 2018 RBC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import aiohttp
from .utils import API
from .errors import NotResponding, Unauthorized, NoProfileFound, NotPlayedError
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
        async with self.session.get(f'http://api.fortnitetracker.com/v1/profile/{platform}/{name}', headers=self.headers) as resp:
            if 500 > resp.status > 400:
                raise Unauthorized()
            elif resp.status >= 500:
                raise NotResponding()
            elif resp.status == 200:
                raw_data = await resp.json()
            else:
                raise NoProfileFound()

        data = Box(raw_data, camel_killer_box=True)
        self.platform = platform
        self.name = name

        return data

    async def get_solos(self, platform, name):
        self.profile = await self.get_player(platform, name)
        try:
            return self.profile.stats.p2
        except AttributeError:
            raise NotPlayedError('solos')

    async def get_duos(self, platform, name):
        self.profile = await self.get_player(platform, name)
        try:
            return self.profile.stats.p10
        except AttributeError:
            raise NotPlayedError('duos')

    async def get_squads(self, platform, name):
        self.profile = await self.get_player(platform, name)
        try:
            return self.profile.stats.p9
        except AttributeError:
            raise NotPlayedError('squads')


class Player(Client):

    def __init__(self):
        super().__init__(Client)

    def __repr__(self):
        return '<Player object>'

    async def get_solos(self):
        try:
            return self.profile.stats.p2
        except AttributeError:
            raise NotPlayedError('solos')

    async def get_duos(self):
        try:
            return self.profile.stats.p10
        except AttributeError:
            raise NotPlayedError('duos')

    async def get_squads(self):
        try:
            return self.profile.stats.p9
        except AttributeError:
            raise NotPlayedError('squads')
