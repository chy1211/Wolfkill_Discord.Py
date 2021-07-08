import discord
from discord.ext import commands
from core.classes import Cog_Extension

dc = discord


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):  # 多關鍵字觸發
        keyword = ["keyword", "關鍵字", "關鍵字1", "關鍵字2"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("已觸發關鍵字!")


def setup(bot):
    bot.add_cog(Event(bot))
