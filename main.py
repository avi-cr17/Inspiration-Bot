import discord
import os
import requests
import json
import random
from replit import db
from kee_alive import keep_alive






def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+" -"+json_data[0]['a']
  return quote


def update_encouragement(enc_msg):
  if("encouragements") in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(enc_msg)
    db["encouragements"]=encouragements

  else:
    db["encouragements"] = [enc_msg]


def delete_encouragement(index):
  encouragements = db["encouragements"]

  if len(encouragements)>index:
    del encouragements[index]
    db["encouragements"]=encouragements

#getting intents

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)


sad_words=["sad","depressed","unhappy","angry","miserable"]

starter_encouragements = [
  "Cheer up",
  "Hang in there",
  "Dont give up"
]




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))


@client.event
async def on_member_join(member):
  print('NEW MEMEBER JOINED')
  guild= member.guild
  print(guild)
  if(guild.id==827206800788291646):
    print('entered here 1')
    channel = guild.get_channel(827206801324900396)
    await channel.send(f'{member.mention} bhai, welcome to the steam.Enjoy ')
  if(guild.id==831528087401005156):
    channel = guild.get_channel(831528087401005159)
    await channel.send(f'{member.mention} bhai, welcome to the steam.Enjoy ')



  

  
keep_alive() 
client.run(os.getenv('TOKEN'))

  

