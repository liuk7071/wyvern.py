from wyvernpy import wyvern
import asyncio
from datetime import datetime

bot = wyvern.wyvern_session("24448939", "4265191352", "!")

def main():
  while True:
    res = asyncio.run(async_main())

@bot.command
async def time(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  ctx.channel.send(bot, "Current bot time: "+current_time)
  

@bot.command
async def pog(ctx):
  ctx.channel.send(bot,"https://www.streamscheme.com/wp-content/uploads/2020/04/Pogchamp.png")

@bot.command
async def kek(ctx):
  ctx.channel.send(bot,"https://www.streamscheme.com/wp-content/uploads/2020/07/kekw-emote.jpg")
 

async def async_main():
  res = await asyncio.gather(time(),pog(),kek())
  return res

main()