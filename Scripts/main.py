from pathlib import Path

from data import *
from commands import *
from tasks import *





TOKEN_FILENAME = ".token"
TOKEN_PATH = Path(__file__).resolve().parent.parent / ".token"

with open(TOKEN_PATH, "r") as token_file:
    TOKEN = token_file.read().strip()





# When the bot has connected to Discord
@client.event
async def on_ready():
    global guild
    global user_logs_channel

    # Initialize guild
    guild = client.get_guild(AETHER_MUSIC_ID)
    if guild is None:
        print(f"guild with ID {AETHER_MUSIC_ID} not found.")
        return

    # Initialize user logs channel
    user_logs_channel = client.get_channel(user_logs_channel_id)
    if user_logs_channel is None:
        print(f"Channel with ID {user_logs_channel_id} not found.")
        return

    # Start logging tasks only after user_logs_channel is initialized
    check_avatars.start(guild, client.get_channel(user_logs_channel_id))
    check_nicknames.start(guild, client.get_channel(user_logs_channel_id))
    check_usernames.start(guild, client.get_channel(user_logs_channel_id))

    # Initialize the testing channel
    testing_channel = client.get_channel(testing_channel_id)
    await testing_channel.send("I'm online! 🤓")
    print(f"{client.user} has connected to Discord!")
    if not testing_channel:
        print(f"Channel with ID `{testing_channel_id}` not found.")

    # Initialize user avatars and nicknames for all members in the guild
    for member in guild.members:
        user_avatars[member.id] = member.avatar
        user_nicknames[member.id] = member.nick
        user_usernames[member.id] = member.name





    # Sync /slash commands
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
    # Handle specific messages in the SCP: PyLab channel
    if message.channel.id == 1359200351282008236:
        thread = await message.channel.create_thread(name=f"{message.author.name}'s idea", message=message)
        await thread.send(f"Thank you {message.author.mention}! If you want to discuss anything, say it here, and don't forget to publish the message you sent!")
        print(f"SCP: PyLab thread created by {message.author.name}")

    # Allow the bot to process commands
    await client.process_commands(message)





# On disconnect
@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected from Discord!")





# Function to start the bot
def bot_startup():
    client.run(TOKEN)

bot_startup()