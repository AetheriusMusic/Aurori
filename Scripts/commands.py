from pathlib import Path

import random
import json

import discord
import aiohttp
from discord import app_commands

from data import *
from utility import *





VERIFICATION_LIST_PATH = Path(__file__).resolve().parent.parent / "Data/verification_list.json"

BUMP_LEADERBOARD_PATH = Path(__file__).resolve().parent.parent / "Data/bump_leaderboard.json"





# Regular !info command
@client.command(name="info")
async def regular_info(ctx):

    embed_aurori_info = make_embed(
                channel=ctx.channel,
                color=AURORI_COLOR,
                title="Aurori",
                description="I am Aurori, a fun bot developed for many purposes, varying from silly commands to moderation ones! <:scugSilly:1406051577365794816>",
                field_1_title="Bot Developer:",
                field_1_is_inline=True,
                field_1_description="Aetherius",
                field_2_title="Developed using:",
                field_2_is_inline=True,
                field_2_description="Python, thanks to discord.py"
                )
    await ctx.send(embed=embed_aurori_info)
    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name}, embed sent in {ctx.channel.name}")

# Slash /info command
@client.tree.command(name="info", description="Check the bot's info")
async def slash_info(interaction: discord.Interaction):

    embed_aurori_info = make_embed(
                channel=interaction.channel,
                color=AURORI_COLOR,
                title="Aurori",
                description="I am Aurori, a fun bot developed for many purposes, varying from silly commands to moderation ones!",
                field_1_title="Bot Developer:",
                field_1_is_inline=True,
                field_1_description="Aetherius",
                field_2_title="Developed using:",
                field_2_is_inline=True,
                field_2_description="Python, thanks to discord.py"
                )
    await interaction.response.send_message(embed=embed_aurori_info)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, embed sent in {interaction.channel.name}")



# Regular !ping command
@client.command(name="ping")
async def regular_ping(ctx):

    latency = round(ctx.bot.latency * 1000)

    await ctx.send(f"Pong! <:cat_milk:1353405311326621706>\nLatency: **{latency}** ms")
    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name} in {ctx.channel.name}")

# Slash /ping command
@client.tree.command(name="ping", description="Check the bot's latency")
async def slash_ping(interaction: discord.Interaction):

    latency = round(interaction.client.latency * 1000)

    await interaction.response.send_message(f"Pong! <:cat_milk:1353405311326621706>\nLatency: **{latency}** ms")
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name} in {interaction.channel.name}")



# Regular !love command
@client.command(name="love")
async def regular_love(ctx):

    random_message = ("I love you",
                      "I love you more than anything",
                      "I love you more than words can describe",
                      "I love you more than you can imagine",
                      "I love you more than you will ever know",
                      "Remember, there's always somebody that loves you"
                      )
    random_emoji = ("❤️", "💖", "💕", "💞", "💗", "💓", "💝", "💘", "💟", "💜", "💛", "💚", "💙", "🧡", "❣️")

    await ctx.send(f"{random.choice(random_message)}, {ctx.author.mention}! {random.choice(random_emoji)}")
    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name} in {ctx.channel.name}")

# Slash /love command
@client.tree.command(name="love", description="Let the bot show you some love")
async def slash_love(interaction: discord.Interaction):

    random_message = ("I love you",
                      "I love you more than anything",
                      "I love you more than words can describe",
                      "I love you more than you can imagine",
                      "I love you more than you will ever know",
                      "Remember, there's always somebody that loves you"
                      )
    random_emoji = ("❤️", "💖", "💕", "💞", "💗", "💓", "💝", "💘", "💟", "💜", "💛", "💚", "💙", "🧡", "❣️")

    await interaction.response.send_message(f"{random.choice(random_message)}, {interaction.user.mention}! {random.choice(random_emoji)}")
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name} in {interaction.channel.name}")



# Regular !coinflip command
@client.command(name="coinflip")
async def regular_coinflip(ctx):

    random_output = ("heads", "tails")

    await ctx.send(f"You got {random.choice(random_output)}!")
    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name} in {ctx.channel.name}")

