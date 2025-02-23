import discord
from dotenv import load_dotenv
import os

from gemini import gemini_api

# Load environment variables from a .env file
load_dotenv()

# Define a custom client class inheriting from discord.Client
class Client(discord.Client):
    # Event handler for when the bot is ready
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    # Event handler for when a message is received
    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            print("Ignoring message from self")
            return

        print(f"Received message: {message.content} from {message.author}")
        response_text = gemini_api(message.content)
        
        await message.channel.send(response_text)
        print(f"Sent response: {response_text}")

    # Event handler for when a reaction is added to a message
    async def on_reaction_add(self, reaction, user):
        # Ignore reactions added by the bot itself
        if user == self.user:
            print("Ignoring reaction from self")
            return
        
        await reaction.message.channel.send('You reacting eh?!')
        print(f"Reacted to message: {reaction.message.content}")

# Define the intents required by the bot
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.reactions = True  # Required to handle reactions

# Create an instance of the custom client with the specified intents
bot = Client(intents=intents)

# Run the bot using the token from the environment variables
bot.run(os.getenv('BOT_TOKEN'))