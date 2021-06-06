import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from googlesearch import search

class Music(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.command(name="join",help="Ask BFF bot to join current voice channel")
  async def join(self,ctx):
    channel=ctx.message.author.voice.channel
    await channel.connect()

  @commands.command(name="leave",help="Ask BFF bot to leave current voice channel")
  async def leave(self,ctx):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
      await voice.disconnect()

  @commands.command(name="pause",help="Ask BFF bot to pause current music")
  async def pause(self,ctx):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
      voice.pause()

  @commands.command(name="resume",help="Ask BFF bot to resume paused music")
  async def resume(self,ctx):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
      voice.resume()

  @commands.command(name="stop",help="Ask BFF bot to stop playing current music")
  async def stop(self,ctx):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    voice.stop()

  @commands.command(name="play",help="Format: !play MUSIC_NAME ARTIST_NAME.")
  async def play(self,ctx,music,artist=""):
    print(music,artist)
    search_query=f"{music} by {artist} site:youtube.com"
    embed=discord.Embed(title="Music",description=f"Searching for {music}  :musical_note:  by {artist}  :mag: ",color=0xFFFF00)
    message = await ctx.send(embed=embed)
    search_results = search(search_query, tld="com", stop=1)
    temp=[url for url in search_results]
    if temp!=[]:
      url=temp[0]
      YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True','-x':'','audioquality':"4"}
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
      if not voice.is_playing():
          with YoutubeDL(YDL_OPTIONS) as ydl:
              info = ydl.extract_info(url, download=False)
          URL = info['formats'][0]['url']
          embed=discord.Embed(title="Music",description=f"Now Playing {music}  :musical_note:  by {artist}  :mag: ",color=0x00FF00)
          await message.edit(embed=embed)
          voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
          voice.is_playing()
      else:
          embed=discord.Embed(title="Music",description=f"Already Playing {music}  :musical_note:  by {artist}  :mag:. Use `!stop` to stop the music",color=0x0000FF)
          await ctx.send(embed=embed)
          return
    else:
      embed=discord.Embed(title="Music",description=f"Could not find {music}  :musical_note:  by {artist}  :mag: ",color=0xFF0000)
      await message.edit(embed=embed)


def setup(bot):
  bot.add_cog(Music(bot))
