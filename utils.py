import json
import sys  
from logger import setup_logger

logger = setup_logger()


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


config = get_config("config.json")
