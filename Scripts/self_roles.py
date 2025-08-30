import discord

from data import *





class SelfRolesMiscView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(emoji="🎵", style=discord.ButtonStyle.primary, custom_id="musician_button")
    async def musician_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(MUSICIAN_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="🎨", style=discord.ButtonStyle.primary, custom_id="artist_button")
    async def artist_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(ARTIST_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="🎮", style=discord.ButtonStyle.primary, custom_id="gamer_button")
    async def gamer_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(GAMER_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="💻", style=discord.ButtonStyle.primary, custom_id="coder_button")
    async def coder_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(CODER_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="📸", style=discord.ButtonStyle.primary, custom_id="photographer_button")
    async def photographer_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(PHOTOGRAPHER_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="✍️", style=discord.ButtonStyle.primary, custom_id="writer_button")
    async def writer_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(WRITER_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="📚", style=discord.ButtonStyle.primary, custom_id="lore_hunter_button")
    async def lore_hunter_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(LORE_HUNTER_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")



class SelfRolesPingView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(emoji="🎶", style=discord.ButtonStyle.primary, custom_id="release_ping_button")
    async def release_ping_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(RELEASE_PING_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="📊", style=discord.ButtonStyle.primary, custom_id="poll_ping_button")
    async def poll_ping_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(POLL_PING_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")

    @discord.ui.button(emoji="🕹️", style=discord.ButtonStyle.primary, custom_id="gaming_ping_button")
    async def gaming_ping_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        role = guild.get_role(GAMING_PING_ROLE_ID)

        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"❌ Succesfully removed the role: {role.mention}", ephemeral=True)
            print(f"Succesfully removed the self role {role.name} to {user.name}")
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"✅ Succesfully given you the role: {role.mention}", ephemeral=True)
            print(f"Succesfully given the self role {role.name} to {user.name}")