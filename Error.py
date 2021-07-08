import discord
from discord.ext import commands
from core.classes import Cog_Extension

dc = discord


class Error(Cog_Extension):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("參數錯誤!")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("指令輸入錯誤，沒有這個指令!")

        elif "403 Forbidden" in str(error):
            await ctx.send("403 Forbidden，請檢查 Bot 權限!")

        else:
            await ctx.send("發生未知錯誤!")


def setup(bot):
    bot.add_cog(Error(bot))
