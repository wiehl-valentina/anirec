import discord
import requests
import json

def getRec():
    response = requests.get('https://api.jikan.moe/v4/random/anime')
    json_data = json.loads(response.text)
    print(json_data['data']['url'])
    return json_data['data']['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith('!rec'):
            try:
                await message.channel.send(getRec())
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
        

intents = discord.Intents.default(); 
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN')