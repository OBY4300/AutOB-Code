#Bu Discord Botum
import discord
import random
import time
from discord.ext import commands
from Bot_Ozellikleri import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event

async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command(description='hehehhehehehehhehehehhehehehehhehehehehhehehehehehehehhehehehehehehhehehehehheheheheheheheheheheheheheheheheheheheheheheheheheheheheheheheheheh')
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def merhaba(ctx):
    await ctx.send("Sana da merhaba.")

@bot.command()
async def sa(ctx):
    await ctx.send("Aleyküm Selam.")


@bot.command(description="piza.")
async def piza(ctx):
    mama = ["pizzarelli", "Pizza", "Pitsa", "Yuri Gagarin"]
    a = random.choice(mama)
    await ctx.send(a)

@bot.command(description="Shows AutOB's current ID.")
async def configid(ctx):
    await ctx.send(makeipconfig())

@bot.command()
async def configrunhealth(ctx):
    await ctx.send("Run.health is optimized. State: Good")

@bot.command()
async def confighostcell(ctx):
    await ctx.send("Host.cell is full. Neuron activity: Very Often, boolean state: 43,2781927786219213198980")

@bot.command()
async def peace(ctx):
    await ctx.send( "Host machine is infested with: peace_virus.exe message from administrator: https://discord.com/invite/JdknrDVpUQ")

@bot.command()
async def EnerHazarUsta(ctx):
    await ctx.send("Host.type: User, User Name: benjamin, Advanced information: Error invalid priviliges. message from administrator: Ne yani herkes Ener'in bilgilerine erişsin mi? Şaka mısın???")

@bot.command()
async def configadministrator(ctx):
    await ctx.send("Host.type: Administrator, User Name: OB-Y, Advanced information: Error invalid priviliges. message from administrator: Yoğ.")

@bot.command()
async def directory_change(ctx):
    await ctx.send("Can't find file directory such as thisiscursed/p")

@bot.command()
async def hintgiventoyou(ctx):
    await ctx.send("Figure out the possibilities. The infinite hex you can traverse.")

@bot.command()
async def Icaca(ctx):
    await ctx.send("Evet, ben de")

@bot.command()
async def amungus(ctx):
    await ctx.send("Shhhhhhhhhhhhhh...")

@bot.command()
async def configminecraftserver(ctx):
    await ctx.send("[10:16:27] [ServerMain/ERROR]: Failed to start the minecraft server com.google.gson.JsonParseException: com.google.gson.stream.MalformedJsonException")

@bot.command()
async def yazitura(ctx):
    yaziturasecim = ["Yazı", "Tura"]
    yazitura = random.choice(yaziturasecim)
    await ctx.send(yazitura)

bot.run("Your own key here")
