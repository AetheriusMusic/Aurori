from discord import Intents
from discord.ext import commands





# Discord intents (permissions for the bot)
intents = Intents.default()
intents.message_content = True  # For reading message content
intents.guilds = True           # For detecting guilds (servers)
intents.presences = True        # Enable presence intent
intents.members = True          # Required for fetching members
intents.webhooks = True         # Required for sending webhooks

# Bot data
app_id = 1328115239996358656
app_public_key = "5fee0f8102a8fa7eae4bf7057300c0fc7b41ea5278644c6bf35647ab26c26bbc"
client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Server data
aether_music = None
AETHER_MUSIC_ID = 1275409524643205212

# Miscellaneous
ERROR_MESSAGE = "An error occurred while executing the command:"
NO_PERMISSION_MESSAGE = "You don't have permission to use this command!"
TASK_TIMER = 10

# User IDs
AETHERIUS_ID = 767363924734509059
DISBOARD_ID = 302050872383242240

# Role IDs
MEMBER_ROLE_ID = 1292518936335749140
STAFF_ROLE_ID = 1275970872217440256

# Colors
AETHER_COLOR = "#9954DD"
AURORI_COLOR = "#54c2e0"
SUPPORT_TICKET_COLOR = "#1BAC55"
USER_LOGS_COLOR = "#53B6E0"

# Channel IDs
TESTING_CHANNEL_ID = 1328140497364975656
USER_LOGS_CHANNEL_ID = 1292539484201685012
TICKETS_CHANNEL_ID = 1353416469160923276

# Category IDs
OTHER_CATEGORY_ID = 1408475211720036504

# Webhook URLs
spamping_general_url = "https://discord.com/api/webhooks/1367871548580691999/BDf3vZ4pS2xfG2HccuX8g3zGgobAFpxo6OcBmUNBpqrpch4S-v9o57b26fFKo9R4Pz0z"
spamping_silksong_url = "https://discord.com/api/webhooks/1346566625591033886/oApOk5EeMufdPcExHaYslNSx6MxCJWhUR_JvS_P-XjCGG1sDc2fLg5-2mzADLLyQSMoZ"