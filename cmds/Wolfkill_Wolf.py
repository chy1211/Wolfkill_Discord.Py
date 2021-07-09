import asyncio
import discord
from discord.errors import NotFound
from discord.ext import commands
from core.classes import Cog_Extension
import json

dc = discord


class Wolfkill_Wolf(Cog_Extension):
    def indict():
        team = []
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        squad_team = jdata["SQUAD_TEAM"]
        for key, value in squad_team.items():
            for i in value:
                team.append(i)
        setjson.close()
        return team

    def writedownkill(id):
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        if Wolfkill_Wolf.indict(id):
            status["WOLFKILL"] = id
            with open("settings.json", "w", encoding="utf8") as setjson:
                json.dump(jdata, setjson, indent=4)
            return id
        else:
            return None

    @commands.command()
    async def goodnight(self, ctx):
        await ctx.send("天黑請閉眼")
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        status["DAWN"] = False
        with open("settings.json", "w", encoding="utf8") as setjson:
            json.dump(jdata, setjson, indent=4)
        for channels in ctx.guild.channels:
            if str(channels) == "你是狼人":
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                dict = jdata["SQUAD_TEAM"]
                wolf = dict["WOLFKING"] + dict["WOLF"]
                status = jdata["STATUS"]
                for i in wolf:
                    for member in ctx.guild.members:
                        if str(member).startswith(str(i)):
                            await channels.set_permissions(
                                member, read_messages=True, send_messages=True
                            )
                status["WOLFCOUNT"] = True
                with open("settings.json", "w", encoding="utf8") as setjson:
                    json.dump(jdata, setjson, indent=4)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def wolf_count():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(862528674385494017)
            self.guild = self.bot.get_guild(860455839201361960)
            while not self.bot.is_closed():
                await asyncio.sleep(1)
                with open("settings.json", "r", encoding="utf8") as setjson:
                    jdata = json.load(setjson)
                status = jdata["STATUS"]
                await asyncio.sleep(1)
                if status["WOLFCOUNT"] is True:
                    setjson.close()
                    msg = await self.channel.send("討論倒數 : 10 秒")
                    for i in range(9, 0, -1):  # 討論時間
                        await asyncio.sleep(0.9)
                        try:
                            await msg.edit(content=f"討論倒數 : {i} 秒")
                        except NotFound:
                            pass
                        finally:
                            pass
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    status = jdata["STATUS"]
                    if status["WOLFCOUNT"] is True:
                        status["WOLFCOUNT"] = False
                        with open("settings.json", "w", encoding="utf8") as setjson:
                            json.dump(jdata, setjson, indent=4)
                        await self.channel.send("本回合殺了 {玩家}")
                        await self.channel.send("狼人請閉眼")
                        await asyncio.sleep(3)
                        await self.channel.purge()
                        with open("settings.json", "r", encoding="utf8") as setjson:
                            jdata = json.load(setjson)
                        dict = jdata["SQUAD_TEAM"]
                        wolf = dict["WOLFKING"] + dict["WOLF"]
                        for i in wolf:
                            for member in self.guild.members:
                                if str(member).startswith(str(i)):
                                    await self.channel.set_permissions(
                                        member,
                                        read_messages=False,
                                        send_messages=False,
                                    )
                        setjson.close()
                        for channels in self.guild.channels:
                            if str(channels) == "你是女巫":
                                with open(
                                    "settings.json", "r", encoding="utf8"
                                ) as setjson:
                                    jdata = json.load(setjson)
                                dict = jdata["SQUAD_TEAM"]
                                witch = dict["WITCH"]
                                if len(witch):
                                    for i in witch:
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
                                    status["WITCHCOUNT"] = True
                                    with open(
                                        "settings.json", "w", encoding="utf8"
                                    ) as setjson:
                                        json.dump(jdata, setjson, indent=4)
                                else:
                                    print("跳到預言家")
                                    for channels in self.guild.channels:
                                        if str(channels) == "你是預言家":
                                            with open(
                                                "settings.json", "r", encoding="utf8"
                                            ) as setjson:
                                                jdata = json.load(setjson)
                                            dict = jdata["SQUAD_TEAM"]
                                            prohert = dict["PROPHET"]
                                            if len(prohert):
                                                for i in witch:
                                                    for member in self.guild.members:
                                                        if str(member).startswith(
                                                            str(i)
                                                        ):
                                                            await channels.set_permissions(
                                                                member,
                                                                read_messages=True,
                                                                send_messages=True,
                                                            )
                                                setjson.close()
                                            else:
                                                print("跳到天亮")
                                                with open(
                                                    "settings.json",
                                                    "r",
                                                    encoding="utf8",
                                                ) as setjson:
                                                    jdata = json.load(setjson)
                                                status = jdata["STATUS"]
                                                status["DAWN"] = True
                                                status["COUNTER"] = 0
                                                with open(
                                                    "settings.json",
                                                    "w",
                                                    encoding="utf8",
                                                ) as setjson:
                                                    json.dump(jdata, setjson, indent=4)
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

        self.bg_task = self.bot.loop.create_task(wolf_count())

    # @commands.command()
    # async def kill(self, ctx, id):
    #     with open("settings.json", "r", encoding="utf8") as setjson:
    #         jdata = json.load(setjson)
    #     dict = jdata["SQUAD_TEAM"]
    #     wolf = dict["WOLFKING"] + dict["WOLF"]
    #     if str(ctx.message.author.name) in wolf:
    #         if Wolfkill_Wolf.writedownkill(id) is not None:
    #             status = jdata["STATUS"]
    #             status["WOLFCOUNT"] = False
    #             with open("settings.json", "w", encoding="utf8") as setjson:
    #                 json.dump(jdata, setjson, indent=4)
    #             await ctx.send(f"本回合殺了{id}")
    #             await ctx.send("狼人請閉眼")
    #             await asyncio.sleep(3)
    #             await ctx.channel.purge()
    #             for channels in ctx.guild.channels:
    #                 if str(channels) == "你是狼人":
    #                     with open("settings.json", "r", encoding="utf8") as setjson:
    #                         jdata = json.load(setjson)
    #                     dict = jdata["SQUAD_TEAM"]
    #                     wolf = dict["WOLFKING"] + dict["WOLF"]
    #                     for i in wolf:
    #                         for member in ctx.guild.members:
    #                             if str(member).startswith(str(i)):
    #                                 await channels.set_permissions(
    #                                     member, read_messages=False, send_messages=False
    #                                 )
    #                     setjson.close()
    #             for channels in ctx.guild.channels:
    #                 if str(channels) == "你是女巫":
    #                     with open("settings.json", "r", encoding="utf8") as setjson:
    #                         jdata = json.load(setjson)
    #                     dict = jdata["SQUAD_TEAM"]
    #                     witch = dict["WITCH"]
    #                     if len(witch):
    #                         for i in witch:
    #                             for member in ctx.guild.members:
    #                                 if str(member).startswith(str(i)):
    #                                     await channels.set_permissions(
    #                                         member,
    #                                         read_messages=True,
    #                                         send_messages=True,
    #                                     )
    #                         setjson.close()
    #                     else:
    #                         for channels in ctx.guild.channels:
    #                             if str(channels) == "你是預言家":
    #                                 with open(
    #                                     "settings.json", "r", encoding="utf8"
    #                                 ) as setjson:
    #                                     jdata = json.load(setjson)
    #                                 dict = jdata["SQUAD_TEAM"]
    #                                 prohert = dict["PROPHET"]
    #                                 if len(prohert):
    #                                     for i in witch:
    #                                         for member in ctx.guild.members:
    #                                             if str(member).startswith(str(i)):
    #                                                 await channels.set_permissions(
    #                                                     member,
    #                                                     read_messages=True,
    #                                                     send_messages=True,
    #                                                 )
    #                                     setjson.close()
    #                                     with open(
    #                                         "settings.json", "r", encoding="utf8"
    #                                     ) as setjson:
    #                                         jdata = json.load(setjson)
    #                                     status = jdata["STATUS"]
    #                                     status["WITCHCOUNT"] = True
    #                                     with open(
    #                                         "settings.json", "w", encoding="utf8"
    #                                     ) as setjson:
    #                                         json.dump(jdata, setjson, indent=4)
    #                                 else:
    #                                     print("跳到天亮")
    #                                     with open(
    #                                         "settings.json",
    #                                         "r",
    #                                         encoding="utf8",
    #                                     ) as setjson:
    #                                         jdata = json.load(setjson)
    #                                     status = jdata["STATUS"]
    #                                     status["DAWN"] = True
    #                                     status["COUNTER"] = 0
    #                                     with open(
    #                                         "settings.json",
    #                                         "w",
    #                                         encoding="utf8",
    #                                     ) as setjson:
    #                                         json.dump(jdata, setjson, indent=4)  # 接續天亮
    #                         with open("settings.json", "r", encoding="utf8") as setjson:
    #                             jdata = json.load(setjson)
    #                         status = jdata["STATUS"]
    #                         status["PROHERTCOUNT"] = True
    #                         with open("settings.json", "w", encoding="utf8") as setjson:
    #                             json.dump(jdata, setjson, indent=4)
    #         else:
    #             await ctx.send(f"找不到{id}")
    #     else:
    #         await ctx.send("您無法使用此指令!")


def setup(bot):
    bot.add_cog(Wolfkill_Wolf(bot))
