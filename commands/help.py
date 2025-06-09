import discord
from discord import app_commands
from discord.ext import commands

from assets import Color


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='help', description="Show help information")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Help", description="This is a simple, open-source Discord bot built with discord.py. It’s designed to be lightweight and easy to use, with the flexibility to add new features if needed. Whether you’re looking for a basic moderation bot or want to customize it for your server, it’s a great starting point. You can find the source code on [GitHub](https://github.com/graynixx/DiscordBot).", color=Color.INFO)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))