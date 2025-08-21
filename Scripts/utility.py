import discord

from data import *





chat_responses = [
                "<:scug_silly:1406051577365794816>",
                "I feel so sigma",
                "Wawa",
                "Perhaps you should consider not breathing.",
                "I'm silly",
                "I'm Evil Larry",
                "Human, I remember your'e **genocides**.",
                "**IT'S TV TIME!**",
                "Pandemonium door 30 <:pandemonium:1341859271876284457>",
                "Womp womp",
                "Rain World is peak",
                "Hollow Knight is peak",
                "Celeste is peak",
                "Inscryption is peak",
                "Undertale is peak",
                "Deltarune is peak",
                "You too",
                "||[ R E D A C T E D ]||",
                "Check behind you.",
                "**THE MIMIIIIIIIIIIC**",
                "You should **ASCEND YOURSELF**, **NOW!**",
                "No",
                "qhar",
                "I think you're crazy",
                "uwu",
                ":3",
                "**BAD PEOPLE GET PUT INTO THE TORTURE CHAMBER!**",
                "kebab is good",
                "Can... anybody hear me? Anyone?",
                "buble",
                "NO MERCY FOR YOU",
                "you should totally listen to Aetherius' music NOW!!11!!1!",
                "Hey, did you hear about this cool house in Karvina?",
                "Things really took a _weird_ route there",
                "You know what that means! **FISH!**",
                "You should **ULTRAKILL** yourself, **NOW!**",
                "Something wicked this way comes...",
                "Nice reference!",
                "Gloria ad Omega!",
                "||boo||",
                "complex? i find it quite simple actually",
                "i might be schizoprenic",
                "i'm silly",
                "HOCHI MAMA!",
                "that knight is pretty hollow... it's like it's some sort of... _**Hollow Knight*_...",
                "it's _raining_ so much in this _world_... what is it, some kind of... _**Rain World**_?!?",
                "GOD FUCKING DAMMIT KRIS, WHERE THE **FUCK** ARE WE?",
                "i'm not real",
                "you're not real",
                "get real",
                "||get a job||",
                "_bans you_",
                "erm... ackshually, according to my calcuclations 🤓",
                "I'm old!",
                "I'm gold!",
                "Kris, Get The Banana",
                "The Rot consumes...",
                "||⊗||",
                "You are not a doctor.",
                "Box of truth",
                "that dirty Leshy guy...",
                "this _Rodent_ sure does look _Golden_!",
                "[Check this out!](https://youtu.be/xvFZjo5PgG0)",
                "i like to think im funni",
                "susie rulez!",
                "Thank you for using our limited time only imaginary friend remote!",
                "I can't reason but I can tell you a lot of references to weird stuff that Aetherius enjoys",
                "stop!",
                "Chaos, Chaos!",
                "**HATSUNE MIKU?!?**",
                "my reaction to that information"
]



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

        # Convert hex color to discord.Color
        color = discord.Color(int(color.lstrip('#'), 16))

        embed = discord.Embed(title=title, description=description, color=color)
        if field_1_title and field_1_description:
            embed.add_field(name=field_1_title, value=field_1_description, inline=field_1_is_inline)
            if field_2_title and field_2_description:
                embed.add_field(name=field_2_title, value=field_2_description, inline=field_2_is_inline)
                if field_3_title and field_3_description:
                    embed.add_field(name=field_3_title, value=field_3_description, inline=field_3_is_inline)
        if footer:
            embed.set_footer(text=footer, icon_url=GUILD.icon.url)

        return embed