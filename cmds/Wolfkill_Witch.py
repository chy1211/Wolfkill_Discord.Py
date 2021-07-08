import asyncio
import discord
from discord.errors import NotFound
from discord.ext import commands
from core.classes import Cog_Extension
import json

dc = discord


class Wolfkill_Witch(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def witch_count():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(862608140885688330)
            self.guild = self.bot.get_guild(860455839201361960)
            while not self.bot.is_closed():
                await asyncio.sleep(1)
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                status = jdata["STATUS"]
                await asyncio.sleep(1)
                if status["WITCHCOUNT"] is True:
                    if status["WITCHPOISON"] and status["WITCHANTIDOTE"]:
                        setjson.close()
                        await self.channel.send("{玩家}被殺了,你要救嗎?")
                        await self.channel.send("你要毒誰嗎")
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
                        if status["WITCHCOUNT"] is True:
                            status["WITCHCOUNT"] = False
                            with open("settings.json", "w", encoding="utf8") as setjson:
                                json.dump(jdata, setjson, indent=4)
                            await self.channel.send("本回合沒做任何動作")
                            await self.channel.send("女巫請閉眼")
                            await asyncio.sleep(3)
                            await self.channel.purge()
                    elif (
                        status["WITCHPOISON"] is False
                        and status["WITCHANTIDOTE"] is True
                    ):
                        setjson.close()
                        await self.channel.send("{玩家}被殺了,你要救嗎?")
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
                        if status["WITCHCOUNT"] is True:
                            status["WITCHCOUNT"] = False
                            with open("settings.json", "w", encoding="utf8") as setjson:
                                json.dump(jdata, setjson, indent=4)
                            await self.channel.send("本回合沒做任何動作")
                            await self.channel.send("女巫請閉眼")
                            await asyncio.sleep(3)
                            await self.channel.purge()
                    elif (
                        status["WITCHPOISON"] is True
                        and status["WITCHANTIDOTE"] is False
                    ):
                        setjson.close()
                        await self.channel.send("你要毒誰嗎")
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
                        if status["WITCHCOUNT"] is True:
                            status["WITCHCOUNT"] = False
                            with open("settings.json", "w", encoding="utf8") as setjson:
                                json.dump(jdata, setjson, indent=4)
                            await self.channel.send("本回合沒做任何動作")
                            await self.channel.send("女巫請閉眼")
                            await asyncio.sleep(3)
                            await self.channel.purge()
                    else:
                        setjson.close()
                        await self.channel.send("您手上沒有任何藥劑,無法做任何動作!")
                        msg = await self.channel.send("將在 10 秒 後繼續")
                        for i in range(9, 0, -1):  # 思考時間
                            await asyncio.sleep(0.9)
                            try:
                                await msg.edit(content=f"將在 {i} 秒 後繼續")
                            except NotFound:
                                pass
                            finally:
                                pass
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                            status = jdata["STATUS"]
                        if status["WITCHCOUNT"] is True:
                            status["WITCHCOUNT"] = False
                            with open("settings.json", "w", encoding="utf8") as setjson:
                                json.dump(jdata, setjson, indent=4)
                            await self.channel.send("本回合沒做任何動作")
                            await self.channel.send("女巫請閉眼")
                            await asyncio.sleep(3)
                            await self.channel.purge()
                    for channels in self.guild.channels:
                        if str(channels) == "你是女巫":
                            with open("settings.json", "r", encoding="utf8") as setjson:
                                jdata = json.load(setjson)
                            dict = jdata["SQUAD_TEAM"]
                            witch = dict["WITCH"]
                            for i in witch:
                                for member in self.guild.members:
                                    if str(member).startswith(str(i)):
                                        await channels.set_permissions(
                                            member,
                                            read_messages=False,
                                            send_messages=False,
                                        )
                            setjson.close()
                    for channels in self.guild.channels:
                        if str(channels) == "你是預言家":
                            with open("settings.json", "r", encoding="utf8") as setjson:
                                jdata = json.load(setjson)
                            dict = jdata["SQUAD_TEAM"]
                            prohert = dict["PROPHET"]
                            if len(prohert):
                                for i in prohert:
                                    for member in self.guild.members:
                                        if str(member).startswith(str(i)):
                                            await channels.set_permissions(
                                                member,
                                                read_messages=True,
                                                send_messages=True,
                                            )
                                setjson.close()
                                with open(
                                    "settings.json", "r", encoding="utf8"
                                ) as setjson:
                                    jdata = json.load(setjson)
                                status = jdata["STATUS"]
                                status["PROHERTCOUNT"] = True
                                with open(
                                    "settings.json", "w", encoding="utf8"
                                ) as setjson:
                                    json.dump(jdata, setjson, indent=4)
                            else:
                                print("跳到天亮")
                                with open(
                                    "settings.json", "r", encoding="utf8"
                                ) as setjson:
                                    jdata = json.load(setjson)
                                status = jdata["STATUS"]
                                status["DAWN"] = True
                                status["COUNTER"] = 0
                                with open(
                                    "settings.json", "w", encoding="utf8"
                                ) as setjson:
                                    json.dump(jdata, setjson, indent=4)

        self.bg_task = self.bot.loop.create_task(witch_count())

    @commands.command()
    async def wkill(self, ctx, id):
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        if status["WITCHPOISON"] is True:
            status["WITCHCOUNT"] = False
            with open("settings.json", "w", encoding="utf8") as setjson:
                json.dump(jdata, setjson, indent=4)
            await ctx.send(f"本回合毒殺了殺了{id}")  # 毒殺
            await ctx.send("女巫請閉眼")
            await asyncio.sleep(3)
            await ctx.channel.purge()
            for channels in ctx.guild.channels:
                if str(channels) == "你是女巫":
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    dict = jdata["SQUAD_TEAM"]
                    witch = dict["WITCH"]
                    for i in witch:
                        for member in ctx.guild.members:
                            if str(member).startswith(str(i)):
                                await channels.set_permissions(
                                    member, read_messages=False, send_messages=False
                                )
                    setjson.close()
            for channels in ctx.guild.channels:
                if str(channels) == "你是預言家":
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    dict = jdata["SQUAD_TEAM"]
                    prohert = dict["PROPHET"]
                    if len(prohert):
                        for i in prohert:
                            for member in ctx.guild.members:
                                if str(member).startswith(str(i)):
                                    await channels.set_permissions(
                                        member, read_messages=True, send_messages=True
                                    )
                        setjson.close()
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                        status = jdata["STATUS"]
                        status["PROHERTCOUNT"] = True
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)
                    else:
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                        status = jdata["STATUS"]
                        status["DAWN"] = True
                        status["COUNTER"] = 0
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)

        else:
            await ctx.send("您沒有毒藥,無法毒殺!")

    @commands.command()
    async def save(self, ctx, id):
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        if status["WITCHANTIDOTE"] is True:
            status["WITCHCOUNT"] = False
            with open("settings.json", "w", encoding="utf8") as setjson:
                json.dump(jdata, setjson, indent=4)
            await ctx.send(f"本回合將{id}救了起來!")  # 解救
            await ctx.send("女巫請閉眼")
            await asyncio.sleep(3)
            await ctx.channel.purge()
            for channels in ctx.guild.channels:
                if str(channels) == "你是女巫":
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    dict = jdata["SQUAD_TEAM"]
                    witch = dict["WITCH"]
                    for i in witch:
                        for member in ctx.guild.members:
                            if str(member).startswith(str(i)):
                                await channels.set_permissions(
                                    member, read_messages=False, send_messages=False
                                )
                    setjson.close()
            for channels in ctx.guild.channels:
                if str(channels) == "你是預言家":
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    dict = jdata["SQUAD_TEAM"]
                    prohert = dict["PROPHET"]
                    if len(prohert):
                        for i in prohert:
                            for member in ctx.guild.members:
                                if str(member).startswith(str(i)):
                                    await channels.set_permissions(
                                        member, read_messages=True, send_messages=True
                                    )
                        setjson.close()
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                        status = jdata["STATUS"]
                        status["PROHERTCOUNT"] = True
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)
                    else:
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                        status = jdata["STATUS"]
                        status["DAWN"] = True
                        status["COUNTER"] = 0
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)

        else:
            await ctx.send("您沒有解藥,無法救人!")


def setup(bot):
    bot.add_cog(Wolfkill_Witch(bot))
