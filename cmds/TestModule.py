import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import json

with open("settings.json", "r", encoding="utf8") as setjson:
    jdata = json.load(setjson)
global squad
global votes
squad = jdata["SQUAD"]
EMOJI = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
votes = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

dc = discord


class TestModule(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    def votemember(len):
        msg = "```diff\n-投票\n"
        for i in range(int(len)):
            msg += f"{i+1}號 : {squad[i]} "
        msg += "```"
        return msg

    @commands.command()
    async def showvote(self, ctx, len):
        i = 1
        msg = await ctx.send(TestModule.votemember(len))
        for emoji in EMOJI:
            if i <= int(len):
                await msg.add_reaction(emoji)
                i += 1
            else:
                break
        message = await ctx.send("投票倒數 : 10 秒")
        for i in range(9, 0, -1):
            await asyncio.sleep(1)
            await message.edit(content=f"投票倒數 : {i} 秒")
        await asyncio.sleep(1)
        await message.edit(content=f"淘汰者為`{squad[votes.index(max(votes))]}`")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if str(data.emoji) == "1️⃣":
            votes[0] += 1
        elif str(data.emoji) == "2️⃣":
            votes[1] += 1
        elif str(data.emoji) == "3️⃣":
            votes[2] += 1
        elif str(data.emoji) == "4️⃣":
            votes[3] += 1
        elif str(data.emoji) == "5️⃣":
            votes[4] += 1
        elif str(data.emoji) == "6️⃣":
            votes[5] += 1
        elif str(data.emoji) == "7️⃣":
            votes[6] += 1
        elif str(data.emoji) == "8️⃣":
            votes[7] += 1
        elif str(data.emoji) == "9️⃣":
            votes[8] += 1
        else:
            votes[9] += 1

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if str(data.emoji) == "1️⃣":
            votes[0] -= 1
        elif str(data.emoji) == "2️⃣":
            votes[1] -= 1
        elif str(data.emoji) == "3️⃣":
            votes[2] -= 1
        elif str(data.emoji) == "4️⃣":
            votes[3] -= 1
        elif str(data.emoji) == "5️⃣":
            votes[4] -= 1
        elif str(data.emoji) == "6️⃣":
            votes[5] -= 1
        elif str(data.emoji) == "7️⃣":
            votes[6] -= 1
        elif str(data.emoji) == "8️⃣":
            votes[7] -= 1
        elif str(data.emoji) == "9️⃣":
            votes[8] -= 1
        else:
            votes[9] -= 1

    @commands.command()
    async def testdef(self, ctx, len):
        votemember = TestModule.votemember(len)
        await ctx.send(votemember)


def setup(bot):
    bot.add_cog(TestModule(bot))
