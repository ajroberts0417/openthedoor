import discord
from discord import Intents
from discord.ext import commands


## SETUP DISCORD BOT
DISCORD_BOT_TOKEN = 'MTA5NTAxMjcyNDg1OTIwNzY4MA.GyHamB.nA02cLbk4qEZlUSlXTDELqNniCC4DLYWmPt2F4'  # Replace with your bot's token

intents = Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')


def send_message_to_openthedoor_channels(caller_number):
    print("Sending message to openthedoor channels")
    for guild in bot.guilds:
        print(f"Sending message to {guild.name}")
        channel = discord.utils.get(guild.channels, name='openthedoor')
        if channel is not None:
            print(f"Sending message to {channel.name}")
            channel.send(f'OpenTheDoor received a call from {caller_number}.')
