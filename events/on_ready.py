import discord
from discord.ext import commands

from utils import config, logger

ACTIVITY_MAPPING = {
    "playing": lambda name: discord.Game(name=name),
    "listening": lambda name: discord.Activity(type=discord.ActivityType.listening, name=name),
    "watching": lambda name: discord.Activity(type=discord.ActivityType.watching, name=name),
    "streaming": lambda name: discord.Activity(type=discord.ActivityType.streaming, name=name),
    "competing": lambda name: discord.Activity(type=discord.ActivityType.competing, name=name),
}

class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        try:
            await self.bot.tree.sync()
            logger.info("Command tree synced successfully.")
        except Exception as e:
            logger.error(f"Error syncing command tree: {e}")
            return  

        status_message = config.get("status_message", "github.com/graynixx") 
        raw_status_type = config.get("status_type") 
        
        if not isinstance(raw_status_type, str):
            logger.warning(f"Invalid or missing status_type '{raw_status_type}', defaulting to 'playing'")
            status_type = "playing"
        else:
            status_type = raw_status_type.lower()

        if status_type not in ACTIVITY_MAPPING:
            logger.warning(f"Invalid status_type '{status_type}', defaulting to 'playing'")
            status_type = "playing"

        activity = ACTIVITY_MAPPING[status_type](status_message)

        try:
            await self.bot.change_presence(status=discord.Status.online, activity=activity)
            logger.info(f"{self.bot.user.name} is ready with status: {status_message}")
        except Exception as e:
            logger.error(f"Error changing bot status: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(OnReady(bot))