import discord
from discord.ext import commands
import scraper


intents = discord.Intents.default()
intents.typing = False
intents.presences = False  

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
live_scores = []

@bot.command() 
async def livescore(ctx):
    try:
        url = 'https://www.espncricinfo.com/live-cricket-score'  
        class_name1 = 'ds-text-tight-m ds-font-bold ds-capitalize ds-truncate'
        class_name2 = 'ds-text-tight-m ds-font-bold ds-capitalize ds-truncate'

        over1 = "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"
        over2 = "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"

        det = "ds-text-tight-s ds-font-regular ds-truncate ds-text-typo"

        print('executing livescore')
        scraped_data = scraper.scrape_specific_division(url, class_name1, class_name2, det, over1, over2)

        if scraped_data:
            await ctx.send(f'Title: {scraped_data}')
            live_scores.append(scraped_data)
        else:
            await ctx.send('data not found')

    except ValueError:
        await ctx.send('Usage /fetch <url>')

@bot.command()
async def csv(ctx):
    if live_scores:
        await ctx.send("All Live Scores:")
        for score in live_scores:
            await ctx.send(f'Title: {score}')
    else:
        await ctx.send('YOU HAVENT ASKED FOR ANY LIVE SCORES YET.')

@bot.command()
async def helpp(ctx):
    await ctx.send("use /livescore to get livescore, /csv for livescores youve asked until now, /help for help with so complicated commands")


bot.run('MTE1NDc1NTQwNDYxNDYxMDk0NA.G4XT1U.t2WvlPIVky9-ZZUeqh8QxDCX-JyEuwYWgfVgkc')
