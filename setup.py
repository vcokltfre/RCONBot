from pathlib import Path

items = {
    "TOKEN": "Enter your bot's token: ",
    "RCON_ADDR": "Enter your server's address: ",
    "RCON_PASS": "Enter your server's RCON password: ",
    "RCON_PORT": "Enter your server's RCON port [25575]: ",
    "ADMIN_ROLES": "Enter the name of your admin role on Discord: ",
    "WHITELIST_LIMIT": "Enter the amount of accounts a user can whitelist: "
}

for key in items:
    items[key] = input(items[key])

data = f"""
TOKEN = "{items['TOKEN']}"
RCON_ADDR = "{items['RCON_ADDR']}"
RCON_PASS = "{items['RCON_PASS']}"
RCON_PORT = {items['RCON_PORT']}
ADMIN_ROLES = ["{items['ADMIN_ROLES']}"]
BYPASS_ROLES = []
WHITELIST_LIMIT = {items['WHITELIST_LIMIT']}
"""

path = Path("config/")
path.mkdir(parents=True)
path = Path("config/config.py")
with path.open("w") as f:
    f.write(data)