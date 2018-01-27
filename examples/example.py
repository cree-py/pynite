import pynite  # this is the module
import asyncio

token = ''  # this is your api key from https://fortnitetracker.com/site-api
# do not post this on public github repos.
# We are not responsible for your loss


# Async loop.
async def main():

    # Construct the client
    client = pynite.Client(token, timeout=5)

    platform = 'pc'  # Platform can be pc, psn, or xbl
    name = 'muselk'  # epic games username

    # Documentation about this coming soon
    player = await client.get_player(platform, name)
    solos = await player.get_solos()
    duos = await player.get_duos()
    squads = await player.get_squads()

    # currently player attributes are in camelCase
    # all solos, duos, and squad attributes are in snake_case
    print(player.accountId)  # prints account id
    print(solos.kills.value)  # prints the number of kills you have
    print(duos.avg_time_played.display_value)
    print(squads.top3.value)

# Run the async loop!
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
