from discord.ext import commands
import discord
import requests
import json

class Rocket(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	
	@commands.command(name="launches")
	async def launches(self,ctx,num=1):
		embed=discord.Embed(title="Rocket Launches", description="Fetching rocket launches! :rocket:",color=0xFFFF00)
		message = await ctx.send(embed=embed)
		try:
			URL=f"https://fdo.rocketlaunch.live/json/launches/next/1"
			data=requests.get(URL)
			data=json.loads(data.text)
			data=data['result']
			embed=discord.Embed(title="Rocket Launches", description="Rocket launches :rocket:",color=0x00FF00)
			for i in range(1):
				temp=data[i]
				name=temp['name']
				provider=temp['provider']['name']
				vehicle=temp['vehicle']['name']
				location=temp['pad']['location']['name']
				weather_summary=temp['weather_summary']
				description=temp['quicktext']
				embed.add_field(name="Name: ", value=name)
				embed.add_field(name="Provider: ", value=provider)
				embed.add_field(name="Vechicle: ", value=vehicle)
				embed.add_field(name="Location: ", value=location)
				embed.add_field(name="Weather: ", value=weather_summary)
				embed.add_field(name="Description: ", value=description)
				await message.edit(embed=embed)
		except:
			embed=discord.Embed(title="Rocket Launches", description="Could not fetch data from API.",color=0xFF0000)


def setup(bot):
	bot.add_cog(Rocket(bot))