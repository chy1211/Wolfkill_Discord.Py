import asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

dc = discord


class Wolfkill_Dawn(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def witch_count():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(860765201275158578)
            self.guild = self.bot.get_guild(860455839201361960)
            while not self.bot.is_closed():
                await asyncio.sleep(1)
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                status = jdata["STATUS"]
                await asyncio.sleep(1)
                if status["DAWN"] is True and status["COUNTER"] == 0:
                    setjson.close()
                    await self.channel.send("天亮了,{玩家}被殺了!")
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    status = jdata["STATUS"]
                    status["COUNTER"] = 1
                    with open("settings.json", "w", encoding="utf8") as setjson:
                        json.dump(jdata, setjson, indent=4)

        self.bg_task = self.bot.loop.create_task(witch_count())

    @commands.command()
    async def collision(self, ctx, id):
        await ctx.send(f"{ctx.message.author.name}衝撞了{id}")


def setup(bot):
    bot.add_cog(Wolfkill_Dawn(bot))
