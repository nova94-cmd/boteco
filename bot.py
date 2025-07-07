import os
import discord
from discord.ext import commands

# Configuração para evitar módulos problemáticos
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = False  # Desativa voz para evitar audioop

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

@bot.command()
async def info(ctx):
    await ctx.send('Sou um bot de teste!')

@bot.command()
async def dado(ctx):
    import random
    await ctx.send(f'{ctx.author.mention} rolou um dado: **{random.randint(1,6)}**')

if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if token:
        bot.run(token)
    else:
        print("Token não encontrado. Verifique a variável de ambiente DISCORD_TOKEN.")
