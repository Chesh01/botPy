from xml.etree.ElementTree import tostring
import discord
from discord.ext import commands
from discord import app_commands
import random
import praw
REDDIT_APP_ID="1xp4A0myryk44eT2EbmbTw"
REDDIT_APP_SECRET="bQEWGJ7_QOTE5eMZ48sQjKSwXaKQoA"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



# Praw init
reddit = praw.Reddit(
    client_id= REDDIT_APP_ID,
    client_secret= REDDIT_APP_SECRET,
    password="Cheshire@1975",
    user_agent="Cheese.pyDiscord:%s:1.0" % REDDIT_APP_ID,
    username="HmChesh",
)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def ping(ctx):
    await ctx.send(str(round(bot.latency*100.0, 2)) + "ms")

# Tells Join Date of User
@bot.hybrid_command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')


# Bunny Reddit
@bot.hybrid_command(aliases=['bun'])
async def bunny(ctx, num = 1):
    async with ctx.channel.typing():
        if reddit:
            while num > 0:
                notImage = True
                while notImage:
                    submissions = reddit.subreddit("Rabbits").hot()

                    post_to_pick = random.randint(1,100)

                    for i in range(0, post_to_pick):
                        submission = next(x for x in submissions if not x.stickied)
                        ## print(submission.url)
                    if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                        notImage = False
                        break
                await ctx.send(submission.url)
                num = num - 1
        else:
            await ctx.send("This is not working, contact dev")


#Minecraft Reddit
@bot.command()
async def minecraft(ctx, num = 1):
    async with ctx.channel.typing():
        if reddit:
            while num > 0:
                notImage = True
                while notImage:
                    submissions = reddit.subreddit("minecraft").hot()

                    post_to_pick = random.randint(1,100)

                    for i in range(0, post_to_pick):
                        submission = next(x for x in submissions if not x.stickied)
                        ## print(submission.url)
                    if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                        notImage = False
                        break
                await ctx.send(submission.url)
                num = num - 1
        else:
            await ctx.send("This is not working, contact dev")


# Meme Reddit
@bot.command()
async def meme(ctx, num = 1):
    async with ctx.channel.typing():
        if reddit:
            while num > 0:
                notImage = True
                while notImage:
                    submissions = reddit.subreddit("memes").hot()

                    post_to_pick = random.randint(1,100)

                    for i in range(0, post_to_pick):
                        submission = next(x for x in submissions if not x.stickied)
                        ## print(submission.url)
                    if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                        notImage = False
                        break
                await ctx.send(submission.url)
                num = num - 1
        else:
            await ctx.send("This is not working, contact dev")


# Cat Reddit
@bot.command()
async def cat(ctx, num = 1):
    async with ctx.channel.typing():
        if reddit:
            while num > 0:
                notImage = True
                while notImage:
                    submissions = reddit.subreddit("cats").hot()

                    post_to_pick = random.randint(1,100)

                    for i in range(0, post_to_pick):
                        submission = next(x for x in submissions if not x.stickied)
                        ## print(submission.url)
                    if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                        notImage = False
                        break
                await ctx.send(submission.url)
                num = num - 1
        else:
            await ctx.send("This is not working, contact dev")



# Dog Reddit
@bot.command()
async def dog(ctx, num = 1):
    async with ctx.channel.typing():
        if reddit:
            while num > 0:
                notImage = True
                while notImage:
                    submissions = reddit.subreddit("dog").hot()

                    post_to_pick = random.randint(1,100)

                    for i in range(0, post_to_pick):
                        submission = next(x for x in submissions if not x.stickied)
                        ## print(submission.url)
                    if submission.url.startswith("https://i.redd.it/") or submission.url.startswith("https://i.imgur.com/"): 
                        notImage = False
                        break
                await ctx.send(submission.url)
                num = num - 1
        else:
            await ctx.send("This is not working, contact dev")


#No
@bot.command()
async def porn(ctx):
    await ctx.send("No.")

# Ci
@bot.command()
async def ci(ctx):
    await ctx.send("Is amazing")


# Avatar command
@bot.command()
async def avatar(ctx, *,member: discord.Member=None):
    member = ctx.author if not member else member
    embed = discord.Embed(title=member.name)
    embed.set_image(url=member.display_avatar)
    await ctx.send(embed=embed)


# Banner Command
@bot.command()
async def banner(ctx, *,member: discord.Member=None):
    target = ctx.author or member
    fetched = await bot.fetch_user(target.id)
    # print(fetched.banner.url)
    embed = discord.Embed(title=fetched.name)
    embed.set_image(url=fetched.banner)
    await ctx.send(embed=embed)

bot.run('MTA3MTIwNjU3MTYxMjMxMTcwMw.GqAPWC.ZtzELD8kNkuk-smLZPoRe0SOK0S-yRK64uDQxg')