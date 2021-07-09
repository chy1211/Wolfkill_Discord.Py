import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.all()
dc = discord

with open("settings.json", "r", encoding="utf8") as setjson:
    jdata = json.load(setjson)

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot 載入完成!")
    print("Bot 現在正在線上")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"模組 `{extension}` 載入完成!!")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"模組 `{extension}` 已取消載入!!")


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"模組 `{extension}` 已重新載入!!")


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        print(f"載入中,正在讀取{filename}")
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
