import discord
from discord.ext import commands
import pynite


class Fortnite:
    '''
    Example cog for a Discord bot made through the discord.py ext.commands framework.

    Requirements
    --------------
        discord.py rewrite
        python 3.5+
        pynite v1.3.0+
    '''

    def __init__(self, bot):
        self.bot = bot
        self.client = pynite.Client('token', timeout=5)

    @commands.command()
    async def profile(self, ctx, platform, name):
        '''Fetch a profile.'''

        player = await self.client.get_player(platform, name)
        solos = await player.get_solos()

        await ctx.send("# of kills in solos for {}: {}".format(name,solos.kills.value))


def setup(bot):
    bot.add_cog(Fortnite(bot))
