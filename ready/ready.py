import discord
import asyncio

class ready():
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print ("------")
        print ("Hey, my name is " + self.bot.user.name + ".")
        print ("My ID is " + self.bot.user.id)
        print ("------")
        await self.bot.change_presence(game=discord.Game(name='v2'))


def setup(bot):
    bot.add_cog(ready(bot))
