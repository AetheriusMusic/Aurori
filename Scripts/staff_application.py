import json
import io

import discord

from data import *
from utility import *





STAFF_APPLICATIONS_LIST_PATH = Path(__file__).resolve().parent.parent / "Data/.staff_applications_list.json"



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

    age = discord.ui.TextInput(
        label="Your age (optional but must be over 13)",
        placeholder="How old are you?",
        required=False,
        max_length=3
    )

    country = discord.ui.TextInput(
        label="Your country (optional)",
        placeholder="Where are you from?",
        required=False,
        max_length=100
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
        data_backup_channel = interaction.client.get_channel(DATA_BACKUP_CHANNEL_ID)

        if self.age.value == None or self.age.value.strip() == "":
            age_answer = "Age not specified <:scugScribble:1430184357225693204>"
        elif self.age.value != None:
            age_answer = self.age.value

        if self.country.value == None or self.country.value.strip() == "":
            country_answer = "Country not specified <:scugScribble:1430184357225693204>"
        elif self.country.value != None:
            country_answer = self.country.value

        user_id_string = str(author.id)



        embed_application = make_embed(
                    channel=staff_forms_channel,
                    title=f"New Staff Application by **{author.mention}**",
                    field_1_title="Provided Username",
                    field_1_description=self.name.value,
                    field_1_is_inline=False,
                    field_2_title="Provided ID",
                    field_2_description=self.user_id.value,
                    field_2_is_inline=False,
                    field_3_title="Country",
                    field_3_description=country_answer,
                    field_3_is_inline=True,
                    field_4_title="Age",
                    field_4_description=age_answer,
                    field_4_is_inline=True,
                    field_5_title="Reason for Applying",
                    field_5_description=self.reason.value,
                    color=AURORI_COLOR
                )
        embed_application.set_thumbnail(url=author.display_avatar.url if author.display_avatar else author.default_avatar.url)
        embed_application.set_footer(text=f"User ID: {author.id}")



        with open(STAFF_APPLICATIONS_LIST_PATH, "r", encoding="utf-8") as staff_applications_list_file:
                staff_applications_list = json.load(staff_applications_list_file)

        if user_id_string in staff_applications_list:
            status = staff_applications_list[user_id_string].get("Status")

            if status == "Pending":
                await interaction.response.send_message("You have already submitted an application! Please wait for a response from the Staff.", ephemeral=True)
                return

            elif status == "Approved":
                await interaction.response.send_message("You silly goose, are you trying to be part of Staff+? <:scugSilly:1406051577365794816>", ephemeral=True)
                return



        staff_applications_list[user_id_string] = {
            "Username": author.name,
            "Display name": author.display_name,
            "Join date": author.joined_at.strftime("%d/%m/%Y"),
            "Reason": self.reason.value,
            "Age": age_answer,
            "Country": country_answer,
            "Application date": discord.utils.utcnow().strftime("%d/%m/%Y"),
            "Status": "Pending",
        }

        with open(STAFF_APPLICATIONS_LIST_PATH, "w", encoding="utf-8") as staff_applications_list_file:
            json.dump(staff_applications_list, staff_applications_list_file, indent=4)

        await staff_forms_channel.send(embed=embed_application, view=StaffApplicationsReviewView())

        await interaction.response.send_message("<:scugSilly:1406051577365794816> Thank you for applying! We'll reach out to you soon to let you know if you get accepted!", ephemeral=True)
        print(f"New staff application submitted by {author.name}")

        with open(STAFF_APPLICATIONS_LIST_PATH, "r", encoding="utf-8") as staff_applications_list_file:
            staff_applications_list = json.load(staff_applications_list_file)

        # Data backup
        json_bytes = json.dumps(staff_applications_list, indent=4).encode("utf-8")
        staff_applications_list_backup_file = discord.File(fp=io.BytesIO(json_bytes), filename="staff_applications_list_backup.json")

        await data_backup_channel.send(file=staff_applications_list_backup_file)



class StaffApplicationFormView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="👮 Staff Application", style=discord.ButtonStyle.primary, custom_id="staff_application_button")
    async def staff_application_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(StaffApplicationFormModal())