# Slash /coinflip command
@client.tree.command(name="coinflip", description="Flip a coin")
async def slash_coinflip(interaction: discord.Interaction):

    random_output = ("heads", "tails")

    await interaction.response.send_message(f"You got {random.choice(random_output)}!")
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name} in {interaction.channel.name}")



# Regular !avatar command
@client.command(name="avatar")
async def regular_avatar(ctx, user: discord.User = None):

    user = user or ctx.author
    avatar_url = user.display_avatar.url

    embed_avatar = make_embed(title=f"{user.name}'s avatar", channel=ctx.channel, color=AETHER_COLOR)
    embed_avatar.set_image(url=avatar_url)

    await ctx.send(embed=embed_avatar)
    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name}, {user.name}'s avatar sent in {ctx.channel.name}")

# Slash /avatar command
@client.tree.command(name="avatar", description="Get a user's avatar")
@app_commands.describe(user="The user to get the avatar of")
async def slash_avatar(interaction: discord.Interaction, user: discord.User = None):

    user = user or interaction.user
    avatar_url = user.display_avatar.url

    embed_avatar = make_embed(title=f"{user.name}'s avatar", channel=interaction.channel, color=AETHER_COLOR)
    embed_avatar.set_image(url=avatar_url)

    await interaction.response.send_message(embed=embed_avatar)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, {user.name}'s avatar sent in {interaction.channel.name}")



# Regular !shutdown command
@client.command(name="shutdown")
async def regular_shutdown(ctx):
    if ctx.author.id != AETHERIUS_ID:
        await ctx.send(NO_PERMISSION_MESSAGE)
        return

    await ctx.send("<:catPonder:1379876581153177771> Shutting down...")
    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name}")
    await client.close()
    print("Client closed successfully")

# Slash /shutdown command
@client.tree.command(name="shutdown", description="Shut down the bot")
async def slash_shutdown(interaction: discord.Interaction):

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    await interaction.response.send_message("<:catPonder:1379876581153177771> Shutting down...")
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}")
    await client.close()
    print("Client closed successfully")





# Slash /spamping command
@client.tree.command(name="spamping", description="Destroy a user's soul")
@app_commands.describe(
    times="Number of times to ping",
    user="The user to ping",
    role="The role to ping",
    text="Custom message to include (default: \"Hello :3\")",
    webhook_index="The channel to send the spamping in (1: Bot Commands, 0: Silksong)"
    )
async def slash_spamping(interaction: discord.Interaction,
                         times: int,
                         user: discord.User = None,
                         role: discord.Role = None,
                         text: str = "Hello :3",
                         webhook_index: int = None
                         ):

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    if times < 1:
        await interaction.followup.send("Insert a value bigger than 1!", ephemeral=True)
    if not ping_provided:
        await interaction.followup.send("Provide a user or a role to ping!", ephemeral=True)
    if times > 100:
        times = 100
        await interaction.followup.send("You can't spam ping more than 100 times! (Limit set to 100)", ephemeral=True)

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

    message = f"{ping_provided} {text}"

    await interaction.response.defer(ephemeral=True)

    if times > 1 and ping_provided:


        match webhook_index:
            case 0: webhook_index = spamping_silksong_url
            case 1: webhook_index = spamping_bot_commands_url
            case None:
                await interaction.followup.send("Invalid channel selection! Defaulting to Silksong channel.", ephemeral=True)
                webhook_index = spamping_silksong_url
            case _:
                await interaction.followup.send("Invalid channel selection! Defaulting to Silksong channel.", ephemeral=True)
                webhook_index = spamping_silksong_url

        # Spamping using a webhook
        async with aiohttp.ClientSession() as session:
            spamping_webhook = discord.Webhook.from_url(webhook_index, session=session)
                
            for _ in range(times):
                await spamping_webhook.send(message, username="Deleterius & Co. Spamping™", avatar_url=None)

            await interaction.followup.send(f"✅ Successfully pinged {ping_provided} {times} times!", ephemeral=True)
            print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}")





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
                      color: str = AURORI_COLOR,
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

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    elif interaction.user.id == AETHERIUS_ID:

        embed = make_embed(
                        channel,
                        title,
                        description,
                        color,
                        field_1_title,
                        field_1_description,
                        field_1_is_inline,
                        field_2_title,
                        field_2_description,
                        field_2_is_inline,
                        field_3_title,
                        field_3_description,
                        field_3_is_inline,
                        footer
                        )

        await channel.send(embed=embed)
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f"✅ Embed sent succesfully in {channel.mention}!", ephemeral=True)
        print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, embed sent in {channel.name}")





