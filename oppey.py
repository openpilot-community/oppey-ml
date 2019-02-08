import os
import aiohttp
import discord
from dotenv import load_dotenv
load_dotenv()
async def fetch(session, url):
  async with session.get(url) as response:
    return await response.text()
class MyClient(discord.Client):
    async def on_ready(self):
      # print(.get(name="Oppey"))
      
      self.oppey = discord.utils.get(self.guilds[0].members,name='Oppey')
      
      print('Logged on as {0}!'.format(self.user))
      print('Oppey bot is {0}'.format(self.oppey))
    
    async def on_message(self, message):
      if self.oppey:
        is_oppey = (message.author.id == self.oppey.id)
      else:
        is_oppey = True
      is_self = (message.author.id == self.user.id)
      is_bot_channel = (message.channel.name == "dev-oppey-bot")
      print('Is Oppey? {1} {0.author}: {0.content}'.format(message, is_oppey or is_self))
      # 
      async with aiohttp.ClientSession() as self.httpClient:
      # print('OppeyML: {0}'.format(response))
      if is_oppey or is_self:
        return
      if is_bot_channel:
        async with self.httpClient.get() as response:
          return await response.text()
        
      # print("author: {0}".format(message.author.id))
      # print("self: {0}".format(self.user.id))
      # print("is_oppey: {0}".format(is_oppey))
      # print("is_self: {0}".format(is_self))
      # print("is_bot_channel: {0}".format(is_bot_channel))
      
      
      # if is_bot_channel:
        
      # else:
      #   print('Possible: {0}'.format(response))

client = MyClient()
client.run(os.environ.get('OPPEY_ML_TOKEN'))