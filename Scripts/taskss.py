from pathlib import Path

from discord import Intents
from discord.ext import commands, tasks

from data import *
from utility import *



# Avatar update
user_avatars = {}

@tasks.loop(seconds=10)
async def check_avatars(guild):
    if user_logs_channel is None:
        print("User logs channel is not initialized. Skipping avatar check.")
        return

    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_avatars:
            if member.avatar != user_avatars[member.id]:  # Compare stored avatar with current avatar
                await user_logs_channel.send(f"{member.name} changed their avatar!")
                await user_logs_channel.send(f"Old avatar: {user_avatars[member.id]}")
                await user_logs_channel.send(f"New avatar: {member.avatar}")
                print(f"{member.name} changed their avatar!")
                print(f"Old avatar: {user_avatars[member.id]}")
                print(f"New avatar: {member.avatar}")
                make_embed(channel=user_logs_channel,
                           title="Avatar Update",
                           description=f"{member.name} changed their avatar!",
                           color=aether_color,
                           field_1_title="Old avatar",
                           field_1_description=user_avatars[member.id],
                           field_2_title="New avatar",
                           field_2_description=member.avatar)

                # Update the stored avatar
                user_avatars[member.id] = member.avatar
        else:
            # Store the avatar if it's not already stored
            user_avatars[member.id] = member.avatar



# Nickname update
user_nicknames = {}

@tasks.loop(seconds=10)
async def check_nicknames(guild):
    if user_logs_channel is None:
        print("User logs channel is not initialized. Skipping nickname check.")
        return

    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_nicknames:
            if member.nick != user_nicknames[member.id]:  # Compare stored nickname with current nickname
                await user_logs_channel.send(f"{member.name} changed their nickname!")
                await user_logs_channel.send(f"Old nickname: {user_nicknames[member.id]}")
                await user_logs_channel.send(f"New nickname: {member.nick}")
                print(f"{member.name} changed their nick!")
                print(f"Old nickname: {user_nicknames[member.id]}")
                print(f"New nickname: {member.nick}")
                make_embed(channel=user_logs_channel,
                           title="Nickname Update",
                           description=f"{member.name} changed their nickname!",
                           color=aether_color,
                           field_1_title="Old nickname",
                           field_1_description=user_nicknames[member.id],
                           field_2_title="New nickname",
                           field_2_description=member.nick)

                # Update the stored nick
                user_nicknames[member.id] = member.nick
        else:
            # Store the nick if it's not already stored
            user_nicknames[member.id] = member.nick