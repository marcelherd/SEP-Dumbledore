import os
import sys
import asyncio
import logging

try:
    import discord
except ImportError:
    sys.exit('You must install discord.py first.')

logging.basicConfig(level = logging.INFO)

client = discord.Client()

token = None

if len(sys.argv) > 1:
    token = sys.argv[1]
else:
    token = os.environ.get('DISCORD_TOKEN')

if token is None:
    sys.exit('You must set the environment variable DISCORD_TOKEN or pass the token as first argument.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('?contribute'):
        await client.send_message(message.channel, '<https://github.com/marcelherd/SEP-Dumbledore>')

client.run(token)