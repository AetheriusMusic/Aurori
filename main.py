import os
from dotenv import load_dotenv
import discord
from discord import Intents, app_commands
from discord.ext import commands

# Loads token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Sets up Discord intents (permissions for the bot)
intents = Intents.default()
intents.message_content = True  # For reading message content
intents.guilds = True  # For detecting guilds (servers)

# Sets up the bot client (connection with Discord)
client = commands.Bot(command_prefix="!", intents=intents)



# When the bot has connected to Discord
@client.event
async def on_ready():
    channel_id = 1323038721234440326  # Chilling
    channel = client.get_channel(channel_id)
    await client.tree.sync()
    print("Slash comands ready!")
    for command in client.tree.get_commands():
        print(f"Registered command: {command.name}.")



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




# Sync slash commands for a specific guild
async def sync_commands():
    guild_id = 1275409524643205212 # Aether
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild:
        await client.tree.sync(guild=guild)
        print(f"Synced /slash commands to {guild.name} succesfully!")

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



# Function to start the bot
def bot_startup():
    client.run(TOKEN)

bot_startup()