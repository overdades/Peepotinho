import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pg")
    async def pg(self, ctx):
        await ctx.send("Pong! Tamo junto garai, eu e oce!")

async def setup(bot):  
    await bot.add_cog(Ping(bot))  
