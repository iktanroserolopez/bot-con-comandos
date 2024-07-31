import  discord
import random
import requests

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command()
async def hola(ctx):
    await ctx.send("hola")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_pokemon_image_url():    
    url = ' https://pokeapi.co/api/v2/pokemon/ditto'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_zorro_image():    
    image = 'https://randomfox.ca/floof/'
    res = requests.get(image)
    data = res.json()
    return data['image']


@bot.command()
async def moneda(ctx):
    await ctx.send(random.randint(0,1))

@bot.command()
async def problemas(ctx):
    await ctx.send("botproblemasatencionalcliente.com,comunicate aqui")

@bot.command()
async def profesor(ctx, nombre):
    await ctx.send(f" {nombre} has sido asignado para la clase de bots con comandos ")
@bot.command()
async def opiniones(ctx, *, mensaje):
    await ctx.send(f"TU dices esto: {mensaje}")
@bot.command()
async def patoRandom(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def pokemon(ctx):
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

@bot.command()
async def zorro(ctx):
    image = get_zorro_image()
    await ctx.send(image)

bot.run("ingresa tu token de bot de discord")
