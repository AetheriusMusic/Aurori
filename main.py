import os
from dotenv import load_dotenv
from discord import Intents, Client

# STEP 0: Load token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# STEP 1: Bot setup
intents = Intents.default()
intents.message_content = True
intents.guilds = True
client = Client(intents=intents)

# STEP 3: Bot startup
@client.event
async def on_ready():
    print(f"{client.user} is now running!")

# STEP 5: Main entry point
def main():
    client.run(token=TOKEN)

main()