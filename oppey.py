import os
import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.INFO)
chatbot = ChatBot(
    'OppeyML',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # logic_adapters=[
    #     'chatterbot.logic.MathematicalEvaluation',
    #     'chatterbot.logic.TimeLogicAdapter',
    #     'chatterbot.logic.BestMatch'
    # ],
    database_uri='sqlite:///database.db'
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
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
      print('{0.author}: {0.content}'.format(message))
      # 
      # print('OppeyML: {0}'.format(response))
      
      if is_oppey or is_self:
        return
      if is_bot_channel:
        response = chatbot.get_response(message.content)
        await message.channel.send(response)
        
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