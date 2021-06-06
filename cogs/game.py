import discord
from discord.ext import commands
import random

class Game(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.command(name="rps", help="Play Rock Paper Scissors with BFF bot")
  async def rps(self,ctx, parameter):
    choice=["Rock :rock:","Paper :page_facing_up:", "Scissors :scissors:"]
    choice_sel=["rock","paper", "scissors"]
    option=random.choice(choice_sel)
    if type(parameter)==str:
      if option == parameter.lower():
        embed=discord.Embed(title="Rock Paper Scissors", description=f"{choice[choice_sel.index(parameter.lower())]} and {choice[choice_sel.index(option)]} are friends! It's a draw",color=0xFFFF00)
        embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
        embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
      elif parameter.lower()=="rock":
        if option=="paper":
          embed=discord.Embed(title="Rock Paper Scissors",description="Paper covers rock! You lose.", color=0xFF0000)
          embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
          embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
        else:
          embed=discord.Embed(title="Rock Paper Scissors",description="Rock smashes scissors! You win!", color=0x00FF00)
          embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
          embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
      elif parameter.lower()=="paper":
        if option=="scissors":
          embed=discord.Embed(title="Rock Paper Scissors",description="Scissors cuts paper! You lose.", color=0xFF0000)
          embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
          embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
        else:
          embed=discord.Embed(title="Rock Paper Scissors",description="Paper covers rock! You win!", color=0x00FF00)
          embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
          embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
      elif parameter.lower()=="scissors":
        if option=="rock":
          embed=discord.Embed(title="Rock Paper Scissors",description="Rock smashes scissors! You lose.", color=0xFF0000)
          embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
          embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
        else:
          embed=discord.Embed(title="Rock Paper Scissors",description="Scissors cuts paper! You win!", color=0x00FF00)
          embed.add_field(name="You chose:",value=choice[choice_sel.index(parameter.lower())])
          embed.add_field(name="I chose:", value=choice[choice_sel.index(option)])
      else:
          embed=discord.Embed(title="Rock Paper Scissors",description="Illegal choice! :oncoming_police_car:", color=0xFF0000)
    else:
          embed=discord.Embed(title="Rock Paper Scissors",description="Illegal choice! :oncoming_police_car:", color=0xFF0000)
    await ctx.send(embed=embed)
    
def setup(bot):
  bot.add_cog(Game(bot))