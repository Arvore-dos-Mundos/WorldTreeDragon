import discord
import json
import os
from discord.ext.commands import Bot

with open("config.json") as f:
    configData = json.load(f)

client = Bot(command_prefix= "!", intents = discord.Intents.all())

for filename in os.listdir("./commands"):
    if filename.endswith(".py") and not filename.startswith("__"):
        client.load_extension("commands.{0}".format(filename[:-3]))

client.run(configData["token"])