import aiohttp
import json

async def open_session(platform, name):
    platform = platform.lower()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.fortnitetracker.com/v1/profile/{platform}/{name}', headers=headers) as resp:
                data = await resp.json()
    except Exception as e:
        return e # until we implement errors
