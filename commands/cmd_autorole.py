import os
from os import path

import discord
from discord import Embed


def get(server):
    f = "SETTINGS/" + server.id + "/autorole"
    if path.isfile(f):
        with open(f) as f:
            return discord.utils.get(server.roles, id=f.read())
    else:
        return None


def safeFile(id, server):
    if not path.isdir("SETTINGS/" + server.id):
        os.makedirs("SETTINGS/" + server.id)
    with open("SETTINGS/" + server.id + "/autorole", "w") as fw:
        fw.write(id)
        fw.close()


def ex(message, args, client):

    if len(args) > 1:
        if args[0] == "add":
            rolename = args[1:].__str__()[1:-1].replace("'", "").replace(",", "")
            try:
                role = discord.utils.get(message.server.roles, name=rolename)
                safeFile(role.id, message.server)
                yield from client.send_message(message.channel, embed=Embed(color=discord.Color.green(), description=("Successfully set autorole to role `%s`." % role.name)))
            except:
                yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=("Role `%s` does not exist on this server!" % rolename)))
