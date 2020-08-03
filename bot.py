import discord
from discord.ext import commands

from config.config import TOKEN


class Bot(commands.Bot):
    """A subclassed version of commands.Bot to add functionality"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_cog(self, cog: commands.Cog) -> None:
        """Adds a cog to the bot and logs it."""
        super().add_cog(cog)

    def load_extensions(self, cogs: list):
        """Loads a list of cogs"""
        for cog in cogs:
            try:
                super().load_extension(cog)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    bot = Bot(
        command_prefix="!",
        help_command=commands.MinimalHelpCommand()
    )

    cogs = ["cogs.rcon"]

    bot.load_extensions(cogs)
    bot.run(TOKEN)