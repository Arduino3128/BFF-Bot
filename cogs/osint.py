import discord
from discord.ext import commands
import requests

class OSINT(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(name="osint", help="""Open Source Intellegence API. Powered by SpiderFoot.

Your scan target may be one of the following:

Domain Name: e.g. example.com
IPv4 Address: e.g. 1.2.3.4
IPv6 Address: e.g. 2606:4700:4700::1111
Hostname/Sub-domain: e.g. abc.example.com
Subnet: e.g. 1.2.3.0/24
Bitcoin Address: e.g. 1HesYJSP1QqcyPEjnQ9vzBL1wujruNGe7R
E-mail address: e.g. bob@example.com
Phone Number: e.g. +12345678901 (E.164 format)
Human Name: e.g. "John Smith" (must be in quotes*)
Username: e.g. "jsmith2000" (must be in quotes*)
Network ASN: e.g. 1234

*Note: You will have to escape out of the quote for input with multiple segments.\n For Example: "John Smith" must be typed as "\\"John Smith\\"".
""")
	async def osint(self,ctx, scanname, scantarget):
		headers={"Host": "spiderfootapi.kanadnemade.repl.co","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Referer": "https://spiderfootapi.kanadnemade.repl.co/newscan","Content-Type": "application/x-www-form-urlencoded","Content-Length": "68","Origin": "https://spiderfootapi.kanadnemade.repl.co","Connection": "keep-alive","Upgrade-Insecure-Requests": "1","TE": "Trailers"}
		embed=discord.Embed(title="Open Source Intelligence. Powered by SpiderFoot",description=f"Analysing Scan Target: {scantarget} in {scanname}",color=0xFFFF00)
		message = await ctx.send(embed=embed)
		data={"scanname":scanname,"scantarget":scantarget,"usecase":"all","modulelist":"","typelist":""}
		opt=requests.post("https://spiderfootapi.kanadnemade.repl.co/startscan",data=data, headers=headers,allow_redirects=True)
		if str(opt.url)!="https://spiderfootapi.kanadnemade.repl.co/startscan":
			embed=discord.Embed(title="Open Source Intelligence. Powered by SpiderFoot",description=f"Analysing Scan Target: {scantarget} in {scanname}",color=0x00FF00)
			embed.add_field(name='Scan details at:', value=opt.url)
			await message.edit(content=ctx.author.mention, embed=embed)
		else:	
			embed=discord.Embed(title="Open Source Intelligence. Powered by SpiderFoot",description=f"Could not Scan Target: {scantarget} in {scanname}. \n Make sure \"Scan Target\" format is correct!",color=0xFF0000)
			await message.edit(content=ctx.author.mention, embed=embed)
		
	


def setup(bot):
	bot.add_cog(OSINT(bot))