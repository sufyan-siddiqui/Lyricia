import discord
from getLyrics import searchFor
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "!")
token = os.environ["TOKEN"]
@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(brief="Tells you the lyrics of the song", description="Tells you the lyrics of a song by passing in artist's and song's name as args\nuse the args as \"ArtistName-SongName\" without quotes\nmake sure to place hyphen between Artist and Song name ")
async def getlyrics(ctx, *, args):
    print(args)
    message = await ctx.send(f"```Processing {ctx.author}'s request..```")
    result = searchFor(args)
    output = f"{ctx.author.mention}\n```{result}```"
    await message.edit(content=output)

bot.run(token)
