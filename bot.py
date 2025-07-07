import discord
   import os
   from discord.ext import commands

   intents = discord.Intents.default()
   intents.message_content = True

   bot = commands.Bot(command_prefix='!', intents=intents)

   @bot.event
   async def on_ready():
       print(f'Bot {bot.user.name} online!')

   @bot.command()
   async def ola(ctx):
       await ctx.send(f'Olá, {ctx.author.mention}!')

   @bot.command()
   async def info(ctx):
       await ctx.send('Bot de teste sem voz!')

   TOKEN = os.getenv('DISCORD_TOKEN')
   bot.run(TOKEN)
