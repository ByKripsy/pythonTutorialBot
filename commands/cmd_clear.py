import discord
import asyncio


async def ex(args, message, client, invoke):

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Please enter a valid number as message count!"))
        return

    failed = 0
    cleared = 0

    # Nur zur demonstartion dass das einen error throwt
    # await client.delete_messages(client.logs_from(message.channel, limit=ammount))
    # return

    async for m in client.logs_from(message.channel, limit=ammount):
        try:
            await client.delete_message(m)
            cleared += 1
        except:
            failed += 1
            pass

    failed_msg = "\n\nFailed to delete %s messages." % failed if failed > 0 else ""

    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_msg)))
    await asyncio.sleep(4)
    await client.delete_message(returnmsg)