# Slash /ticketsetup command
@client.tree.command(name="ticketsetup", description="Sets up the ticket system for the current channel")
async def slash_ticket_setup(interaction: discord.Interaction):

    from tickets import SupportTicketView

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    embed_ticket_setup = make_embed(
            channel=interaction.channel,
            title="Support ticket",
            description="Open a ticket to request support to the server Staff!",
            color=SUPPORT_TICKET_COLOR
            )

    await interaction.channel.send(embed=embed_ticket_setup, view=SupportTicketView())

    await interaction.response.send_message("✅ Ticket system set up in the current channel!", ephemeral=True)

    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, ticket system set up in {interaction.channel.name}")



# Slash /addmember command
@client.tree.command(name="addmember", description="Add a member to the ticket")
@app_commands.describe(user="The user to add to the ticket")
async def slash_add_member(interaction: discord.Interaction, user: discord.Member):

    if not interaction.channel.name.startswith(("ticket-")):
        await interaction.response.send_message("⚠️ This command can only be used in ticket channels!", ephemeral=True)
        return

    guild = interaction.guild
    staff_role = guild.get_role(STAFF_ROLE_ID)

    if staff_role not in interaction.user.roles:
        await interaction.response.send_message("❌ Only Staff can add members to the ticket!", ephemeral=True)
        return

    await interaction.channel.set_permissions(user, view_channel=True, send_messages=True, read_message_history=True)

    await interaction.response.send_message(f"✅ {user.mention} has been added to the ticket!", ephemeral=True)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, {user.name} added to {interaction.channel.name}")



# Slash /selfrolessetup command
@client.tree.command(name="selfrolessetup", description="Sets up the self roles for the current channel")
async def slash_self_roles_setup(interaction: discord.Interaction):

    from self_roles import SelfRolesMiscView
    from self_roles import SelfRolesPingView

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    embed_misc = make_embed(
            channel=interaction.channel,
            title="MISC ROLES",
            description="Are you looking for a way to customize your experience in the server?\nClick on the buttons below to get your roles!\nTo remove them simply click the button again!",
            field_1_title="Avalaible roles:",
            field_1_description="🎵 Musician\n🎨 Artist\n🎮 Gamer\n 💻Coder\n📸 Photographer\n✍️ Writer\n📚 Lore Hunter",            
            color="#3EBAE6"
            )

    embed_ping = make_embed(
            channel=interaction.channel,
            title="PING ROLES",
            description="Wanna receive pings for specific situations?\nClick the buttons to receive them!\nTo remove them simply click the button again!",
            field_1_title="Avalaible roles:",
            field_1_description="🎶 Release Ping\n📊 Poll Ping\n🕹️ Gaming Ping",
            color="#8E70F2"
            )

    await interaction.channel.send(embed=embed_misc, view=SelfRolesMiscView())
    await interaction.channel.send(embed=embed_ping, view=SelfRolesPingView())

    await interaction.response.send_message("✅ Self roles buttons set up in the current channel!", ephemeral=True)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name} in {interaction.channel.name}")





# Slash /staffapplicationsetup command
@client.tree.command(name="staffapplicationsetup", description="Sets up the Staff application form for the current channel")
async def slash_staff_application_setup(interaction: discord.Interaction):

    from staff_application import StaffApplicationFormView

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    embed_staff = make_embed(
            channel=interaction.channel,
            title="Staff Application Form",
            description="Click the button to open the from and apply to become part of the Staff!",          
            color=AURORI_COLOR
            )

    await interaction.channel.send(embed=embed_staff, view=StaffApplicationFormView())

    await interaction.response.send_message("✅ Staff application form set up in the current channel!", ephemeral=True)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name} in {interaction.channel.name}")





