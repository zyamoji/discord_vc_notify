from os import sync
import discord
from datetime import datetime, time, timedelta

def getToken(filePath):
    with open(filePath, 'r', encoding="UTF-8") as f:
        data = f.read()
        return data
    
TOKEN = getToken("token")
SERVER_ID = 937003318750900325
TXT_ID = 937003319199674369

print("Success > Got token and SERVER and TEXT ID.")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Success > Login.")

@client.event
async def on_voice_state_update(member, before, after):
    print(f"Log > Event was called.")
    if member.guild.id == SERVER_ID:
        if before.channel != after.channel:
            now = datetime.utcnow() + timedelta(hours=9)
            alert_channel = client.get_channel(TXT_ID)
            if before.channel is None:
                msg = f"== {now:%m/%d %H:%M} ==\n{member.name} さん <#{after.channel.id}> へようこそ！"
                print(msg)
                await alert_channel.send(msg)
            elif after.channel is None:
                msg = f"== {now:%m/%d %H:%M} ==\n{member.name} さん <#{before.channel.id}> へまた来てね！"
                print(msg)
                await alert_channel.send(msg)

client.run(TOKEN)