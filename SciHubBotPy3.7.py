import discord
from urllib.parse import urlparse
import urllib.request
#import sys

#sys.stdout = open("log.txt", "a")

#ctx=context

client = discord.Client()

scihub = 'https://scihubtw.tw/'

@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='Sci-Hub: removing barriers in the way of science'))      


@client.event
async def on_message(message):
    #print(message.guild.name, message.channel.mention, message.author, message.content)
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
        SciHubURL = scihub + 'https://' + URL
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
        SciHubURL = scihub + URL
        await message.channel.send(SciHubURL)
    if 'springer.com/' in message.content:
        print("scientific article found!")
        URLIndex = message.content.index('springer.com')
        print(URLIndex)
        URLpartial = message.content[URLIndex:]
        URL = URLpartial.split(' ', 1)[0]
        URL = 'https://www.' + URL
        print(URL)  
        SciHubURL = scihub + URL
        await message.channel.send(SciHubURL)
    if 'nature.com/' in message.content:
        print("scientific article found!")
        URLIndex = message.content.index('nature.com')
        print(URLIndex)
        URLpartial = message.content[URLIndex:]
        URL = URLpartial.split(' ', 1)[0]
        URL = 'https://www.' + URL
        print(URL)  
        SciHubURL = scihub + URL
        await message.channel.send(SciHubURL)
    if 'onlinelibrary.wiley.com' in message.content:
        print("scientific article found!")
        URLIndex = message.content.index('onlinelibrary.wiley.com')
        print(URLIndex)
        URLpartial = message.content[URLIndex:]
        URL = URLpartial.split(' ', 1)[0]
        #URL = 'https://www.' + URL
        print(URL)  
        SciHubURL = scihub + URL
        await message.channel.send(SciHubURL)
    if 'doi.org' in message.content:
        print("scientific article found!")
        URLIndex = message.content.index('doi.org')
        print(URLIndex)
        URLpartial = message.content[URLIndex:]
        URL = URLpartial.split(' ', 1)[0]
        URL = 'https://' + URL
        print(URL)  
        SciHubURL = scihub + URL
        await message.channel.send(SciHubURL)

client.run('[INSERT API KEY HERE]')
