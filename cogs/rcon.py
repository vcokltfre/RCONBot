# -*- coding: utf-8 -*-

from discord import colour
from discord.ext import commands
import discord
from mcrcon import MCRcon

from config.config import RCON_PASS, RCON_ADDR, RCON_PORT, BYPASS_ROLES, ADMIN_ROLES


class RCON(commands.Cog):
    """Interface with a Minecraft server theorugh Discord with RCON"""

    def __init__(self, bot):
        self.bot = bot
        self.rcon = MCRcon(RCON_ADDR, RCON_PASS, RCON_PORT)
        self.rcon.connect()

    @commands.command(name="rcon")
    @commands.has_any_role(*ADMIN_ROLES)
    async def rcon_send(self, ctx, *command):
        command = " ".join(command)
        resp = self.rcon.command(command)

        embed = discord.Embed(title="RCON", description=f"Command: {command}", colour=0x0FFF0F)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        data = resp if resp else "No data was returned. This likely means the command succeeded."
        embed.add_field(name="Result", value=data)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(RCON(bot))
