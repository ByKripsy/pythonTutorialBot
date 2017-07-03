import asyncio as asyncio
import discord
from discord import Game, Server, Member, Embed

import SECRETS
from commands import cmd_ping, STATICS

client = discord.Client()


commands = {

    "ping": cmd_ping,

}


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="This is just for tutorial purposes!"))


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(args, message, client, invoke)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=("The command `%s` is not valid!" % invoke)))




client.run(SECRETS.TOKEN)