import discord
import time
from tabulate import tabulate
from table2ascii import table2ascii
from discord.ext import commands

client = commands.Bot(command_prefix="Hey nigga do ", self_bot = False, help_command=None)
#token = "mfa.cMReSq-doLpv1EHmamN5Q0nMKkt0NJwsHtfPugipwAF8UtFrefKggJ-x3820ni2_jvqH_WYcbSAawVpwie8o"
token = "OTY2NzE0MTY1OTU3ODkwMTE4.YmFwuQ.RuvQ4mj11c-YSQ02aDqbEKBTdwI"

listcommands = table2ascii(
    body=[["Commands"], ["e"]]
)

output = table2ascii(
    body=[["E"], ["monkey"], ["listcommands"], ["roast"], ["rules"]],  
)

rulelist = table2ascii(
    body=[["1) Be anti-LGBTQ+"],  ["2) Dont be a furry"], ["3) Dont act wierd"], ["4) Dont spam"], ["5) Invite people"], ["6) Be a chad and hate on faggots!"]],
)



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Hey nigga do commands'))
    print("Bot is working")
    

@client.command()
async def rules(ctx):
    await ctx.send(f"\n`{rulelist}`\n")

@client.command()
async def roast(ctx):
    await ctx.send("***Spamming roasts (Note dont take litiraly):*** ")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("You are what happens when women drink during pregnancy.")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("You are the sun in my life… now get 93 million miles away from me.")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("You have such a beautiful face… But let’s put a bag over that personality.")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("There is someone out there for everyone. For you, it’s a therapist.")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("I would smack you, but I’m against animal abuse.")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("If I wanted to kill myself, I would simply jump from your ego to your IQ.")
    await ctx.send("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    await ctx.send("I can’t wait to spend my whole life without you.")
    
@client.command()
async def e(ctx):
    await ctx.send("e")

@client.command()
async def monkey(ctx):
    await ctx.send("monkey")

@client.command()
async def commands(ctx):
    await ctx.send(f"\n`{output}`\n")


client.run(token, bot=True)