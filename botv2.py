import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

print("Şu anda çalışılan klasör:", os.getcwd())

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def cevrebot(ctx):
    with open('images/cevre.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send(f"ben çevrebot Doğayı korumak için yanındayım bana sadece ne yapmayı istediğini söyle ben talimatı veririm. saksı, oyuncak, giysi. eğer sadece kullanmak yerine başka şeylerde yapacğaım dersen şunları yapabilirsin. ağaçlandırma çalışmalarına katıl.Örnek: TEMA yada kendin ağaçlar ek,atıkları doğru çöp kutusuna at. örnek: mavi kırmızı sarı gibi renkli olanlar")

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



@bot.command()
async def komik(ctx):
    files = os.listdir("images")
    selected_file = random.choice(files)
    with open(f'images/{selected_file}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def saksı(ctx):
    with open('images/saksi.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send(f'pet şişeleri yada plastik büyük su yada süt bidonunu ortadan ikiye bölüp onların iki parçasınada MARKETTEN ALMAMAK ÜZERE toprak dolduruyoruz ve saksımız hazır. bir yere asacaksan yanlarına silikon yada bant ile ip yapıştır')

@bot.command()
async def oyuncak(ctx):
    with open('images/petaraba.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send(f'kendi kendine giden araba. su şişesinin kenrlarına bir çöp şiş geçir o çöp şişlerede şişe kapaklarını yapıştır sonra şişenin arkasında bir pipetin sığabileceği bir yer del biraz büyük olsun. sonrasında oraya bir balon geçir ve pipeti balonun ağızına yapıştır ve sırada bir tek o pipete üfleyip o balonu şişirmek kalıyor balon şişince içindeki hava dıaşrı çıkıyor ve araba ilerliyor')

@bot.command()
async def giysi(ctx):
    await ctx.send(f'iki çeşidi var bunun. ilk çeşitte biiiirsürü şişe kapaını silikonla birbirlerine yapıştıracaksın ve giysi şekli oluşturacaksın sonrada giyeceksin. ikinci çeşit ise eski ve atılacak kıyafetinin üzerine kapakları yerleştirmek. yine silikon ile yapıştır.')


bot.run("TOKEN")
