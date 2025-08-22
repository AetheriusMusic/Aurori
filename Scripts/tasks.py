from discord.ext import tasks

from data import *
from utility import *





# Avatar update
user_avatars = {}

@tasks.loop(seconds=TASK_TIMER)
async def check_avatars(guild, channel):
    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_avatars:
            if member.avatar != user_avatars[member.id]:  # Compare stored avatar with current avatar
                old_avatar_url = user_avatars[member.id].url if user_avatars[member.id] else "No previous avatar"
                new_avatar_url = member.avatar.url if member.avatar else "No current avatar"

                print(f"{member.name} changed their avatar!")
                print(f"Old avatar: {old_avatar_url}")
                print(f"New avatar: {new_avatar_url}")

                # Create the embed
                embed = make_embed(
                                channel=client.get_channel(USER_LOGS_CHANNEL_ID),
                                title="Avatar Update",
                                description=f"{member.name} changed their **avatar**!",
                                color=USER_LOGS_COLOR,
                                field_1_title="Old avatar",
                                field_1_description=f"{old_avatar_url}",
                                field_2_title="New avatar",
                                field_2_description=f"{new_avatar_url}"
                )

                embed.set_author(name=member.name, icon_url=member.avatar.url if member.avatar else None)

                # Add the new avatar as a thumbnail
                embed.set_thumbnail(url=old_avatar_url)
                embed.set_image(url=new_avatar_url)

                await channel.send(embed=embed)

                # Update the stored avatar
                user_avatars[member.id] = member.avatar
        else:
            # Store the avatar if it's not already stored
            user_avatars[member.id] = member.avatar



# Nickname update
user_nicknames = {}

@tasks.loop(seconds=TASK_TIMER)
async def check_nicknames(guild, channel):

    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_nicknames:
            if member.nick != user_nicknames[member.id]:  # Compare stored username with current username
                print(f"{member.name} changed their nickname!")
                print(f"Old nickname: {user_usernames[member.id]}")
                print(f"New nickname: {member.nick}")
                embed = make_embed(
                                channel=client.get_channel(USER_LOGS_CHANNEL_ID),
                                title="Nickname Update",
                                description=f"{member.mention} changed their **nickname**!",
                                color=USER_LOGS_COLOR,
                                field_1_title="Old nickname",
                                field_1_description=user_nicknames[member.id],
                                field_2_title="New nickname",
                                field_2_description=member.nick
                )

                embed.set_author(name=member.nick, icon_url=member.avatar.url if member.avatar else None)

                await channel.send(embed=embed)
                

                # Update the stored nick
                user_nicknames[member.id] = member.nick
        else:
            # Store the nick if it's not already stored
            user_nicknames[member.id] = member.nick



# Username update
user_usernames = {}

@tasks.loop(seconds=TASK_TIMER)
async def check_usernames(guild, channel):

    for member in guild.members:  # Iterate through all members in the guild
        if member.id in user_usernames:
            if member.name != user_usernames[member.id]:  # Compare stored username with current username
                print(f"{member.name} changed their username!")
                print(f"Old username: {user_usernames[member.id]}")
                print(f"New username: {member.name}")
                embed = make_embed(
                                channel=client.get_channel(USER_LOGS_CHANNEL_ID),
                                title="Username Update",
                                description=f"{member.mention} changed their **username**!",
                                color= USER_LOGS_COLOR,
                                field_1_title="Old username",
                                field_1_description=user_usernames[member.id],
                                field_2_title="New username",
                                field_2_description=member.name
                )

                embed.set_author(name=member.name, icon_url=member.avatar.url if member.avatar else None)

                await channel.send(embed=embed)
                

                # Update the stored nick
                user_usernames[member.id] = member.name
        else:
            # Store the nick if it's not already stored
            user_usernames[member.id] = member.name