import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='prefix')

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is Yato" + bot.user.name)
  print ("With the ID:489775956731363328" + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")



bot.run(os.environ.get('Token'))
