import os
from dotenv import load_dotenv
import discord
import aiohttp
from discord import Intents, app_commands
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
intents.webhooks = True         # Required for sending webhooks

# Sets up the bot client (connection with Discord)
client = commands.Bot(command_prefix="!", intents=intents)
guild_id = 1275409524643205212  # Aether Music server
owner_id = 767363924734509059  # Aetherius' ID
guild = None
spamping_webhook_url = "https://discord.com/api/webhooks/1346566625591033886/oApOk5EeMufdPcExHaYslNSx6MxCJWhUR_JvS_P-XjCGG1sDc2fLg5-2mzADLLyQSMoZ"



# When the bot has connected to Discord
@client.event
async def on_ready():
    guild = client.get_guild(guild_id)
    channel_id = 1346126004229247010  # Bot commands
    channel = client.get_channel(channel_id)
    await channel.send("I'm online! 🤓")
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
    try:
        await client.tree.sync()
        print(f"Syncing /slash commands to {guild.name}...")
        for command in client.tree.get_commands():
            print(f"Registered command: {command.name}")
    except Exception as e:
            print(f"Failed to sync commands: {e}")



# Regular command to get ping
@client.command(name="ping")
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

    if interaction.user.id != owner_id:
        await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
        return

    await interaction.response.send_message("Shutting down...")
    print("Slash `shutdown` command successfully executed. Closing client...")
    await client.close()



# Slash command to spamping
@client.tree.command(name="spamping", description="Destroy a user's soul")
@app_commands.describe(
    times="Number of times to ping",
    user="The user to ping",
    role="The role to mention",
    text="Custom message to include"
)
async def slash_spamping(interaction: discord.Interaction, times: int, user: discord.User = None, role: discord.Role = None, text: str = "You've been spammed!"):
    try:
        if interaction.user.id != owner_id:
            await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
            return

        if times > 100:  # Prevent excessive spamming
            await interaction.response.send_message("You can't spam ping more than 100 times!", ephemeral=True)
            return

        if user is None:
            await interaction.response.send_message("You must specify a user to ping!", ephemeral=True)
            return

        role_mention = role.mention if role else ""
        message = f"{user.mention} {role_mention} {text}"  # Custom message

        await interaction.response.defer()  # Defer the response to give more time

        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(spamping_webhook_url, session=session)
            
            for _ in range(times):
                await webhook.send(message, username="Deleterius & Co. Spamping™", avatar_url= None)

        await interaction.followup.send(f"Successfully pinged {user.mention} {role_mention} {times} times!")
        print("Slash `spamping` command successfully executed.")
    except Exception as e:
        print(f"An error occurred in the `spamping` command: {e}")
        await interaction.followup.send("An error occurred while executing the command.", ephemeral=True)



# On disconnect
@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected from Discord!")

# On shut down
@client.event
async def on_close():
    channel_id = 1346125122020446278  # General chat
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