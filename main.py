import discord
import asyncio

from discord import Game

import SECRETS
import STATICS
from commands import ping

client = discord.Client()

# Später hinzufügen, wenn der Command Parser gecoded wird
commands = {

    "ping": ping,

}


@client.event
@asyncio.coroutine
def on_ready():

    print("\nRunning on %s servers:" % len(client.servers))
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    print("------------------------")

    yield from client.change_presence(game=Game(name="THIS BOT IS RUNNING FOR TUTORIAL RECORDING"))


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith("."):
        invoke = message.content[1:].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(message, args, client)
        else:
            yield from client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Command \"%s%s\" does not exist!" % (STATICS.PREFIX, invoke))))


client.run(SECRETS.TOKEN)