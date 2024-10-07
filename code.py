import discord
from discord.ext import commands
import openai

# Discord bot prefix'i '$' olarak ayarlanıyor
bot = commands.Bot(command_prefix='$')

# OpenAI API anahtarınızı buraya girin
openai.api_key = 'YEMEZLER'

# Bot çalışmaya başladığında yapılacak işlemler
@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı')

# $chat komutunu tanımlıyoruz
@bot.command()
async def chat(ctx, *, message: str):
    # OpenAI API'si ile ChatGPT'ye istekte bulunuyoruz
    response = openai.Completion.create(
        engine="text-davinci-003",  # En güçlü model
        prompt=message,
        max_tokens=100  # Maksimum yanıt uzunluğu
    )
    
    # ChatGPT'den gelen cevabı alıyoruz
    reply = response.choices[0].text.strip()
    
    # Bot, cevabı Discord'a geri gönderiyor
    await ctx.send(reply)

# Discord bot token'ınızı buraya ekleyin
bot.run('YEMEZLER')