class StaffApplicationsReviewView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)



    @discord.ui.button(label="✅ Approve", style=discord.ButtonStyle.green, custom_id="staff_applications_review_approve_button")
    async def staff_applications_review_approve_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user.id != AETHERIUS_ID:
            await interaction.response.send_message("You silly goose <:scugSilly:1406051577365794816>", ephemeral=True)
            return

        data_backup_channel = interaction.client.get_channel(DATA_BACKUP_CHANNEL_ID)
        embed = interaction.message.embeds[0]
        user_id_string = str(embed.footer.text.split(": ")[1])



        with open(STAFF_APPLICATIONS_LIST_PATH, "r", encoding="utf-8") as staff_applications_list_file:
                staff_applications_list = json.load(staff_applications_list_file)

        if user_id_string in staff_applications_list:
            status = staff_applications_list[user_id_string].get("Status")

            if status == "Pending":
                staff_applications_list[user_id_string]["Status"] = "Approved"
                staff_applications_list[user_id_string]["Approve date"] = discord.utils.utcnow().strftime("%d/%m/%Y")

            elif status == "Approved":
                await interaction.response.send_message("This user is already a staffer <:scugSilly:1406051577365794816>", ephemeral=True)
                return

            elif status == "Denied":
                await interaction.response.send_message("This user has already been denied <:scugFlabbergasted:1406807246159216802>", ephemeral=True)
                return



            with open(STAFF_APPLICATIONS_LIST_PATH, "w", encoding="utf-8") as staff_applications_list_file:
                    json.dump(staff_applications_list, staff_applications_list_file, indent=4)

            await interaction.response.send_message("🔥 The Staff application has been approved!", ephemeral=True)

            # Data backup
            json_bytes = json.dumps(staff_applications_list, indent=4).encode("utf-8")
            staff_applications_list_backup_file = discord.File(fp=io.BytesIO(json_bytes), filename="staff_applications_list_backup.json")

            await data_backup_channel.send(file=staff_applications_list_backup_file)



    @discord.ui.button(label="❌ Deny", style=discord.ButtonStyle.red, custom_id="staff_applications_review_deny_button")
    async def staff_applications_review_deny_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user.id != AETHERIUS_ID:
            await interaction.response.send_message("You silly goose <:scugSilly:1406051577365794816>", ephemeral=True)
            return

        data_backup_channel = interaction.client.get_channel(DATA_BACKUP_CHANNEL_ID)
        embed = interaction.message.embeds[0]
        user_id_string = str(embed.footer.text.split(": ")[1])



        with open(STAFF_APPLICATIONS_LIST_PATH, "r", encoding="utf-8") as staff_applications_list_file:
                staff_applications_list = json.load(staff_applications_list_file)

        if user_id_string in staff_applications_list:
            status = staff_applications_list[user_id_string].get("Status")

            if status == "Pending":
                staff_applications_list[user_id_string]["Status"] = "Denied"
                staff_applications_list[user_id_string]["Deny date"] = discord.utils.utcnow().strftime("%d/%m/%Y")

            elif status == "Denied":
                await interaction.response.send_message("This user has already been denied <:scugFlabbergasted:1406807246159216802>", ephemeral=True)
                return

            elif status == "Approved":
                await interaction.response.send_message("This user is already a staffer <:scugSilly:1406051577365794816>", ephemeral=True)
                return



            with open(STAFF_APPLICATIONS_LIST_PATH, "w", encoding="utf-8") as staff_applications_list_file:
                    json.dump(staff_applications_list, staff_applications_list_file, indent=4)

            await interaction.response.send_message("⛔ The Staff application has been denied!", ephemeral=True)

            # Data backup
            json_bytes = json.dumps(staff_applications_list, indent=4).encode("utf-8")
            staff_applications_list_backup_file = discord.File(fp=io.BytesIO(json_bytes), filename="staff_applications_list_backup.json")

            await data_backup_channel.send(file=staff_applications_list_backup_file)