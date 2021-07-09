import asyncio
import discord
from discord.errors import NotFound
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

dc = discord
global vote
vote = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
EMOJI = [
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣",
    "🔟",
    "🅰️",
    "🅱️",
    "🥇",
    "🥈",
    "🥉",
]


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

    def wolfvote():
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        info = jdata["GAMEINFO"]
        len = info[7]
        team = Wolfkill_Wolf.indict()
        inrandom = random.sample(team, k=len)
        msg = "```diff\n-要殺誰?\n"
        for i in range(int(len)):
            msg += f"{i+1}號 : {inrandom[i]} "
        msg += "```"
        re = []
        re.append(msg)
        re.append(inrandom)
        re.append(len)
        return re

    @commands.command()
    async def goodnight(self, ctx):
        vote = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        print(vote)
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
                    remsg = Wolfkill_Wolf.wolfvote()
                    reteam = remsg[1]
                    msgadd = await self.channel.send(remsg[0])
                    i = 1
                    for emoji in EMOJI:
                        if i <= int(remsg[2]):
                            await msgadd.add_reaction(emoji)
                            i += 1
                        else:
                            break
                    msg = await self.channel.send("討論倒數 : 10 秒")
                    for i in range(9, 0, -1):  # 討論時間
                        await asyncio.sleep(0.9)
                        try:
                            await msg.edit(content=f"討論倒數 : {i} 秒")
                        except NotFound:
                            pass
                        finally:
                            pass
                    await msg.edit(content=f"本局殺了`{reteam[vote.index(max(vote))]}`")
                    with open("settings.json", "r", encoding="utf8") as setjson:
                        jdata = json.load(setjson)
                    status = jdata["STATUS"]
                    status["WOLFKILL"] = str(reteam[vote.index(max(vote))])
                    status["WOLFCOUNT"] = False
                    with open("settings.json", "w", encoding="utf8") as setjson:
                        json.dump(jdata, setjson, indent=4)
                    await self.channel.send(
                        f"本回合殺了 {str(reteam[vote.index(max(vote))])}"
                    )
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
                            with open("settings.json", "r", encoding="utf8") as setjson:
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
                                                    if str(member).startswith(str(i)):
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

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        if status["DAWN"] is False:
            if str(data.emoji) == "1️⃣":
                vote[0] += 1
            elif str(data.emoji) == "2️⃣":
                vote[1] += 1
            elif str(data.emoji) == "3️⃣":
                vote[2] += 1
            elif str(data.emoji) == "4️⃣":
                vote[3] += 1
            elif str(data.emoji) == "5️⃣":
                vote[4] += 1
            elif str(data.emoji) == "6️⃣":
                vote[5] += 1
            elif str(data.emoji) == "7️⃣":
                vote[6] += 1
            elif str(data.emoji) == "8️⃣":
                vote[7] += 1
            elif str(data.emoji) == "9️⃣":
                vote[8] += 1
            elif str(data.emoji) == "🔟":
                vote[9] += 1
            elif str(data.emoji) == "🅰️":
                vote[10] += 1
            elif str(data.emoji) == "🅱️":
                vote[11] += 1
            elif str(data.emoji) == "🥇":
                vote[12] += 1
            elif str(data.emoji) == "🥈":
                vote[13] += 1
            else:
                vote[14] += 1

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        status = jdata["STATUS"]
        if status["DAWN"] is False:
            if str(data.emoji) == "1️⃣":
                vote[0] -= 1
            elif str(data.emoji) == "2️⃣":
                vote[1] -= 1
            elif str(data.emoji) == "3️⃣":
                vote[2] -= 1
            elif str(data.emoji) == "4️⃣":
                vote[3] -= 1
            elif str(data.emoji) == "5️⃣":
                vote[4] -= 1
            elif str(data.emoji) == "6️⃣":
                vote[5] -= 1
            elif str(data.emoji) == "7️⃣":
                vote[6] -= 1
            elif str(data.emoji) == "8️⃣":
                vote[7] -= 1
            elif str(data.emoji) == "9️⃣":
                vote[8] -= 1
            elif str(data.emoji) == "🔟":
                vote[9] -= 1
            elif str(data.emoji) == "🅰️":
                vote[10] -= 1
            elif str(data.emoji) == "🅱️":
                vote[11] -= 1
            elif str(data.emoji) == "🥇":
                vote[12] -= 1
            elif str(data.emoji) == "🥈":
                vote[13] -= 1
            else:
                vote[14] -= 1


def setup(bot):
    bot.add_cog(Wolfkill_Wolf(bot))
