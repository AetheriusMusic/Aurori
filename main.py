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
    if channel:
        await channel.send("I'm online!")
    print(f"{client.user} is now running!")

    # Sync slash commands for a specific guild
    guild_id = 1275409524643205212 # Aether
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild:
        await client.tree.sync(guild=guild)
    print(f"Synced /slash commands to {guild.name} succesfully!")



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

# Function to start the bot
def bot_startup():
    client.run(TOKEN)

bot_startup()