from discord.ext import commands
import discord

class Delete(commands.Cog):
	def __init__(self,bot):
		self.bot=bot

	@commands.command(name="delete", help="Use this to delete spam messages only!")
	async def deletechats(self,ctx, limit):
		async for msg in ctx.message.channel.history(limit=int(limit)+1):
			try:
				await msg.delete()
			except:
				pass

def setup(bot):
	bot.add_cog(Delete(bot))