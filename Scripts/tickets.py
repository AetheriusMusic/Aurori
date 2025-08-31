from pathlib import Path
from datetime import datetime
import discord
import asyncio

from data import *
from utility import *





class CloseTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🔒 Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket")

    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild
        staff_role = guild.get_role(STAFF_ROLE_ID)

        if staff_role not in interaction.user.roles:
            await interaction.response.send_message("❌ Only Staff can close the ticket!", ephemeral=True)
            return

        await interaction.response.send_message("⏳ Saving transcript...", ephemeral=True)

        messages = []

        async for message in interaction.channel.history(limit=None, oldest_first=True):

            timestamp = message.created_at.strftime("%Y-%d-%m_%H.%M.%S")
            author = message.author.name
            parts = []

            if message.content:
                parts.append(message.content)

            for attachment in message.attachments:
                parts.append(f"[Attachment: {attachment.url}]")

            for embed in message.embeds:
                embed_info = []
                if embed.title:
                    embed_info.append(f"Title: {embed.title}")
                if embed.description:
                    embed_info.append(f"Description: {embed.description}")
                if embed.url:
                    embed_info.append(f"URL: {embed.url}")
                if embed_info:
                    parts.append(f"[Embed: {' | '.join(embed_info)}]")

            content = " ".join(parts) if parts else "[No Content]"
            messages.append(f"[{timestamp}] {author}: {content}")

        transcripts_dir = Path(__file__).resolve().parent.parent / "Ticket Transcripts"
        transcripts_dir.mkdir(parents=True, exist_ok=True)

        attachments_dir = transcripts_dir / "Attachments"
        attachments_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%d-%m_%H.%M.%S")
        filename = f"{interaction.channel.name} {timestamp}.txt"
        transcript_path = transcripts_dir / filename

        with open(transcript_path, "w", encoding="utf-8") as transcript_file:
            transcript_file.write("\n".join(messages))

        async for message in interaction.channel.history(limit=None, oldest_first=True):

            for attachment in message.attachments:
                save_name = f"{interaction.channel.name}_{timestamp}_{attachment.id}_{attachment.filename}"
                save_path = attachments_dir / save_name

                try:
                    await attachment.save(save_path)
                    print(f"Attachment saved: {save_path}")
                except Exception as error:
                    error_print(f"Failed to save attachment {attachment.url}: {error}")

        await interaction.followup.send("✅ Transcript successfully saved to the database! Deleting channel...", ephemeral=True)

        await asyncio.sleep(5)

        await interaction.channel.delete()

        print(f"Ticket closed by {interaction.user.name} and transcript successfully saved to the database")



class SupportTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🆘 Support Ticket", style=discord.ButtonStyle.green, custom_id="support_ticket")

    async def support_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild
        user = interaction.user
        category=guild.get_channel(OTHER_CATEGORY_ID)
        member_role = guild.get_role(MEMBER_ROLE_ID)
        staff_role = guild.get_role(STAFF_ROLE_ID)

        existing_channel = discord.utils.get(category.text_channels, name=f"supp-ticket-{user.name.lower()}")
        if existing_channel:
            await interaction.response.send_message(f"⚠️ You already have an open support ticket: {existing_channel.mention}", ephemeral=True)
            return

        overwrites = {
            member_role: discord.PermissionOverwrite(view_channel=False),
            staff_role: discord.PermissionOverwrite(view_channel=True),
            user: discord.PermissionOverwrite(view_channel=True)
        }

        support_ticket_channel = await guild.create_text_channel(
            name=f"supp-ticket-{user.name}",
            overwrites=overwrites,
            category=category
        )

        await support_ticket_channel.send(f"{user.mention} thanks for creating a **Support Ticket**! A {staff_role.mention} member will be here to assist you soon!", view=CloseTicketView())

        await interaction.response.send_message(f"✅ Your ticket has been created: {support_ticket_channel.mention}", ephemeral=True)

        print(f"Support ticket succesfully created by {user.name}")