import discord
from discord.ext import commands
from core.classes import Cog_Extension

dc = discord


class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # ping指令
    async def ping(self, ctx):
        await ctx.send(f"現在延遲 {round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def hi(self, ctx):  # hi指令
        await ctx.send("Hi!")

    @commands.command()  # embed
    async def about(self, ctx):
        embed = dc.Embed(
            title="About this bot",
            description="This is a bot create for practice",
            color=0x66D1F4,
        )  # timestamp=datetime.now() <- 時間戳記
        embed.set_author(
            name="PythonProgram",
            icon_url="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png",
        )
        embed.add_field(name="Main", value="主要指令", inline=True)
        embed.add_field(name="Event", value="事件觸發", inline=True)
        embed.add_field(name="React", value="回應", inline=True)
        embed.add_field(name="提示", value="你可以使用!help", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))
