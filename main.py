# main.py
import discord, search_that_hash
import logging
import os,json
from replit import db
from keep_alive import keep_alive
from discord.ext import commands

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG) # Do not allow DEBUG messages through
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("{asctime}: {levelname}: {name}: {message}", style="{"))
logger.addHandler(handler)

print([keys for keys in db.keys()])
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_guild_join(guild):
	ID = str(guild.id)
	db[ID] = {}
	db[ID]["Birthday"] = {}
	db[ID]["Reminder"] = {}
	for channel in guild.channels:
			if str(channel)=='announcements':
				channel_id=int(channel.id)
				break
	print(channel_id)
	channel = bot.get_channel(channel_id)
	embed = discord.Embed(title="Hello! I am BFF Bot",description=":wave: I keep record of your birthdays :confetti_ball:",color=0x2E5090)
	embed.set_footer(text="I am developed by Kanad Nemade")
	await channel.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
	try:
		ID = str(guild.id)
		del db[ID]
	except:
		pass

@bot.event
async def on_ready():
	with open("config/cogs.json",'r') as config:
		configs=json.load(config)
	print("Loading Cogs")
	for cog in configs["Cogs"]:
		try:
			bot.load_extension(cog)
			print(f"Cog {cog} loaded successfully!")
		except Exception as error:
			print(f"Cog {cog} failed to load.",str(error))
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over the server'))

keep_alive()
bot.run(os.environ['TOKEN'])