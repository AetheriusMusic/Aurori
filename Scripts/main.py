import random
import os
import discord
import aiohttp
from discord import Intents, app_commands
from discord.ext import commands, tasks
from Commands import regular_ping, slash_ping, regular_shutdown, slash_shutdown, regular_love, slash_love, regular_coinflip, slash_coinflip, regular_avatar, slash_avatar, regular_spamping, slash_spamping, slash_embed

# TODO: Do not hardcode.
TOKEN = "MTMyODExNTIzOTk5NjM1ODY1Ng.GJQarU.eSqeqUZwOB6LRMiSNlBlOWMN7F3ujFt1aJN7Tg"

# Sets up Discord intents (permissions for the bot)
intents = Intents.default()
intents.message_content = True  # For reading message content
intents.guilds = True           # For detecting guilds (servers)
intents.presences = True        # Enable presence intent
intents.members = True          # Required for fetching members
intents.webhooks = True         # Required for sending webhooks

# Sets up the bot client (connection with Discord)
client = commands.Bot(command_prefix="!", intents=intents)
guild_id = 1275409524643205212  # Aether Music server
owner_id = 767363924734509059   # Aetherius' ID
guild = None
spamping_webhook_url = "https://discord.com/api/webhooks/1346566625591033886/oApOk5EeMufdPcExHaYslNSx6MxCJWhUR_JvS_P-XjCGG1sDc2fLg5-2mzADLLyQSMoZ"



# When the bot has connected to Discord
@client.event
async def on_ready():
    guild = client.get_guild(guild_id)
    channel_id = 1328140497364975656  # Testing channel
    channel = client.get_channel(channel_id)
    await channel.send("I'm online! 🤓")
    print(f"{client.user} is connected to Discord!")

    guild = client.get_guild(guild_id)
    if not guild:
        print(f"Could not find guild with ID {guild_id}.")
        return

    # Initialize user avatars and nicknames for all members in the guild
    for member in guild.members:
        user_avatars[member.id] = member.avatar
        user_nicknames[member.id] = member.nick

    # Start the avatars and nicknames checking tasks
    check_avatars.start(guild)
    check_nicknamens.start(guild)

    # Add regular commands
    client.add_command(regular_ping)
    client.add_command(regular_shutdown)
    client.add_command(regular_love)
    client.add_command(regular_coinflip)
    client.add_command(regular_avatar)
    client.add_command(regular_spamping)

    # Add slash commands
    client.tree.add_command(slash_ping)
    client.tree.add_command(slash_shutdown)
    client.tree.add_command(slash_love)
    client.tree.add_command(slash_coinflip)
    client.tree.add_command(slash_avatar)
    client.tree.add_command(slash_spamping)
    client.tree.add_command(slash_embed)

    # Syncs /slash commands
    try:
        await client.tree.sync()
        print(f"Syncing /slash commands to {guild.name}...")
        for command in client.tree.get_commands():
            print(f"Registered /slash command: /{command.name}")
    except Exception as error:
            print(f"Failed to sync /slash commands: {error}")



# On message
@client.event
async def on_message(message):
    if message.channel.id == 1359200351282008236:
        thread = await message.channel.create_thread(name=f"{message.author.name}' idea",message=message)
        await thread.send(f"Thank you {message.author.mention}! If you want to discuss anything, say it here, and don't forget to publish the message you sent!")
        print(f"SCP: PyLab thread created by {message.author.name}")




# On disconnect
@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected from Discord!")



# Avatar update
user_avatars = {}  # Store user avatars

@tasks.loop(seconds=10)  # Adjust the interval as needed
async def check_avatars(guild):

    channel_id = 1292539484201685012 # User logs channel
    channel = client.get_channel(channel_id)

    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_avatars:
            if member.avatar != user_avatars[member.id]:  # Compare stored avatar with current avatar
                await channel.send(f"{member.name} changed their avatar!")
                await channel.send(f"Old avatar: {user_avatars[member.id]}")
                await channel.send(f"New avatar: {member.avatar}")
                print(f"{member.name} changed their avatar!")
                print(f"Old avatar: {user_avatars[member.id]}")
                print(f"New avatar: {member.avatar}")

                # Update the stored avatar
                user_avatars[member.id] = member.avatar
        else:
            # Store the avatar if it's not already stored
            user_avatars[member.id] = member.avatar



user_nicknames = {}  # Store user nicknames

@tasks.loop(seconds=10)  # Adjust the interval as needed
async def check_nicknamens(guild):

    channel_id = 1292539484201685012 # User logs channel
    channel = client.get_channel(channel_id)

    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_nicknames:
            if  member.nick != user_nicknames[member.id]:  # Compare stored nickname with current nickname
                await channel.send(f"{member.name} changed their nickname!")
                await channel.send(f"Old nickname: {user_nicknames[member.id]}")
                await channel.send(f"New nickname: {member.nick}")
                print(f"{member.name} changed their nickname!")
                print(f"Old nickname: {user_nicknames[member.id]}")
                print(f"New nickname: {member.nick}")

                # Update the stored avatar
                user_nicknames[member.id] = member.nick
        else:
            # Store the avatar if it's not already stored
            user_nicknames[member.id] = member.nick



# Function to start the bot
def bot_startup():
    client.run(TOKEN)

bot_startup()