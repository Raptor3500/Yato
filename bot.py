import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='yato')
aiosession = aiohttp.ClientSession(loop=bot.loop)
ownerID = "274298631517896704"

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
  
  # Make me say shit
@bot.command(pass_context=True)
async def say(ctx, *args):
    if ctx.message.author.id ==! ownerID:
        await bot.say("You are not allowed to run this command!")
    else:
        channel = ctx.message.channel
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        await bot.send_typing(channel)
        await asyncio.sleep(1)
        await bot.say(mesg)
        print (ctx.message.author.id + " or " + ctx.message.author.name + " made me say '{}'".format(mesg))
  



bot.run(os.environ.get('Token'))
