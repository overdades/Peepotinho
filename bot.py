import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio


# Carrega as variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)

@bot.event
async def on_ready():
    print(f"ACORDEI CARALHO!! Oficialmente {bot.user}")

async def carregar_comandos():
    for arquivo in os.listdir("./comandos"):
        if arquivo.endswith(".py") and not arquivo.startswith("__"):
            nome = arquivo[:-3]
            await bot.load_extension(f"comandos.{nome}")

async def main():
    await carregar_comandos()
    await bot.start(TOKEN)

asyncio.run(main())