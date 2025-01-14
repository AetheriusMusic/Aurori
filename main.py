import os
from dotenv import load_dotenv
import discord
from discord import Intents
from discord.ext import commands, tasks

# Loads token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Sets up Discord intents (permissions for the bot)
intents = Intents.default()
intents.message_content = True  # For reading message content
intents.guilds = True           # For detecting guilds (servers)
intents.presences = True        # Enable presence intent
intents.members = True          # Required for fetching members

# Sets up the bot client (connection with Discord)
client = commands.Bot(command_prefix="!", intents=intents)
guild_id = 1275409524643205212  # Aether server



# When the bot has connected to Discord
@client.event
async def on_ready():
    channel_id = 1328140497364975656  # Testing channel
    channel = client.get_channel(channel_id)
    await channel.send("I'm online!")
    print(f"{client.user} is connected to Discord!")

    guild = client.get_guild(guild_id)
    if not guild:
        print(f"Could not find guild with ID {guild_id}.")
        return

    # Initialize user avatars for all members in the guild
    for member in guild.members:
        user_avatars[member.id] = member.avatar

    # Start the avatar-checking task
    check_avatars.start(guild)

    # Syncs /commands
    if guild:
        await client.tree.sync(guild=guild)
        print(f"Synced /slash commands to {guild.name} succesfully!")
#   for command in client.tree.get_commands():
#       print(f"Registered command: {command.name}.")



# Regular command to get ping
@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f"Pong! 🏓 Latency: {latency}ms")
    print("`!ping` command succesfully executed.")

# Slash command to get ping
@client.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    latency = round(client.latency * 1000)  # Convert latency to milliseconds
    await interaction.response.send_message(f"Pong! 🏓 Latency: {latency}ms")
    print("`/ping` command succesfully executed.")



# Regular command to shutdown
@client.command(name="shutdown")
@commands.is_owner()  # Restrict this command to the bot owner
async def regular_shutdown(ctx):
    await ctx.send("Shutting down...")
    print("Regular `shutdown` command successfully executed. Closing client...")
    await client.close()

# Slash command to shutdown
@client.tree.command(name="shutdown", description="Shut down the bot")
async def slash_shutdown(interaction: discord.Interaction):
    await interaction.response.send_message("Shutting down...")
    print("Slash `shutdown` command successfully executed. Closing client...")
    await client.close()



# On disconnect
@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected from Discord!")

# On shut down
@client.event
async def on_close():
    channel_id = 1323038721234440326  # Chilling
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send("I'm gonna sleep!")



# Avatar update
user_avatars = {}



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



# Function to start the bot
def bot_startup():
    client.run(TOKEN)

bot_startup()