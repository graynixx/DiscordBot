import json
import sys

import discord

from logger import setup_logger

logger = setup_logger()

INTENTS_MAP = {
    "members": "members",                 
    "presences": "presences",            
    "message_content": "message_content"  
}


def get_config(config_path: str) -> dict:
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        logger.critical(f"Config file not found: {config_path}")
        sys.exit(1) 
    except json.JSONDecodeError as e:
        logger.critical(f"Invalid JSON in config file: {e}")
        sys.exit(1) 

    if not config.get("bot_id"):
        logger.critical("Missing required config value: 'bot_id'")
        sys.exit(1) 

    return config


def get_intents(config: dict) -> discord.Intents:
    if config.get("intents") == "all":
        return discord.Intents.all()

    intents = discord.Intents.default()

    for name in config.get("intents", []):
        attr = INTENTS_MAP.get(name.lower())
        if attr:
            setattr(intents, attr, True)
        else:
            logger.warning(f"Unknown intent '{name}' in config.json — skipping.")
            
    return intents


config = get_config("config.json")
intents = get_intents(config)
