from discord.ext import commands
import discord
from search_that_hash import api

class CrackTheHash(commands.Cog):
	def __init__(self,bot):
		self.bot=bot

	def get_hash(self,ctx, hash, embed):
		response = api.return_as_fast_json([hash])[0]
		print(response)
		if 'hash' not in response.keys(
		) and response[hash] != 'Could not crack hash':
			embed = discord.Embed(title="Hash cracking",description=f"Cracked {hash} :sunglasses:",color=0x00FF00)
			embed.add_field(name="Hash Type: ",value=" or ".join(response[hash]['types']),inline=False)
			embed.add_field(name="Plain Text: ", value=response[hash]['plaintext'])
			return embed
		else:
			embed = discord.Embed(title="Hash cracking",description=f"Could not crack {hash}:cry:",color=0xFF0000)
			return embed

	@commands.command(name="crack", help="A Tool to crack hashes with GPLv3 license.")
	async def crackthehash(self,ctx, hash):
		hash = hash.lower()
		embed = discord.Embed(title="Hash cracking",description=f"Cracking {hash} :slight_smile:",color=0xFFFF00)
		message = await ctx.send(embed=embed)
		await message.edit(content=ctx.author.mention,embed=self.get_hash(ctx, hash, embed))

def setup(bot):
	bot.add_cog(CrackTheHash(bot))