import os
import discord
import asyncio

client = discord.Client()

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

client.run(os.environ['DISCORD_TOKEN'])
