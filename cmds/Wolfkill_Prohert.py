import asyncio
import discord
from discord.errors import NotFound
from discord.ext import commands
from core.classes import Cog_Extension
import json

dc = discord


class Wolfkill_Prohert(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def witch_count():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(862608218009370624)
            self.guild = self.bot.get_guild(860455839201361960)
            while not self.bot.is_closed():
                await asyncio.sleep(1)
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                status = jdata["STATUS"]
                await asyncio.sleep(1)
                if status["PROHERTCOUNT"] is True:
                    setjson.close()
                    await self.channel.send("你要查驗誰?")
                    msg = await self.channel.send("思考時間倒數 : 10 秒")
                    for i in range(9, 0, -1):  # 思考時間
                        await asyncio.sleep(0.9)
                        try:
                            await msg.edit(content=f"思考時間倒數 : {i} 秒")
                        except NotFound:
                            pass
                        finally:
                            pass
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                        status = jdata["STATUS"]
                    if status["PROHERTCOUNT"] is True:
                        status["PROHERTCOUNT"] = False
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)
                        await self.channel.send("本回合沒做任何動作")
                        await self.channel.send("預言家請閉眼")
                        await asyncio.sleep(3)
                        await self.channel.purge()
                    for channels in self.guild.channels:
                        if str(channels) == "你是預言家":
                            with open("settings.json", "r", encoding="utf8") as setjson:
                                jdata = json.load(setjson)
                            dict = jdata["SQUAD_TEAM"]
                            prohert = dict["PROPHET"]
                            for i in prohert:
                                for member in self.guild.members:
                                    if str(member).startswith(str(i)):
                                        await channels.set_permissions(
                                            member,
                                            read_messages=False,
                                            send_messages=False,
                                        )
                            setjson.close()
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                        status = jdata["STATUS"]
                        status["DAWN"] = True
                        status["COUNTER"] = 0
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)

        self.bg_task = self.bot.loop.create_task(witch_count())

    @commands.command()
    async def Check(self, ctx, id):
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        status["PROHERTCOUNT"] = False
        with open("settings.json", "w", encoding="utf8") as setjson:
            json.dump(jdata, setjson, indent=4)
        await ctx.send("查驗目標為:{玩家},他是好/壞人")  # 查驗
        await ctx.send("預言家請閉眼")
        await asyncio.sleep(3)
        await ctx.channel.purge()
        for channels in ctx.guild.channels:
            if str(channels) == "你是預言家":
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                dict = jdata["SQUAD_TEAM"]
                prohert = dict["PROPHET"]
                for i in prohert:
                    for member in ctx.guild.members:
                        if str(member).startswith(str(i)):
                            await channels.set_permissions(
                                member, read_messages=False, send_messages=False
                            )
                setjson.close()
            with open("settings.json", "r", encoding="utf8") as setjson:
                jdata = json.load(setjson)
            status = jdata["STATUS"]
            status["DAWN"] = True
            status["COUNTER"] = 0
            with open("settings.json", "w", encoding="utf8") as setjson:
                json.dump(jdata, setjson, indent=4)


def setup(bot):
    bot.add_cog(Wolfkill_Prohert(bot))
