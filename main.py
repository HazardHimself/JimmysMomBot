import discord
import requests
import json
import sight
import generate
import random

import uwufunc

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "It's ok to be sad sometimes. It gets better, I promise.",
  "Hang in there! I believe in you!",
  "You are a great person!"
]

global replymode
global replychannel
replymode = False
replychannel = 0

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

  global replymode
  global replychannel

  if message.author == client.user:
    return

  elif message.content.lower().startswith('%quit'):
    quit()

  elif message.content.startswith('%cysm'):
      await message.channel.send(sight.cysm(message.author.nick))

  elif message.content.startswith('%uwu'):
    await message.channel.send((uwufunc.uwufunc(message.content)))

  elif message.content.lower().startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  elif 'sus' in message.content.lower():
    await message.reply("Amongus.")

  elif 'among us' in message.content.lower():
    await message.reply("Sus.")

  elif message.content.lower().startswith('%deny'):
    await message.channel.send('No.')

  elif message.content.lower().startswith('%affirm'):
    await message.channel.send('Yes.')

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  elif message.content.startswith('%replymode'):
    replymode = not replymode
    replystring = "Reply mode is currently set to: " + str(replymode)
    await message.channel.send(replystring)

  elif message.content.startswith('%replychannel'):
    replychannel = message.channel
    replystring = "This is now the only channel I will reply in :)"
    await message.channel.send(replystring)

  elif message.content.startswith('%rand'):
    async with message.channel.typing():
      aigen = generate.aitext(message.content)
    await message.channel.send(aigen)

  # with context ai text generator function
  elif (replymode and (message.channel == replychannel)) or message.content.startswith('%con'):
    maxlen = 2600
    global contstring
    contstring = ""
    for cached in client.cached_messages:
      if cached.channel == replychannel:
        contstring += cached.content + '\n'
    if len(contstring) > maxlen:
      curdiff = len(contstring) - maxlen
      contstring = contstring[curdiff:]
    print(len(contstring))
    async with message.channel.typing():
      aigen = generate.contextgen((contstring))

    if aigen != "":
      await message.channel.send(aigen)
    else:
      await message.channel.send("Sorry, something went wrong. Try again.")

  elif message.content.startswith('%ayb'):
      await message.channel.send(contstring)

client.run('')