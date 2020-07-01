import discord
from getLyrics import searchFor
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "!")
token = os.environ["TOKEN"]
@bot.event
async def on_ready():
    print("Bot is ready")

def greetings():
    hi = "Hi, how can I help you? I listen to the following command(s)"
    cmd = "```!getlyrics ArtistName-SongName - **to get the lyrics of the song**```"
    return hi+"\n"+cmd

@bot.command()
async def lyricia(ctx, *, args):
    await ctx.send(greetings())

@bot.command()
async def getlyrics(ctx, *, args):
    print(args)
    message = await ctx.send(f"```Processing {ctx.author}'s request..```")
    result = searchFor(args)
    output = f"{ctx.author.mention}\n```{result}```"
    await message.edit(content=output)

bot.run(token)
