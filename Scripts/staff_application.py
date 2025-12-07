import discord

from data import *
from utility import *





class StaffApplicationFormModal(discord.ui.Modal, title="Staff Application Form"):

    name = discord.ui.TextInput(
        label="Your username",
        placeholder="Write your username here.",
        required=True,
        max_length=32
    )

    user_id = discord.ui.TextInput(
        label="Your user ID",
        placeholder="Make sure to enable Developer Mode in the settings.",
        required=True,
        min_length=17,
        max_length=24
    )

    country = discord.ui.TextInput(
        label="Your country (optional)",
        placeholder="Where are you from?",
        required=False,
        max_length=100
    )

    age = discord.ui.TextInput(
        label="Your age (optional but over 13)",
        placeholder="How old are you?",
        required=False,
        max_length=3
    )

    reason = discord.ui.TextInput(
        label="Reason for applying",
        placeholder="Why do you want to become a staffer?",
        required=True,
        max_length=4000,
        style=discord.TextStyle.paragraph
    )



    async def on_submit(self, interaction: discord.Interaction):

        author = interaction.user
        staff_forms_channel = interaction.client.get_channel(STAFF_FORMS_CHANNEL_ID)

        embed_application = make_embed(
            channel=staff_forms_channel,
            title=f"New Staff Application by {author.name}",
            field_1_title="Name",
            field_1_description=self.name.value,
            field_1_is_inline=True,
            field_2_title="User ID",
            field_2_description=self.user_id.value,
            field_2_is_inline=True,
            field_3_title="Reason for Applying",
            field_3_description=self.reason.value,
            color=AURORI_COLOR
        )
        embed_application.set_thumbnail(url=author.display_avatar.url)
        embed_application.set_footer(text=f"User ID: {author.id}")

        await staff_forms_channel.send(embed=embed_application)

        await interaction.response.send_message(f"Thank you for applying! We'll reach out to you soon to let you know if you were accepted!", ephemeral=True)



class StaffApplicationFormView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="👮 Staff Application", style=discord.ButtonStyle.primary, custom_id="staff_application_button")
    async def staff_application_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(StaffApplicationFormModal())