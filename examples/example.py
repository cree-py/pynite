import pynite  # this is the module
# Other required modules (should bundle with pynite in setup)
import aiohttp
import asyncio

token = ''  # this is your api key from https://fortnitetracker.com/site-api


# Async loop.
async def main():

    # Create a client
    client = pynite.Client(token, session=aiohttp.ClientSession())

    platform = 'pc'  # Platform can be pc, psn, or xbl
    name = 'umbresp'  # epics game username

    # Get a Profile.
    profile = await client.get_player(platform, name)
    solos = await client.get_solos(platform, name)

    # Print your number of Kills in Solo. (Docs coming soon, and an easier way to access exact info.)
    print(profile.account_id)  # prints account id
    print(solos.kills.value)  # prints the number of kills you have

# Run the async loop!
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
