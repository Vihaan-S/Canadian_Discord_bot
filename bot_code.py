import discord
from dotenv import load_dotenv
import os

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
            return
        
        # Check if the message ends with a period
        if message.content.endswith('.'):
            # Remove the period and add 'eh.' instead
            modified_message = message.content[:-1] + ' eh.'
            await message.channel.send(modified_message)
        
        # Check if the message contains "eh" (case insensitive)
        if 'eh' in message.content.lower():
            # React with "🇪" and "🇭" emojis
            await message.add_reaction('🇪')
            await message.add_reaction('🇭')

    # Event handler for when a reaction is added to a message
    async def on_reaction_add(self, reaction, user):
        # Ignore reactions added by the bot itself
        if user == self.user:
            return
        
        await reaction.message.channel.send('You reacting eh?!')

# Define the intents required by the bot
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.reactions = True  # Required to handle reactions

# Create an instance of the custom client with the specified intents
bot = Client(intents=intents)
# hi
# Run the bot using the token from the environment variables
bot.run(os.getenv('BOT_TOKEN'))
