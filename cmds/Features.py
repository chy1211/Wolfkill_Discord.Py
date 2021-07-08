import discord
from discord.ext import commands
from core.classes import Cog_Extension

dc = discord


class Features(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1)


def setup(bot):
    bot.add_cog(Features(bot))
