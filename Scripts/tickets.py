import discord

from data import *





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

        await interaction.channel.delete()
        print(f"Ticket closed by {interaction.user.name}")



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

        existing_channel = discord.utils.get(category.text_channels, name=f"support-ticket-{user.name.lower()}")
        if existing_channel:
            await interaction.response.send_message(f"⚠️ You already have an open support ticket: {existing_channel.mention}", ephemeral=True)
            return

        # Private text channel for the ticket
        overwrites = {
            member_role: discord.PermissionOverwrite(view_channel=False),
            staff_role: discord.PermissionOverwrite(view_channel=True),
            user: discord.PermissionOverwrite(view_channel=True)
        }

        support_ticket_channel = await guild.create_text_channel(
            name=f"support-ticket-{user.name}",
            overwrites=overwrites,
            category=category
        )

        await support_ticket_channel.send(f"{user.mention} thanks for creating a **Support Ticket**! A {staff_role.mention} member will be here to assist you soon!", view=CloseTicketView())

        await interaction.response.send_message(f"✅ Your ticket has been created: {support_ticket_channel.mention}", ephemeral=True)

        print(f"Support ticket succesfully created by {user.name}")