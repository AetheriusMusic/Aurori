import discord

from data import *





def debug_print(text):
     print(f"DEBUG: {text}")

def error_print(text):
     print(f"ERROR: {text}")



def make_embed(channel,
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

        # Hex color to discord.Color
        color = discord.Color(int(color.lstrip("#"), 16))

        embed = discord.Embed(title=title, description=description, color=color)
        if field_1_title and field_1_description:
            embed.add_field(name=field_1_title, value=field_1_description, inline=field_1_is_inline)
            if field_2_title and field_2_description:
                embed.add_field(name=field_2_title, value=field_2_description, inline=field_2_is_inline)
                if field_3_title and field_3_description:
                    embed.add_field(name=field_3_title, value=field_3_description, inline=field_3_is_inline)
        if footer:
            guild = client.get_guild(AETHER_MUSIC_ID)
            embed.set_footer(text=footer, icon_url=guild.icon.url)

        return embed