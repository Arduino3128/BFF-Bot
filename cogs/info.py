import discord
from discord.ext import commands

class Info(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		
	@commands.command(name="info", help="Get information about the BFF Bot.")
	async def info(self,ctx):
		with open("config/info.txt",'r') as file:
			infodata=file.read()
		embed=discord.Embed(title="Info", description=infodata,color=0x00FF00)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Info(bot))