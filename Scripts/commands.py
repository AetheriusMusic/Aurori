import random
import discord
import aiohttp
from discord import Intents, app_commands
from discord.ext import commands, tasks

from data import *





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



# Regular !ping command
@client.command(name="ping")
async def regular_ping(ctx):
    latency = round(ctx.bot.latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f"Pong! 🏓 Latency: {latency}ms")
    print(f"Regular `!ping` command successfully executed by {ctx.author.name}")

# Slash /ping command
@client.tree.command(name="ping", description="Check the bot's latency")
async def slash_ping(interaction: discord.Interaction):
    latency = round(interaction.client.latency * 1000)  # Convert latency to milliseconds
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
    print(f"Regular `!love` command successfully executed by {ctx.author.name}")

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



# Regular !coinflip command
@client.command(name="coinflip")
async def regular_coinflip(ctx):

    random_output = ("heads", "tails")

    await ctx.send(f"You got {random.choice(random_output)}!")
    print(f"Regular `!coinflip` command successfully executed by {ctx.author.name}")



# Slash /coinflip command
@client.tree.command(name="coinflip", description="Flip a coin")
async def slash_coinflip(interaction: discord.Interaction):

    random_output = ("heads", "tails")

    await interaction.response.send_message(f"You got {random.choice(random_output)}!")
    print(f"Slash `/coinflip` command successfully executed by {interaction.user.name}")



# Regular !avatar command
@client.command(name="avatar")
async def regular_avatar(ctx, user: discord.User = None):

    user = user or ctx.author
    avatar_url = user.avatar.url

    color = "#9954DD"
    color = discord.Color(int(color.lstrip('#'), 16))

    embed = discord.Embed(title=f"{user.name}'s avatar", color=color)
    embed.set_image(url=avatar_url)

    await ctx.send(embed=embed)
    print(f"Regular `!avatar` command successfully executed by {ctx.author.name}")



# Slash /avatar command
@client.tree.command(name="avatar", description="Get a user's avatar")
@app_commands.describe(user="The user to get the avatar of")
async def slash_avatar(interaction: discord.Interaction, user: discord.User = None):

    user = user or interaction.user
    avatar_url = user.avatar.url

    color = "#9954DD"
    color = discord.Color(int(color.lstrip('#'), 16))

    embed = discord.Embed(title=f"{user.name}'s avatar", color=color)
    embed.set_image(url=avatar_url)

    await interaction.response.send_message(embed=embed)
    print(f"Slash `/avatar` command successfully executed by {interaction.user.name}")



# Regular !spamping command
@client.command(name="spamping")
@commands.is_owner()  # Restrict this command to the bot owner
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
        
        if times < 1:
            await ctx.send("Insert a value bigger than 1!")
        if not ping_provided:
            await ctx.send("Provide a user or a role to ping!")
        if times > 100:
            times = 100
            await ctx.send("You can't spam ping more than 100 times! (Limit set to 100)")

    except Exception as error:
        print(f"An error occurred in the `!spamping` command: {error}")
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

        if interaction.user.id != owner_id:
            await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
            return

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

            # Spamping using a webhook
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(spamping_webhook_url, session=session)
                
                for _ in range(times):
                    await webhook.send(message, username="Deleterius & Co. Spamping™", avatar_url=None)

                await interaction.followup.send(f"Successfully pinged {ping_provided} {times} times!", ephemeral=True)
                print(f"Slash `/spamping` command successfully executed by {interaction.user.name}")

        if times < 1:
            await interaction.followup.send("Insert a value bigger than 1!", ephemeral=True)
        if not ping_provided:
            await interaction.followup.send("Provide a user or a role to ping!", ephemeral=True)
        if times > 100:
            times = 100
            await interaction.followup.send("You can't spam ping more than 100 times! (Limit set to 100)", ephemeral=True)

    except Exception as error:
        print(f"An error occurred in the `/spamping` command: {error}")
        await interaction.response.send_message(f"An error occurred while executing the command.\nError: **{error}**", ephemeral=True)





# Slash /embed command
@client.tree.command(name="embed", description="Send an embed")
@app_commands.describe(
    channel = "The channel to send the embed in",
    title = "The title of the embed (default: Title)",
    description = "The description of the embed (default: Description)",
    color = "The hexadecimal value of the color of the embed (default: #9954DD)",
    field_1_title = "The title of the first field",
    field_1_description = "The description of the first field",
    field_1_is_inline = "Whether the first field is inline or not (default: False)",
    field_2_title = "The title of the second field",
    field_2_description="The description of the second field",
    field_2_is_inline = "Whether the second field is inline or not (default: False)",
    field_3_title = "The title of the third field",
    field_3_description = "The description of the third field",
    field_3_is_inline = "Whether the third field is inline or not (default: False)",
    footer = "The footer text"
)
async def slash_embed(interaction: discord.Interaction,
                      channel: discord.TextChannel,
                      title: str = "Title",
                      description: str = "Description",
                      color: str = "#9954DD",
                      field_1_title: str = None,
                      field_1_description: str = None,
                      field_1_is_inline: bool = False,
                      field_2_title: str = None,
                      field_2_description: str = None,
                      field_2_is_inline: bool = False,
                      field_3_title: str = None,
                      field_3_description: str = None,
                      field_3_is_inline: bool = False,
                      footer: str = None
                      ):
    try:

        if interaction.user.id != owner_id:
            await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
            return

        # Convert hex color to discord.Color
        color = discord.Color(int(color.lstrip('#'), 16))

        embed = discord.Embed(title=title, description=description, color=color)
        if field_1_title and field_1_description:
            embed.add_field(name=field_1_title, value=field_1_description, inline=field_1_is_inline)
            if field_2_title and field_2_description:
                embed.add_field(name=field_2_title, value=field_2_description, inline=field_2_is_inline)
                if field_3_title and field_3_description:
                    embed.add_field(name=field_3_title, value=field_3_description, inline=field_3_is_inline)
        if footer:
            embed.set_footer(text=footer, icon_url=interaction.guild.icon.url)

        await channel.send(embed=embed)
        await interaction.response.send_message("Embed sent successfully!", ephemeral=True)

    except Exception as error:
        print(f"An error occurred in the `/embed` command: {error}")
        await interaction.response.send_message(f"An error occurred while executing the command.\nError: **{error}**", ephemeral=True)