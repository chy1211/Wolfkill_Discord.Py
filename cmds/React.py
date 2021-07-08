import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

dc = discord

with open("settings.json", "r", encoding="utf8") as setjson:
    jdata = json.load(setjson)


class React(Cog_Extension):
    @commands.command()
    async def logo(self, ctx):
        img = jdata["img_logo"]
        await ctx.send(img)

    @commands.command()
    async def test(self, ctx):
        await ctx.send("testing!")


def setup(bot):
    bot.add_cog(React(bot))
