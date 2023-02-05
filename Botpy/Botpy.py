from xml.etree.ElementTree import tostring
import discord
from discord.ext import commands
from discord import app_commands
import random
import praw
import json


# Cog for images from reddit
class RedditImages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
        with open("key.json","r") as file:
            jsonData = json.load(file)
        key = jsonData["key"]
        REDDIT_APP_ID=jsonData["REDDIT_APP_ID"]
        REDDIT_APP_SECRET=jsonData["REDDIT_APP_SECRET"]
        REDDIT_USER=jsonData["username"]
        REDDIT_PASSWORD=jsonData["password"]

        # Praw init
        self.reddit = praw.Reddit(
            client_id= REDDIT_APP_ID,
            client_secret= REDDIT_APP_SECRET,
            password=REDDIT_PASSWORD,
            user_agent="Cheese.pyDiscord:%s:1.0" % REDDIT_APP_ID,
            username=REDDIT_USER,
        )


    # Bunny Reddit
    @commands.hybrid_command(aliases=['bun'])
    async def bunny(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("Rabbits").hot()

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
    @commands.hybrid_command(aliases=['mc'])
    async def minecraft(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("Minecraft").hot()

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
    @commands.hybrid_command(aliases=['m'])
    async def meme(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("memes").hot()

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
    @commands.hybrid_command(aliases=['kitty'])
    async def cat(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("cats").hot()

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
    @commands.hybrid_command(aliases=['doggo', 'doggy'])
    async def dog(self, ctx, num = 1):
        async with ctx.typing():
            if self.reddit:
                while num > 0:
                    notImage = True
                    while notImage:
                        submissions = self.reddit.subreddit("dog").hot()

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
    
class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # Avatar command
    @commands.command(aliases= ["av"])
    async def avatar(self, ctx, *,member: discord.Member=None):
        member = ctx.author if not member else member
        embed = discord.Embed(title=member.name)
        embed.set_image(url=member.display_avatar)
        await ctx.send(embed=embed)


    # Banner Command
    @commands.command()
    async def banner(self, ctx, *,member: discord.Member=None):
        target = ctx.author or member
        fetched = await bot.fetch_user(target.id)
        # print(fetched.banner.url)
        embed = discord.Embed(title=fetched.name)
        embed.set_image(url=fetched.banner)
        await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(str(round(bot.latency*100.0, 2)) + "ms")

    # Tells Join Date of User
    @commands.hybrid_command()
    async def joined(self, ctx, *, member: discord.Member):
        await ctx.send(f'{member} joined on {member.joined_at}')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    await bot.add_cog(RedditImages(bot))
    await bot.add_cog(Util(bot))
    print(f'We have logged in as {bot.user}')


#No
@bot.command()
async def porn(ctx):
    await ctx.send("No.")

# Ci
@bot.command()
async def ci(ctx):
    await ctx.send("Is amazing")





with open("key.json","r") as file:
    jsonData = json.load(file)
key = jsonData["key"]
# print(key)

bot.run(key)