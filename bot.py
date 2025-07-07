import os
import sys
import discord
from discord.ext import commands

# Solução para o erro do audioop em Python 3.13
try:
    import audioop
except ModuleNotFoundError:
    # Cria um módulo falso para audioop
    class FakeAudioop:
        def __getattr__(self, name):
            return None
    sys.modules['audioop'] = FakeAudioop()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def dado(ctx):
    import random
    await ctx.send(f'Dado: {random.randint(1, 6)}')

# Inicialização
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print("Token não encontrado!")
