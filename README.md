# vcokltfre/RCONBot

## A Discord bot for connecting to a Minecraft server via RCON

#### Setup:

- Run `setup.py` to generate a config file, your bot's token can be obtained at the Discord developer portal
- Run `python3 bot.py` to start the bot

#### Commands:

- `!rcon <command>` executes a command via RCON
- `!whitelist <username>` whitelists the user 'username'
- `!unwhitelist <username>` removes 'username' from the whitelist
- `!purgeuser <username>` forcefully purges 'username' from both the whitelist database and attempts to remove from the server whitelist too, regardless of whether the database purge worked