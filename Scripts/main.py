from datetime import timedelta, timezone
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

with open(BUMP_LEADERBOARD_PATH, "r", encoding="utf-8") as bump_leaderboard_file:
    bump_leaderboard = json.load(bump_leaderboard_file)





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
    uptime_timer.start(datetime.now())

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
    client.add_view(StaffApplicationsReviewView())

    await testing_channel.send("I'm online and ready! <:scugSilly:1406051577365794816>")





async def bump_warning(channel, user):
    await asyncio.sleep(7200)
    await channel.send(f"Hey {user.mention}, it's time to bump again! <:scugAmazed:1406042797529890908>")



@client.event
async def on_message(message):

    # Chat with members
    if not message.author.bot and client.user in message.mentions and any(role.id == MEMBER_ROLE_ID for role in message.author.roles):
        await message.channel.send(random.choice(chat_responses))
    if "[Check this out!](https://youtu.be/xvFZjo5PgG0)" in message.content and message.author.id == AURORI_ID:
        await message.edit(suppress=True)



    # Bump reminder and leaderboard update
    if message.author.id == DISBOARD_ID and message.embeds:
        embed = message.embeds[0]
        if embed.description and "Bump done" in embed.description:

            if message.interaction_metadata and message.interaction_metadata.user:
                user = message.interaction_metadata.user
                user_id_string = str(user.id)

                if user_id_string in bump_leaderboard:
                    bump_leaderboard[user_id_string]["Username"] = user.name
                    bump_leaderboard[user_id_string]["Display name"] = user.display_name
                    bump_leaderboard[user_id_string]["Bump count"] = bump_leaderboard[user_id_string].get("Bump count", 0) + 1
                    bump_leaderboard[user_id_string]["Last bump"] = str(datetime.now().strftime("%d-%m-%Y, %H:%M"))

                else:
                    bump_leaderboard[user_id_string] = {"Username" : user.name,
                                                        "Display name" : user.display_name,
                                                        "Bump count" : 1,
                                                        "Last bump" : str(datetime.now().strftime("%d-%m-%Y %H:%M"))
                                                        }

                with open(BUMP_LEADERBOARD_PATH, "w", encoding="utf-8") as bump_leaderboard_file:
                    json.dump(bump_leaderboard, bump_leaderboard_file, indent=4)

                await message.channel.send("Thank you for bumping the server! <:scugSilly:1406051577365794816>")
                asyncio.create_task(bump_warning(channel=message.channel, user=message.interaction_metadata.user))

                bump_leader_role = aether_music.get_role(BUMP_LEADER_ROLE_ID)

                top_user_id = max(bump_leaderboard.items(), key=lambda item: item[1].get("Bump count", 0))[0]

                top_member = aether_music.get_member(int(top_user_id))

                for user in bump_leader_role.members:
                    if user != top_member:
                        await user.remove_roles(bump_leader_role)
                        print(f"Removed Bump Leader role from {user.name}")

                if bump_leader_role not in top_member.roles:
                    await top_member.add_roles(bump_leader_role)
                    print(f"Assigned Bumper Leader role to {top_member.name} with {bump_leaderboard[top_user_id].get('Bump count', 0)} bumps")

                # Data backup
                data_backup_channel = aether_music.get_channel(DATA_BACKUP_CHANNEL_ID)

                json_bytes = json.dumps(bump_leaderboard, indent=4).encode("utf-8")
                bump_leaderboard_backup_file = discord.File(fp=io.BytesIO(json_bytes), filename="bump_leaderboard.json")

                await data_backup_channel.send(file=bump_leaderboard_backup_file)



    # Commands processing permission
    await client.process_commands(message)





@client.event
async def on_member_join(user):
    account_age = datetime.now(timezone.utc) - user.created_at

    if account_age < timedelta(days=30):
        print(f"Didn't assing Member role to the new user {user.name}, account too young")
        return

    member_role = aether_music.get_role(MEMBER_ROLE_ID)

    await user.add_roles(member_role)
    print(f"Assigned Member role to the new user {user.name}")

    bot_member = aether_music.me
    verification_role = aether_music.get_role(VERIFICATION_ROLE_ID)

    roles_to_remove = [role for role in user.roles if role != aether_music.default_role and not role.managed and role < bot_member.top_role]

    with open(VERIFICATION_LIST_PATH, "r", encoding="utf-8") as verification_file:
        verification_list = json.load(verification_file)

    user_id_string = str(user.id)

    if user_id_string in verification_list:
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

            print(f"Returning user {user.name} has been sent to the verification channel")





@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected from Discord!")





def bot_startup():
    client.run(TOKEN)

bot_startup()