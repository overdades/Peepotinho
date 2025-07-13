import discord
from discord.ext import commands
import random
import asyncio

class Fight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fights = {}  # Armazena quem está sendo desafiado por quem

    @commands.command(name="fight", help="Desafie alguém para uma luta! Use: !fight @usuário")
    @commands.cooldown(rate=3, per=10, type=commands.BucketType.user)
    async def fight(self, ctx, member: discord.Member):
        desafiado = member.name
        desafiante = ctx.author.name

        if member == self.bot.user:
            return await ctx.send("Você nunca conseguiria me derrotar... 🤖")
        if member == ctx.author:
            return await ctx.send("Você iniciou uma luta interna... 💥")

        if self.fights.get(desafiado):
            return await ctx.send(f"{member.mention} já está sendo desafiado por {self.fights[desafiado]}!")

        self.fights[desafiado] = desafiante
        await ctx.send(f"{ctx.author.mention} desafiou {member.mention} para uma luta! Você aceita? (sim/não)")

        def check(message):
            return (
                message.author == member and
                message.channel == ctx.channel and
                message.content.lower() in ("sim", "s", "não", "nao", "n")
            )

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30)
            if msg.content.lower() in ("sim", "s"):
                frases = [
                    f"{desafiado} acaba com {desafiante}!",
                    f"{desafiado} deixa {desafiante} desacordado!",
                    f"{desafiado} derrota {desafiante} facilmente!",
                    f"{desafiado} espanca {desafiante} sem piedade!",
                    f"{desafiado} vence a luta contra {desafiante}!",
                    f"{desafiante} acaba com {desafiado}!",
                    f"{desafiante} deixa {desafiado} desacordado!",
                    f"{desafiante} derrota {desafiado} facilmente!",
                    f"{desafiante} espanca {desafiado} sem piedade!",
                    f"{desafiante} vence a luta contra {desafiado}!",
                ]
                resultado = random.choice(frases)
                await ctx.send(f"🥊 {resultado}")
            else:
                await ctx.send(f"{member.mention} recusou o desafio contra {ctx.author.mention} 👎")
        except asyncio.TimeoutError:
            await ctx.send(f"{member.mention} não respondeu ao desafio de {ctx.author.mention} a tempo ⏰")
        finally:
            self.fights.pop(desafiado, None)

# Carregamento da COG
async def setup(bot):
    await bot.add_cog(Fight(bot))
