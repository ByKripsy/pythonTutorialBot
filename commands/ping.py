import discord.client


def ex(message, args, client):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attached args: %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.send_message(message.channel, "Pong!" + args_out)