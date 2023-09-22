import discord
from discord.ext import commands
import scraper 

bot = commands.Bot(command_prefix='/')

live_scores = []

@bot.command()
async def livescore(ctx):
    try:
        url = 'https://www.espncricinfo.com/live-cricket-score'  
        class_name1 = 'ds-text-tight-m ds-font-bold ds-capitalize ds-truncate'
        class_name2 = 'ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3'

        over1 = "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"
        over2 = "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"

        det = "ds-text-tight-s ds-font-regular ds-truncate ds-text-typo"


        scraped_data = scraper.scrape_specific_division(url, class_name1, class_name2, over1, over2, det)

        if scraped_data:
            await ctx.send(f'Title: {scraped_data}')
        else:
            await ctx.send('WHY YOU LOOKING CRICKET SCORE GO STUDY')

    except ValueError:
        await ctx.send('Usage: /fetch <url>')

@bot.command()
async def csv(ctx):
    if live_scores:
        await ctx.send("All Live Scores:")
        for score in live_scores:
            await ctx.send(f'Title: {score}')
    else:
        await ctx.send('YOU HAVENT ASKED FOR ANY LIVE SCORES YET.')

@bot.command()
async def help(ctx):
    await ctx.send("use /livescore to get livescore, /csv for livescores youve asked until now, /help for help with so complicated commands")


bot.run('MTE1NDc1NTQwNDYxNDYxMDk0NA.G540Xy.3xkya2AmhTgEUzctG512ZUG-nNTra_9pqNqdDo')
