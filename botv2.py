import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def ozellik(ctx):
    await ctx.send(f'merhaba ben bir discord botuyum tanıştığıma memnun oldum adım {bot.user}, görevlerim şunlardır. öncelikle bana bir şey yazacaksan eğer önce dolar işareti "($)" kullanmalısın. sonrasında ise heh yazarsan 5 kere hehehehehe derim eğer sonradan sayı yazarsan o sayı kadar "he" yazarım. hello yazarsan kendimi tanıtırım. ozellik yazarsan şu anda yazdıklarımı yazarım. joined yazarsanda belirttiğin kişinin sunucuya ne zaman katıldığını gösterir')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run("TOKEN")
