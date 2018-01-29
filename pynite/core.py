import aiohttp
from .utils import API
from .errors import NotResponding, Unauthorized, NotFound, NoGames
from box import Box
import asyncio


class Client:
    '''
    The client class that starts everything. From this, you can get
        - Full Player statistics
        - Solo gamemode stats
        - Duos gamemode stats
        - Squads gamemode stats

    This is an async wrapper and client.

    Parameters
    -----------

        token: str
            The api key you can get from
            https://fortnitetracker.com/site-api
        timeout: Optional[int]:
            Quits requests to the API after a number of seconds. Default=10

    Example:

        client = pynite.Client(os.getenv('fntoken'), session=aiohttp.ClientSession(), timeout=5)

    Methods
    --------

        get_id(platform, epic_username):
            Get player ID.
        get_player(platform, epic_username):
            Get player statstics.
        get_solos(platform, epic_username):
            Get statistics for a player's solo games.
        get_duos(platform, epic_username):
            Get statistics for a player's duo games.
        get_squads(platform, epic_username):
            Get statistics for a player's squad games.
        get_lifetime_stats(platform, epic_username):
            Get total lifetime statistics for a player.
    '''

    def __init__(self, token, timeout=10):
        self.token = token
        self.session = aiohttp.ClientSession()
        self.timeout = timeout
        self.headers = {
            'TRN-Api-key': token
        }

    def __repr__(self):
        return f'<FortniteBR-Client> timeout={self.timeout}>'

    def __del__(self):
        self.session.close()

    async def get_player(self, platform, name):
        platform = platform.lower()
        if platform not in ('xbl', 'psn', 'pc'):
            raise ValueError('Incorrect platform passed. Options: xbl, psn, pc')
        try:
            async with self.session.get(f'{API.PLAYER}/{platform}/{name}', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    raw_data = await resp.json()
                elif 500 > resp.status > 400:
                    raise Unauthorized()
                else:
                    raise NotFound()
        except asyncio.TimeoutError:
            raise NotResponding()

        data = Box(raw_data, camel_killer_box=True)
        player = Player(data)

        return player

    async def get_id(self, platform, name):
        profile = await self.get_player(platform, name)
        return profile.get_id()

    async def get_solos(self, platform, name):
        profile = await self.get_player(platform, name)
        return profile.get_solos()

    async def get_duos(self, platform, name):
        profile = await self.get_player(platform, name)
        return profile.get_duos()

    async def get_squads(self, platform, name):
        profile = await self.get_player(platform, name)
        return profile.get_squads()

    async def get_lifetime_stats(self, platform, name):
        profile = await self.get_player(platform, name)
        return profile.get_lifetime_stats()


class Player(Box):
    '''Returns a full player object with all
    of its statistics.

    Methods
    --------

        get_id():
            Get the player's Epic Games ID.
        get_solos():
            Get the player's solo stats.
        get_duos():
            Get the player's duo stats.
        get_squads():
            Get the player's squad stats.
        get_lifetime_stats():
            Get the player's lifetime stats.
    '''

    def __repr__(self):
        return f'<Player object name={self.epicUserHandle} id={self.accountId}>'

    async def get_id(self):
        try:
            return self.account_id
        except AttributeError:
            raise NoGames('')

    async def get_solos(self):
        try:
            return self.stats.p2
        except AttributeError:
            raise NoGames('solos')

    async def get_duos(self):
        try:
            return self.stats.p10
        except AttributeError:
            raise NoGames('duos')

    async def get_squads(self):
        try:
            return self.stats.p9
        except AttributeError:
            raise NoGames('squads')

    async def get_lifetime_stats(self):
        try:
            return self.life_time_stats
        except AttributeError:
            raise NoGames('the game or any of its')
