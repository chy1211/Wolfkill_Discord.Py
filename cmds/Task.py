import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import json
from datetime import datetime

dc = discord


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0
        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(860765201275158578)
        #     while not self.bot.is_closed():
        #         await self.channel.send("Hi I'm still running!")
        #         await asyncio.sleep(5)

        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(860765201275158578)
            while not self.bot.is_closed():
                now_time = datetime.now().strftime("%m%d %H:%M")
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                if now_time == jdata["TIME"] and self.counter == 0:
                    await self.channel.send(jdata["MSG"])
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def setchannel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"頻道更改為:{self.channel.mention}")

    @commands.command()
    async def settime(self, ctx, msg, *, time):
        self.counter = 0
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        jdata["TIME"] = time
        jdata["MSG"] = msg
        with open("settings.json", "w", encoding="utf8") as setjson:
            json.dump(jdata, setjson, indent=4)


def setup(bot):
    bot.add_cog(Task(bot))
