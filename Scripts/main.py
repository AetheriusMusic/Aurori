import random
import os
from dotenv import load_dotenv
import discord
import aiohttp
from discord import Intents, app_commands, embeds
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

    # Initialize user avatars for all members in the guild
    for member in guild.members:
        user_avatars[member.id] = member.avatar

    # Start the avatar-checking task
    check_avatars.start(guild)

    # Syncs /slash commands
    try:
        await client.tree.sync()
        print(f"Syncing /slash commands to {guild.name}...")
        for command in client.tree.get_commands():
            print(f"Registered command: {command.name}")
    except Exception as error:
            print(f"Failed to sync commands: {error}")





# Regular !ping command
@client.command(name="ping")
async def regular_ping(ctx):
    latency = round(client.latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f"Pong! 🏓 Latency: {latency}ms")
    print(f"Regular `!ping` command successfully executed by {ctx.author.name}")

# Slash /ping command
@client.tree.command(name="ping", description="Check the bot's latency")
async def slash_ping(interaction: discord.Interaction):
    latency = round(client.latency * 1000)  # Convert latency to milliseconds
    await interaction.response.send_message(f"Pong! 🏓 Latency: {latency}ms")
    print(f"Slash `/ping` command successfully executed by {interaction.user.name}")



# Regular !shutdown command
@client.command(name="shutdown")
@commands.is_owner()  # Restrict this command to the bot owner
async def regular_shutdown(ctx):
    await ctx.send("Shutting down...")
    print(f"Regular `!shutdown` command successfully executed by {ctx.author.name}")
    await client.close()
    print("Client closed successfully")

# Slash /shutdown command
@client.tree.command(name="shutdown", description="Shut down the bot")
async def slash_shutdown(interaction: discord.Interaction):

    if interaction.user.id != owner_id:
        await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
        return

    await interaction.response.send_message("Shutting down...")
    print(f"Slash `/shutdown` command successfully executed by {interaction.user.name}")
    await client.close()
    print("Client closed successfully")





# Regular !spamping command
@client.command(name="spamping")
async def regular_spamping(ctx, times: int, user: discord.User = None, role: discord.Role = None, text: str = "Hello :3"):
    try:

        if times > 100:  # Prevent excessive spamming
            times = 100
            await ctx.send("You can't spam ping more than 100 times! (Limiting to 100...)")

        user_mention = user.mention if user else ""
        role_mention = role.mention if role else ""

        if user_mention and role_mention:
            ping_provided = f"{user_mention} and {role_mention}"
        elif user_mention and not role_mention:
            ping_provided = user_mention
        elif role_mention and not user_mention:
            ping_provided = role_mention
        else:
            ping_provided = False

        message = f"{ping_provided} {text}"  # Custom message

        await ctx.defer()  # Defer the response to give more time

        if times > 1 and ping_provided:  # Check if user or role is provided

            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(spamping_webhook_url, session=session)
                
                for _ in range(times):
                    await webhook.send(message, username="Deleterius & Co. Spamping™", avatar_url=None)

            await ctx.send(f"Successfully pinged {ping_provided} {times} times!")
            print(f"Regular `!spamping` command successfully executed by {ctx.author.name}")
        elif times < 2 and ping_provided:
            await ctx.send("Please insert a value bigger than 1!")
        elif times < 2 and not ping_provided:
            await ctx.send("Please provide a user or a role to ping and insert a value bigger than 1!")
        elif times > 1 and not ping_provided:
            await ctx.send("Please provide a user or a role to ping!")
        elif times > 100:
            times = 100
            await ctx.send("You can't spam ping more than 100 times! (Limiting to 100...)", ephemeral=True)

    except Exception as error:
        print(f"An error occurred in the `/spamping` command: {error}")
        await ctx.send(f"An error occurred while executing the command.\nError: **{error}**")



# Slash /spamping command
@client.tree.command(name="spamping", description="Destroy a user's soul")
@app_commands.describe(
    times="Number of times to ping",
    user="The user to ping",
    role="The role to ping",
    text="Custom message to include (default: \"Hello :3\")"
)
async def slash_spamping(interaction: discord.Interaction, times: int, user: discord.User = None, role: discord.Role = None, text: str = "Hello :3"):
    try:

        user_mention = user.mention if user else ""
        role_mention = role.mention if role else ""

        if user_mention and role_mention:
            ping_provided = f"{user_mention} and {role_mention}"
        elif user_mention and not role_mention:
            ping_provided = user_mention
        elif role_mention and not user_mention:
            ping_provided = role_mention
        else:
            ping_provided = False

        message = f"{ping_provided} {text}"  # Custom message

        await interaction.response.defer()  # Defer the response to give more time

        if times > 1 and ping_provided:  # Check if user or role is provided

            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(spamping_webhook_url, session=session)
                
                for _ in range(times):
                    await webhook.send(message, username="Deleterius & Co. Spamping™", avatar_url=None)

            await interaction.followup(f"Successfully pinged {ping_provided} {times} times!", ephemeral=True)
            print(f"Slash `/spamping` command successfully executed by {interaction.user.name}")
        elif times < 2 and ping_provided.send:
            await interaction.followup.send("Please insert a value bigger than 1!", ephemeral=True)
        elif times < 2 and not ping_provided:
            await interaction.followup.send("Please provide a user or a role to ping and insert a value bigger than 1!", ephemeral=True)
        elif times > 1 and not ping_provided:
            await interaction.followup.send("Please provide a user or a role to ping!", ephemeral=True)
        elif times > 100:
            times = 100
            await interaction.followup.send("You can't spam ping more than 100 times! (Limiting to 100...)", ephemeral=True)

    except Exception as error:
        print(f"An error occurred in the `/spamping` command: {error}")
        await interaction.followup.send(f"An error occurred while executing the command.\nError: **{error}**", ephemeral=True)



# Regular !love command
@client.command(name="love")
async def regular_love(ctx):

    random_message = ("I love you",
                      "I love you more than anything",
                      "I love you more than words can describe",
                      "I love you more than you can imagine",
                      "I love you more than you will ever know",
                      "You're goddamn fine")

    random_emoji = ("❤️", "💖", "💕", "💞", "💗", "💓", "💝", "💘", "💟", "💜", "💛", "💚", "💙", "🧡", "❣️")

    await ctx.send(f"{random.choice(random_message)}, {ctx.author.mention}! {random.choice(random_emoji)}")
    print(f"Regular `!ping` command successfully executed by {ctx.author.name}")

# Slash /love command
@client.tree.command(name="love", description="Let the bot show you some love")
async def slash_love(interaction: discord.Interaction):

    random_message = ("I love you",
                      "I love you more than anything",
                      "I love you more than words can describe",
                      "I love you more than you can imagine",
                      "I love you more than you will ever know",
                      "You're goddamn fine")

    random_emoji = ("❤️", "💖", "💕", "💞", "💗", "💓", "💝", "💘", "💟", "💜", "💛", "💚", "💙", "🧡", "❣️")

    await interaction.response.send_message(f"{random.choice(random_message)}, {interaction.user.mention}! {random.choice(random_emoji)}")
    print(f"Slash `/love` command successfully executed by {interaction.user.name}")



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



# Function to start the bot
def bot_startup():
    client.run(TOKEN)

bot_startup()