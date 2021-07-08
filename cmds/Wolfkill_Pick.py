import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

dc = discord


class Wolfkill_Pick(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # list info = 狼王,狼人,預言家,女巫,獵人,騎士,平民,總玩家數
    async def setgame(self, ctx):  # 設定遊戲配置
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        info = jdata["GAMEINFO"]
        await ctx.send("開始設定狼人殺!")
        await ctx.send("請輸入狼王數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[0] = int(respone.content)
        await ctx.send("請輸入狼人數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[1] = int(respone.content)
        await ctx.send("請輸入預言家數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[2] = int(respone.content)
        await ctx.send("請輸入女巫數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[3] = int(respone.content)
        await ctx.send("請輸入獵人數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[4] = int(respone.content)
        await ctx.send("請輸入騎士數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[5] = int(respone.content)
        await ctx.send("請輸入平民數量!")
        respone = await self.bot.wait_for("message", check=None)
        info[6] = int(respone.content)
        total = 0
        for i in range(7):
            total += info[i]
        info[7] = total
        embed = discord.Embed(title=f"本局共有{info[7]}位玩家")
        embed.add_field(name="狼王", value=f"{info[0]}位玩家", inline=True)
        embed.add_field(name="狼人", value=f"{info[1]}位玩家", inline=True)
        embed.add_field(name="預言家", value=f"{info[2]}位玩家", inline=True)
        embed.add_field(name="女巫", value=f"{info[3]}位玩家", inline=True)
        embed.add_field(name="獵人", value=f"{info[4]}位玩家", inline=True)
        embed.add_field(name="騎士", value=f"{info[5]}位玩家", inline=True)
        embed.add_field(name="平民", value=f"{info[6]}位玩家", inline=True)
        await ctx.send(embed=embed)
        jdata["SQUAD"] = []
        jdata["GAMEINFO"] = info
        with open("settings.json", "w", encoding="utf8") as setjson:
            json.dump(jdata, setjson, indent=4)

    @commands.command()
    async def showgameinfo(self, ctx):  # 顯示此局配置
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        info = jdata["GAMEINFO"]
        embed = discord.Embed(title=f"本局共有{info[7]}位玩家")
        embed.add_field(name="狼王", value=f"{info[0]}位玩家", inline=True)
        embed.add_field(name="狼人", value=f"{info[1]}位玩家", inline=True)
        embed.add_field(name="預言家", value=f"{info[2]}位玩家", inline=True)
        embed.add_field(name="女巫", value=f"{info[3]}位玩家", inline=True)
        embed.add_field(name="獵人", value=f"{info[4]}位玩家", inline=True)
        embed.add_field(name="騎士", value=f"{info[5]}位玩家", inline=True)
        embed.add_field(name="平民", value=f"{info[6]}位玩家", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def addplayer(self, ctx, name):  # 新增玩家
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        squad = jdata["SQUAD"]
        count = 0
        for member in ctx.guild.members:
            if member.name == name:
                if member.bot is False:
                    await ctx.send(f"玩家 `{member.name}` 已加入隊列")
                    squad.append(member.name)
                    jdata["SQUAD"] = squad
                    with open("settings.json", "w", encoding="utf8") as setjson:
                        json.dump(jdata, setjson, indent=4)
                else:
                    await ctx.send("請勿將機器人加入隊列!")
            elif member.nick == name:
                if member.bot is False:
                    await ctx.send(f"玩家 `{member.nick}` 已加入隊列")
                    squad.append(member.name)
                    jdata["SQUAD"] = squad
                    with open("settings.json", "w", encoding="utf8") as setjson:
                        json.dump(jdata, setjson, indent=4)
                else:
                    await ctx.send("請勿將機器人加入隊列!")
            else:
                count += 1
        if count == len(ctx.guild.members):
            await ctx.send("找不到此ID,請確認是否輸入正確")

    @commands.command()
    async def showsquad(self, ctx):  # 顯示隊列
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        squad = jdata["SQUAD"]
        await ctx.send(squad)
        await ctx.send(type(squad))

    @commands.command()
    async def cleansquad(self, ctx):  # 清理隊列
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        jdata["SQUAD"] = []
        with open("settings.json", "w", encoding="utf8") as setjson:
            json.dump(jdata, setjson, indent=4)
        await ctx.send("隊列已清理完成")

    def choose_identity(key):
        if key == "WOLFKING":  # 崁入訊息選擇
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="狼王", inline=True)
            embed.set_image(url="https://i.imgur.com/7SK5QZD.png")
            return embed
        elif key == "WOLF":
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="狼人", inline=True)
            embed.set_image(url="https://i.imgur.com/fEwH92m.png")
            return embed
        elif key == "PROPHET":
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="預言家", inline=True)
            embed.set_image(url="https://i.imgur.com/4Cf3oQV.png")
            return embed
        elif key == "WITCH":
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="女巫", inline=True)
            embed.set_image(url="https://i.imgur.com/DVmJmER.png")
            return embed
        elif key == "HUNTER":
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="獵人", inline=True)
            embed.set_image(url="https://i.imgur.com/bJm7VzN.png")
            return embed
        elif key == "KNIGHT":
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="騎士", inline=True)
            embed.set_image(url="https://i.imgur.com/P5nGc9d.png")
            return embed
        elif key == "CIVILIAN":
            embed = discord.Embed(title="狼人殺", color=0xFF0000)
            embed.add_field(name="您這局的身分是", value="平民", inline=True)
            embed.set_image(url="https://i.imgur.com/7BRBmMB.png")
            return embed

    @commands.command()
    async def pickteam(self, ctx):  # 抽選身分
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        config = jdata["CONFIG"]
        dfcon = jdata["DEFAULTCONFIG"]
        info = jdata["GAMEINFO"]
        disable = []
        squad = jdata["SQUAD"]
        squad_team = jdata["SQUAD_TEAM_DF"]
        len = 0
        i = 0
        for j in info:
            if j != 0:
                i += 1
                len += 1
            else:
                disable.append(i)
                i += 1
        count = 0
        for i in disable:
            rm = i - count
            info.pop(rm)
            config.pop(rm)
            count += 1
        for i in range(7):
            if dfcon[i] not in config:
                del squad_team[f"{dfcon[i]}"]
        for i in range(len - 1):
            name = random.sample(squad, k=info[i])
            squad_team[f"{config[i]}"] = name
            # print(f"{config[i]}:" + str(name)) <-debug code
            for r in name:
                squad.remove(r)
        setjson.close()
        with open("settings.json", "r", encoding="utf8") as setjson:
            jdata = json.load(setjson)
        jdata["SQUAD_TEAM"] = squad_team
        for key, value in squad_team.items():
            for i in value:
                for member in ctx.guild.members:
                    if str(member).startswith(str(i)):
                        await member.send(embed=Wolfkill_Pick.choose_identity(key))
        with open("settings.json", "w", encoding="utf8") as setjson:
            json.dump(jdata, setjson, indent=4)
        await ctx.send("身分抽選完成!")


def setup(bot):
    bot.add_cog(Wolfkill_Pick(bot))
