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
  
  # Set my game
@bot.command(hidden=True, pass_context=True)
async def setgame(ctx, *args):
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == unrealismID:
        game = ' '.join(args)
        server = ctx.message.server
        current_status = server.me.status if server is not None else None
        if game:
            game = game.strip()
            await bot.change_presence(game=discord.Game(name=game), status=current_status)
            await bot.say("Game set to `{}`.".format(game))
            print ("Game set to '{}'".format(game))
        else:
            await bot.change_presence(game=None, status=current_status)
            await bot.say("Not playing a game now.")
            print ("Not playing a game")
    else:
        await bot.say("You're not allowed to run this command!")



bot.run(os.environ.get('Token'))
