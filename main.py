import discord
import requests
import json
import sight
from discord.ext import commands

import uwufunc

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith('%cysm'):
      await message.channel.send(sight.cysm(message.author.nick))

  if message.content.startswith('%uwu'):
    await message.channel.send((uwufunc.uwufunc(message.content)))

  if message.content.lower().startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.lower().startswith('%deny'):
    await message.channel.send('No.')

  if message.content.lower().startswith('%affirm'):
    await message.channel.send('Yes.')

client.run('OTA2OTk2ODk3NjA3MjAwODU4.YYgwrw.86iXe1S48t0-WRRd0YZt7A26bzU')