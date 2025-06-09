import asyncio
import os
import sys

import aiohttp
import discord
from art import text2art
from colorama import Fore, init
from discord.ext import commands
from dotenv import load_dotenv

from utils import config, logger

load_dotenv()
init(autoreset=True)

TOKEN = os.getenv("TOKEN")
BOT_NAME = config.get("bot_name", "DiscordBot")
PREFIX = config.get("prefix", ".")
BOTID = config["bot_id"]

if not TOKEN:
    logger.critical("Missing TOKEN in environment variables (.env)")
    sys.exit(1)

print(
    f"{Fore.CYAN}{text2art(BOT_NAME)}\n"
    f"{Fore.CYAN}Autor: {Fore.WHITE}Graynix\n"
    f"{Fore.CYAN}Github: {Fore.WHITE}github.com/graynixx"
    )

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command("help")

async def connect_cog():
    folders = ["commands", "events"]
    
    for folder in folders: 
        folder_path = f"./{folder}/"
        if os.path.exists(folder_path): 
            for file in os.listdir(folder_path):
                if file.endswith(".py"):  
                    try:
                        await bot.load_extension(f"{folder}.{file[:-3]}")
                        logger.info(f"Loaded extension: {file[:-3]}")
                    except Exception as e:
                        logger.error(f"Failed to load extension {file}: {e}")

async def main():
    try:
        await connect_cog()
        await bot.start(TOKEN)
    finally:
        if not bot.is_closed():
            await bot.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except discord.LoginFailure:
        logger.critical("Invalid TOKEN provided. Check your .env file.") 
    except discord.PrivilegedIntentsRequired as e:
        logger.critical(f"Missing privileged intents: {e}")
    except discord.HTTPException as e:
        logger.critical(f"HTTP error occurred: {e}")
    except asyncio.CancelledError:
        logger.warning("Asyncio task was cancelled.")
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot has been shut down gracefully.")
    except aiohttp.ClientError as e:
        logger.critical(f"Aiohttp client error: {e}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")