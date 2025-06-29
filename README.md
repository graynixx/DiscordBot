# Discord-bot

A simple, open-source Discord bot built with [discord.py](https://github.com/Rapptz/discord.py).
This bot is designed to be lightweight, easy to use, and flexible for adding new features.
It's a great starting point for moderation, automation, or custom server utilities.

## Features

-   Slash command support (e.g., `/help`)
-   Configuration via `config.json`
-   Color-coded logging for better readability
-   Modular structure for easy command and event extension

---

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/graynixx/DiscordBot.git
    cd DiscordBot
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Required packages:

    - `discord.py==2.3.2`
    - `python-dotenv`
    - `colorama`
    - `art`

3. **Set up environment variables:**

    Create a `.env` file in the project root with the following content:

    ```env
    TOKEN=YOUR_DISCORD_BOT_TOKEN
    ```

4. **Configure the bot:**

    Edit `config.json` to set:

    - Bot name
    - Status type and message
    - Bot ID
    - (Optional) legacy prefix
    - **Intents** (new system!)

---

## Creating Your Bot in the Discord Developer Portal

> Follow these steps to create and connect your bot to a Discord server.

### 1. Create a New Application

-   Go to the [Discord Developer Portal](https://discord.com/developers/applications)
-   Click **"New Application"**, give it a name, and confirm

### 2. Configure Your Bot

When a new application is created, a bot user is automatically included.

-   Go to the **"Bot"** tab in the sidebar
-   Here you can:

    -   Change the bot’s **username** and **icon**
    -   Click **"Reset Token"** (or "Copy") to get the token

### 3. Set Up Your Token

-   Paste the copied token into your `.env` file:

    ```env
    TOKEN=YOUR_DISCORD_BOT_TOKEN
    ```

> Never share your token publicly — treat it like a password.

### 4. Enable Required Intents

**Important!** Based on what you configure in the `config.json` file (under the `intents` field), make sure you enable those exact intents in the **Bot tab** in the Discord Developer Portal.

For example, if you set:

```json
"intents": ["members", "presences"]
```

Then in the Discord Developer Portal, you **must enable** the **Presence Intent** and the **Server Members Intent** in the **Bot tab**.

To enable the intents:

-   Go to the **Bot** tab in the Discord Developer Portal.
-   Under **Privileged Gateway Intents**, toggle on:

    -   **Presence Intent**
    -   **Server Members Intent**
    -   **Message Content Intent** (if you're using `message_content` intent in `config.json`)

These intents must match what's configured in your `config.json`.

### 5. Invite the Bot to Your Server

-   Go to **OAuth2 > URL Generator**
-   Under **Scopes**, check:

    -   `bot`
    -   `applications.commands`

-   Under **Bot Permissions**, select what your bot needs (example):

    -   `Send Messages`
    -   `Manage Messages`
    -   `Read Message History`
    -   `Kick Members`

-   Copy the generated URL, open it in your browser, and invite the bot to your server

---

## Adding Commands & Events

-   Place new command files in the [`commands/`](commands/) folder
-   Place new event listeners in the [`events/`](events/) folder
-   Each file should define a **Cog class** and an asynchronous `setup(bot)` function

---

## Example Command

See [`commands/help.py`](commands/help.py) for a sample implementation of a slash command.

---

## Configuration Reference

Edit the `config.json` file to customize the bot's behavior:

| Field            | Description                                                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bot_name`       | The bot’s display name                                                                                                                                     |
| `prefix`         | (Optional) prefix for legacy text commands                                                                                                                 |
| `bot_id`         | Your bot’s Discord user ID                                                                                                                                 |
| `status_message` | The bot’s status message                                                                                                                                   |
| `status_type`    | One of: `playing`, `listening`, `watching`, `streaming`, `competing`                                                                                       |
| `intents`        | Set intents for the bot. You can either use `"all"` for all intents, or specify a list of intents to enable individually, e.g., `["members", "presences"]` |

---

## Example `config.json`:

```json
{
	"bot_name": "DiscordBot",
	"prefix": ".",
	"bot_id": "your_bot_id",
	"intents": "all",

	"status_message": "Minecraft",
	"status_type": "playing"
}
```

In the `intents` field, you have two options:

1. **Use `"all"`** to enable all intents, or
2. **Use a list of specific intents** you want to enable, such as:

    - `"members"`
    - `"presences"`
    - `"message_content"`

---

## Logging

The bot uses color-coded logs for easier debugging and visibility.
See [`logger.py`](logger.py) to modify log formatting or levels.

---

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

❤ Made with passion by [@graynix](https://github.com/graynixx)

---

### Quickstart (TL;DR)

```bash
git clone https://github.com/graynixx/DiscordBot.git
cd DiscordBot
pip install -r requirements.txt

# Add your bot token to a .env file
# Edit config.json if needed

python main.py
```

---
