import discord
from discord.ext import commands
import requests
import json

class Random(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command(name="random", help="Generate random useless facts!")
  async def random(self,ctx):
    fact=requests.get("https://useless-facts.sameerkumar.website/api")
    fact=json.loads(fact.text)
    embed=discord.Embed(title="Random Fact", description=fact['data'],color=0x00FF00)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Random(bot))