# Slash /say command
@client.tree.command(name="say", description="Make the bot say something")
@app_commands.describe(message = "The message to make the bot say")
async def slash_say(interaction: discord.Interaction, message: str):

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    await interaction.channel.send(message)
    await interaction.response.send_message("✅ Message sent!", ephemeral=True)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}")





# Slash /givememberrole command
@client.tree.command(name="givememberrole", description="Give the Member role to all verified users")
async def slash_give_member_role(interaction: discord.Interaction):

    if interaction.user.id != AETHERIUS_ID:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    guild = interaction.guild
    member_role = guild.get_role(MEMBER_ROLE_ID)
    verification_role = guild.get_role(VERIFICATION_ROLE_ID)

    member_counter = 0
    for member in guild.members:
        if member_role not in member.roles and verification_role not in member.roles and not member.bot:
            await member.add_roles(member_role)
            print(f"Gave Member role to {member.name}")
            member_counter += 1

    await interaction.response.send_message(f"Gave {member_role.mention} role to {member_counter} users!", ephemeral=True)
    print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, gave Member role to {member_counter} users")





# Slash /verify command
@client.tree.command(name="verify", description="Send a user to the verification channel")
@app_commands.describe(user="The user to verify")
async def slash_verify(interaction: discord.Interaction, user: discord.Member):

    staff_role = interaction.guild.get_role(STAFF_ROLE_ID)
    if staff_role not in interaction.user.roles:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    await interaction.response.defer(ephemeral=False)

    guild = interaction.guild
    bot_member = guild.me
    verification_role = guild.get_role(VERIFICATION_ROLE_ID)
    verification_channel = guild.get_channel(VERIFICATION_CHANNEL_ID)

    roles_to_remove = [role for role in user.roles if role != guild.default_role and not role.managed and role < bot_member.top_role]

    with open(VERIFICATION_LIST_PATH, "r", encoding="utf-8") as verification_file:
        verification_list = json.load(verification_file)

    user_id_string = str(user.id)

    if user_id_string not in verification_list:
        previous_role_ids = [role.id for role in roles_to_remove]

        if bot_member.top_role > user.top_role and not user.bot:
            await user.remove_roles(*roles_to_remove)
            await user.add_roles(verification_role)

            verification_list[user_id_string] = {"Username": user.name,
                                                 "Display name": user.display_name,
                                                 "Role IDs": previous_role_ids,
                                                 "Join date": user.joined_at.strftime("%d/%m/%Y")
                                                 }

            with open(VERIFICATION_LIST_PATH, "w", encoding="utf-8") as verification_list_file:
                json.dump(verification_list, verification_list_file, indent=4)

            await interaction.followup.send(f"🔒 {user.mention} has been sent to the {verification_channel.mention} channel!", ephemeral=False)
            print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, {user.name} has been sent to the verification channel")

        elif bot_member.top_role <= user.top_role:
            await interaction.followup.send(f"❌ {user.mention} cannot be sent to the {verification_channel.mention} channel!", ephemeral=True)
            print(f"Slash /{interaction.command.name} failed to execute by {interaction.user.name}, {user.name} cannot be sent to verification")

        elif user.bot:
            await interaction.followup.send(f"❌ {user.mention} cannot be sent to the {verification_channel.mention} channel!", ephemeral=True)
            print(f"Slash /{interaction.command.name} failed to execute by {interaction.user.name}, {user.name} cannot be sent to verification")

    else:
        saved_role_ids = verification_list.pop(user_id_string)["Role IDs"]
        roles_to_restore = [guild.get_role(rid) for rid in saved_role_ids if guild.get_role(rid)]
        if roles_to_restore:
            await user.add_roles(*roles_to_restore)
        await user.remove_roles(verification_role)

        with open(VERIFICATION_LIST_PATH, "w", encoding="utf-8") as verification_list_file:
            json.dump(verification_list, verification_list_file, indent=4)

        await interaction.followup.send(f"🔓 {user.mention} has been given back their roles!", ephemeral=False)
        print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, {user.name} has been given back their roles")





