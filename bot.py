import discord
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Imported dotenv and os modules to use and obtain from env file
token = os.getenv('TOKEN')
print("Token is: " + str(token))

# New class is extended from base class 'discord.Client'
# Base class has methods for common events
# Event - something you listen then respond to
# on_ready() - called when bot login successful
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # on_message() - called anytime new message where bot is located
    # first check - if bot is the one sending message, stops responding to itself
    # second check - see what message starts with to then respond
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello, World!')

# Sets the intents - settings for what bot can access
# Passed into instance of MyClient
# Assigned default() for bot - need to explicitly allow message interaction
intents = discord.Intents.default()
intents.message_content = True

# Instantiates MyClient + calls run() to start client
# Uses token to authenticate itself
client = MyClient(intents=intents)
client.run(token)