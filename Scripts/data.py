from pathlib import Path

from discord import Intents
from discord.ext import commands





WEBHOOK_URL_PATH = Path(__file__).resolve().parent.parent / "Keys/.webhook_urls"

with open(WEBHOOK_URL_PATH, "r", encoding="utf-8") as webhook_urls_file:
    webhook_urls = [line.strip() for line in webhook_urls_file]



# Discord intents
intents = Intents.default()
intents.message_content = True
intents.guilds = True
intents.presences = True
intents.members = True
intents.webhooks = True

# Bot data
app_id = 1328115239996358656
app_public_key = "5fee0f8102a8fa7eae4bf7057300c0fc7b41ea5278644c6bf35647ab26c26bbc"
client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Server data
AETHER_MUSIC_ID = 1275409524643205212
guild = client.get_guild(AETHER_MUSIC_ID)

# Miscellaneous
ERROR_MESSAGE = "An error occurred while executing the command:"
NO_PERMISSION_MESSAGE = "You don't have permission to use this command!"
COMMAND_EXECUTED_MESSAGE = "command successfully executed by"
TASK_TIMER = 5

# User IDs
AETHERIUS_ID = 767363924734509059
AURORI_ID = 1328115239996358656
DISBOARD_ID = 302050872383242240

# Role IDs
MEMBER_ROLE_ID = 1292518936335749140
STAFF_ROLE_ID = 1275970872217440256
VERIFICATION_ROLE_ID = 1443741274724110356
BUMP_LEADER_ROLE_ID = 1447321851641593996

MUSICIAN_ROLE_ID = 1292614107572211793
ARTIST_ROLE_ID = 1292614108805333084
GAMER_ROLE_ID = 1374790675647824003
CODER_ROLE_ID = 1374791842343813260
PHOTOGRAPHER_ROLE_ID = 1374794704322953246
WRITER_ROLE_ID = 1374792123215511743
LORE_HUNTER_ROLE_ID = 1374791432468037733

RELEASE_PING_ROLE_ID = 1346461326544867339
GAMING_PING_ROLE_ID = 1374795318465527848
POLL_PING_ID = 1411443477991915591

# Colors
AETHER_COLOR = "#9954DD"
AURORI_COLOR = "#54c2e0"
SUPPORT_TICKET_COLOR = "#1BAC55"
USER_LOGS_COLOR = "#53B6E0"

# Channel IDs
TESTING_CHANNEL_ID = 1328140497364975656
USER_LOGS_CHANNEL_ID = 1292539484201685012
TICKETS_CHANNEL_ID = 1353416469160923276
VERIFICATION_CHANNEL_ID = 1431972672232751235
STAFF_FORMS_CHANNEL_ID = 1447296864985551050

# Category IDs
OTHER_CATEGORY_ID = 1408475211720036504

# Webhook URLs
spamping_bot_commands_url = webhook_urls[0]
spamping_silksong_url = webhook_urls[1]