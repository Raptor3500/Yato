import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='yato')

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")

@client.command(pass_context=True)
async def help(ctx)
author = ctx.message.author


embed = discord.Embed(
  colour = discord.colour.orange()
)

embed.set_author(name'Help')
embed.add_field(name= '.ping', value-'Returns Pong!', inline-False)

await client.send_message(author, embed-embed)



bot.run(os.environ.get('Token'))
