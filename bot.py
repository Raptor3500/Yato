import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='yato')
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
  
  # Make me say stuff
@bot.command(pass_context=True)
async def say(ctx, *args):
    if ctx.message.author.id in ownerID:
        channel = ctx.message.channel
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        await bot.send_typing(channel)
        await asyncio.sleep(1)
        await bot.say(mesg)
        print (ctx.message.author.id + " or " + ctx.message.author.name + " made me say '{}'".format(mesg))
    else:
      await bot.say("You are not allowed to run this command!")
      
      # I want to kill people
@bot.command(pass_context=True)
async def kill(ctx, user: discord.Member=None):
        if user is None:
            await bot.say(ctx.message.author.mention + ": I can't kill anyone unless you tell me who to kill!")
            return
        if user.id == "489775956731363328":
            await bot.say(ctx.message.author.mention + ": I won't let you kill me! :knife:")
        elif user.id == ownerID:
            await bot.say(ctx.message.author.mention + ": Why do you want to kill my developer?")
        elif user.id == ctx.message.author.id:
            await bot.say(ctx.message.author.mention + ": Why do you want me to kill you?")
            
            #My invite link
            @bot.command(pass_context=True)
async def inviteme(ctx):
    await bot.say("Here is my invite link!")
    await bot.say("https://discordapp.com/api/oauth2/authorize?client_id=489775956731363328&permissions=8&scope=bot")
         
  



bot.run(os.environ.get('Token'))
