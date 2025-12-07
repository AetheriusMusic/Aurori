from pathlib import Path

from data import *
from commands import *
from tasks import *
from tickets import *
from self_roles import *
from staff_application import *





TOKEN_PATH = Path(__file__).resolve().parent.parent / "Keys/.token"

with open(TOKEN_PATH, "r", encoding="utf-8") as token_file:
    TOKEN = token_file.read().strip()

CHAT_RESPONSES_PATH = Path(__file__).resolve().parent.parent / "Data/chat_responses.txt"

with open(CHAT_RESPONSES_PATH, "r", encoding="utf-8") as chat_responses_file:
    chat_responses = [line.strip() for line in chat_responses_file]

BUMP_LEADERBOARD_PATH = Path(__file__).resolve().parent.parent / "Data/bump_leaderboard.json"





@client.event
async def on_ready():
    global aether_music
    global user_logs_channel

    # Guild initialization
    aether_music = client.get_guild(AETHER_MUSIC_ID)

    # Channels initialization
    user_logs_channel = client.get_channel(USER_LOGS_CHANNEL_ID)
    testing_channel = client.get_channel(TESTING_CHANNEL_ID)
    print(f"{client.user} has succesfully connected to Aether Music!")

    # Logging tasks startup
    for member in aether_music.members:
        user_avatars[member.id] = member.avatar
        user_nicknames[member.id] = member.nick
        user_usernames[member.id] = member.name
    check_avatars.start(aether_music, client.get_channel(USER_LOGS_CHANNEL_ID))
    check_nicknames.start(aether_music, client.get_channel(USER_LOGS_CHANNEL_ID))
    check_usernames.start(aether_music, client.get_channel(USER_LOGS_CHANNEL_ID))

    # /Slash commands registration
    await client.tree.sync()

    for command in client.tree.get_commands():
        print(f"Succesfully registered /slash command: /{command.name}")

    # Views reassignment
    client.add_view(CloseTicketView())
    client.add_view(SupportTicketView())
    client.add_view(SelfRolesMiscView())
    client.add_view(SelfRolesPingView())
    client.add_view(StaffApplicationFormView())

    await testing_channel.send("I'm online and ready! <:scugSilly:1406051577365794816>")





@client.event
async def on_message(message):

    # Chat with members
    if client.user in message.mentions and any(role.id == MEMBER_ROLE_ID for role in message.author.roles):
        await message.channel.send(random.choice(chat_responses))
    if "[Check this out!](https://youtu.be/xvFZjo5PgG0)" in message.content and message.author.id == AURORI_ID:
        await message.edit(suppress=True)

    # Bump thanking
    if message.author.id == DISBOARD_ID and message.embeds:
        embed = message.embeds[0]
        if embed.description and "Bump done" in embed.description:
            await message.channel.send("Thank you for bumping the server! <:scugSilly:1406051577365794816>")



    # Commands processing permission
    await client.process_commands(message)





@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected from Discord!")





def bot_startup():
    client.run(TOKEN)

bot_startup()