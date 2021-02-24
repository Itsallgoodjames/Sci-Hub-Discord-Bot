#Sci-Hub Discord Bot V1.0

import discord
from urllib.parse import urlparse
import urllib.request

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('Test')
    if 'pubs.acs.org/' in message.content:
        print("scientific article found!")
        URLIndex = message.content.index('pubs.acs.org')
        print(URLIndex)
        URLpartial = message.content[URLIndex:]
        URL = URLpartial.split(' ', 1)[0]
        print(URL)
        SciHubURL = 'https://sci-hub.se/' + 'https://' + URL
        print(SciHubURL)
        await message.channel.send(SciHubURL)
    if 'sciencedirect.com/' in message.content:
        print("scientific article found!")
        URLIndex = message.content.index('sciencedirect.com')
        print(URLIndex)
        URLpartial = message.content[URLIndex:]
        URL = URLpartial.split(' ', 1)[0]
        URL = 'https://www.' + URL
        print(URL)
        SciHubURL = 'https://sci-hub.se/' + URL
        await message.channel.send(SciHubURL)
        
        
client.run('ODEzNDA1NjE2MDM0Njc2Nzc2.YDO1Aw.itt01sez-mGNuKcMkbvOYrYlukc')
