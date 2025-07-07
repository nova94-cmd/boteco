# bot.py
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ola'):
        await message.channel.send(f'Olá, {message.author.mention}!')
    
    if message.content.startswith('!info'):
        await message.channel.send('Sou um bot de testes!')

client.run(os.getenv('DISCORD_TOKEN'))