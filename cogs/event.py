from discord.ext import commands, tasks
import discord
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from replit import db

print('Servers Registered: ',[keys for keys in db.keys()])
class Event(commands.Cog):
	def __init__(self, bot):
		self.bot=bot
		self.function.start()
		self.reminder.start()

	@commands.command(name="addevent", help="Add Birthday and Reminder events!")
	async def addevent(self, ctx, eventtype, mention, adddate, addtime="", about=""):
		adddate = adddate.split("-")
		adddate = [adddate[1], adddate[0], adddate[2]]
		
		if eventtype.capitalize() == "Birthday":
			print("Event Added")
			adddate = " ".join(adddate)
			adddate = datetime.strptime(adddate, "%m %d %Y").date()
			ID = str(ctx.guild.id)
			db[ID]['Birthday'][str(adddate)] = str(mention)
			print(db[ID]['Birthday'][str(adddate)])
			embed = discord.Embed(title="Add Event",description=f"Added Birthday Event {adddate} :sunglasses:",color=0x00FF00)
			await ctx.send(embed=embed)
		elif eventtype.capitalize() == "Reminder":
			ID = str(ctx.guild.id)
			addtime=addtime.split(":")
			adddate = " ".join(adddate+addtime)
			ISTTime=datetime.strptime(adddate, "%m %d %Y %H %M")
			ISTTime=ISTTime.strftime("%Y-%m-%d, %H:%M")
			adddate=datetime.strptime(adddate, "%m %d %Y %H %M")-timedelta(hours=5,minutes=30)
			adddate=adddate.strftime("%Y-%m-%d, %H:%M")
			print("Added Event on", str(adddate))
			db[ID]['Reminder'][str(adddate)]={}
			db[ID]['Reminder'][str(adddate)]["Mention"] = str(mention)
			db[ID]['Reminder'][str(adddate)]["About"] = str(about)
			print(db[ID]['Reminder'][str(adddate)])
			embed = discord.Embed(title="Add Event",description=f"Added Reminder Event {str(ISTTime)} :sunglasses:",color=0x00FF00)
			await ctx.send(embed=embed)

	def wishbirthday(self,mention):
		embed = discord.Embed(title=f"Happy Birthday! :confetti_ball: ",description=f"Hey! @everyone wish {mention}. It's PAAAAARRRRTY Time :confetti_ball: ",color=0x2E5090)
		return embed
	def remind(self,mention,about):
		embed=discord.Embed(title="Reminder",description=f"Reminder about {about}",color=0x00FF00)
		return embed
		
	@tasks.loop(seconds=5)
	async def reminder(self):
		for ID in [key for key in db.keys()]:
			try:
				temp = [key for key in dict(db[ID]["Reminder"]).keys()]
				if str(datetime.now().strftime("%Y-%m-%d, %H:%M")) in temp:
					mention=db[ID]["Reminder"][str(datetime.now().strftime("%Y-%m-%d, %H:%M"))]["Mention"]
					about=db[ID]["Reminder"][str(datetime.now().strftime("%Y-%m-%d, %H:%M"))]["About"]
					await self.bot.wait_until_ready()
					guild=[guildtemp for guildtemp in self.bot.guilds if int(guildtemp.id) == int(ID)][0]
					for channel in guild.channels:
						if str(channel)=='announcements':
							channel_id=int(channel.id)
							break
					print(channel_id)
					channel = self.bot.get_channel(channel_id)
					await channel.send(content=mention, embed=self.remind(mention,about))
					del db[ID]["Reminder"][str(datetime.now().strftime("%Y-%m-%d, %H:%M"))]
			except Exception as Error:
				print("ERROR 5 Secs: ", Error)
				
				
	@tasks.loop(seconds=15)
	async def function(self):
		for ID in [key for key in db.keys()]:
			try:
				temp = [key for key in dict(db[ID]["Birthday"]).keys()]
				if str(datetime.now().date()) in temp:
					mention = db[ID]["Birthday"][str(datetime.now().date())]
					await self.bot.wait_until_ready()
					guild=[guildtemp for guildtemp in self.bot.guilds if int(guildtemp.id) == int(ID)][0]
					for channel in guild.channels:
						if str(channel)=='general':
							channel_id=int(channel.id)
							break
					print(channel_id)
					channel = self.bot.get_channel(channel_id)
					await channel.send(content=f"{mention} and @everyone", embed=self.wishbirthday(mention))
					del db[ID]["Birthday"][str(datetime.now().date())]
					db[ID]["Birthday"][str((datetime.now()+relativedelta(years=1)).date())] = mention
					print('Hello! Its time!', db, str(datetime.now().date()))
			except Exception as Error:
				print("ERROR 15 Secs: ", Error)

def setup(bot):
	bot.add_cog(Event(bot))