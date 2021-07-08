from asyncio.windows_events import NULL
import json

with open("settings.json", "r", encoding="utf8") as setjson:
    jdata = json.load(setjson)
dict = jdata["SQUAD_TEAM"]
prohert = dict["PROPHET"]

print(prohert)

print(prohert != NULL)

if len(prohert):
    print("T")
else:
    print("F")

print(type(prohert))
