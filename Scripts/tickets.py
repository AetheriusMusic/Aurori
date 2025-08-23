import discord

from data import *





class SupportTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🆘 Support Ticket", style=discord.ButtonStyle.green, custom_id="support_ticket")
    async def support_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        category=guild.get_channel(OTHER_CATEGORY_ID)

        existing_channel = discord.utils.get(
            category.text_channels, name=f"support-ticket-{user.name.lower()}"
        )
        if existing_channel:
            await interaction.response.send_message(f"⚠️ You already have an open support ticket: {existing_channel.mention}", ephemeral=True)
            return

        member_role = guild.get_role(MEMBER_ROLE_ID)
        staff_role = guild.get_role(STAFF_ID)

        # Private text channel for the ticket
        overwrites = {
            member_role: discord.PermissionOverwrite(view_channel=False),
            user: discord.PermissionOverwrite(view_channel=True)
        }

        support_ticket_channel = await guild.create_text_channel(
            name=f"support-ticket-{user.name}",
            overwrites=overwrites,
            category=category
        )

        await support_ticket_channel.send(f"{user.mention} thanks for creating a **Support Ticket**! A {staff_role.mention} member will be here to assist you soon!")

        await interaction.response.send_message(f"✅ Your ticket has been created: {support_ticket_channel.mention}", ephemeral=True)

        print(f"Support ticket succesfully created by {user.name}")