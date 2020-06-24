import discord
from getLyrics import searchFor
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "!")
token = os.environ["TOKEN"]
@bot.event
async def on_ready():
    print("Bot is ready")

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send(f'{message.author.mention} Hello!')

@bot.command()
async def getlyrics(ctx, *, args):
    print(args)
    message = await ctx.send(f"Processing {ctx.author}'s request..")
    result = searchFor(args)
    output = f"{ctx.author.mention}\n```{result}```"
    await message.edit(content=output)

bot.run('NzI0MTQzMTY3MzgwNzgzMTA1.Xu75Kw.Qp2sbrlUZa6NJg3wkb5ueriKRz0')