# Regular !bumpleaderboard command
@client.command(name="bumpleaderboard", aliases=["bumplb"])
async def regular_bumpleaderboard(ctx):

    with open(BUMP_LEADERBOARD_PATH, "r", encoding="utf-8") as bump_leaderboard_file:
        bump_leaderboard = json.load(bump_leaderboard_file)

    users = []
    for user_id, info in bump_leaderboard.items():
        users.append({
            "user_id": user_id,
            "display_name": info.get("Display name", "Unknown"),
            "count": info.get("Bump count", 0)
        })

    users.sort(key=lambda u: u["count"], reverse=True)
    top10 = users[:10]

    description_lines = []
    for index, entry in enumerate(top10, start=1):
        medals = ["🥇", "🥈", "🥉"]
        position = medals[index-1] if index <= len(medals) else f"{index})"
        user_id = entry["user_id"]
        count = entry["count"]
        description_lines.append(f"{position} - <@{user_id}>: **{count}** bumps")

    description = "\n".join(description_lines) if description_lines else "No data <:catPonder:1379876581153177771>"

    embed_bump_leaderboard = make_embed(
                channel=ctx.channel,
                color=AURORI_COLOR,
                title="Bump Leaderboard",
                description=description
                )

    await ctx.send(embed=embed_bump_leaderboard)

    print(f"Regular !{ctx.command.name} {COMMAND_EXECUTED_MESSAGE} {ctx.author.name} in {ctx.channel.name}")



# Slash /bumpleaderboard command
@client.tree.command(name="bumpleaderboard", description="Show the Bump Leaderboard")
async def slash_bumpleaderboard(interaction: discord.Interaction):

    with open(BUMP_LEADERBOARD_PATH, "r", encoding="utf-8") as bump_leaderboard_file:
        bump_leaderboard = json.load(bump_leaderboard_file)

    users = []
    for user_id, info in bump_leaderboard.items():
        users.append({
            "user_id": user_id,
            "display_name": info.get("Display name", "Unknown"),
            "count": info.get("Bump count", 0)
        })

    users.sort(key=lambda u: u["count"], reverse=True)
    top10 = users[:10]

    description_lines = []
    for index, entry in enumerate(top10, start=1):
        medals = ["🥇", "🥈", "🥉"]
        position = medals[index-1] if index <= len(medals) else f"{index})"
        user_id = entry["user_id"]
        count = entry["count"]
        description_lines.append(f"{position} - <@{user_id}>: **{count}** bumps")

    description = "\n".join(description_lines) if description_lines else "No data <:catPonder:1379876581153177771>"

    embed_bump_leaderboard = make_embed(
                channel=interaction.channel,
                color=AURORI_COLOR,
                title="Bump Leaderboard",
                description=description
                )

    await interaction.response.send_message(embed=embed_bump_leaderboard)

    print(f"Regular !{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name} in {interaction.channel.name}")





# Slash /dm command
@client.tree.command(name="dm", description="Send a direct message as an embed to a user")
@app_commands.describe(user = "The user to send the DM to",
                       title = "The title of the embed",
                       message = "The message to include in the embed"
                       )
async def slash_dm(interaction: discord.Interaction, user: discord.User, title: str, message: str):

    staff_role = interaction.guild.get_role(STAFF_ROLE_ID)
    if staff_role not in interaction.user.roles:
        await interaction.response.send_message(NO_PERMISSION_MESSAGE, ephemeral=True)
        return

    embed_dm = make_embed(
        color=AURORI_COLOR,
        title=title,
        description=message
    )
    embed_dm.set_author(name="Message from Aether Music's Staff", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)
    embed_dm.set_footer(text=f"Sent by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)

    try:
        await user.send(embed=embed_dm)
        await interaction.response.send_message(f"✅ Message sent to {user.mention}", ephemeral=False)
        print(f"Slash /{interaction.command.name} {COMMAND_EXECUTED_MESSAGE} {interaction.user.name}, message sent to {user.name}")
    except discord.Forbidden:
        await interaction.response.send_message(f"❌ Failed to send a DM to {user.mention}", ephemeral=False)