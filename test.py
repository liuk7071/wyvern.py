from wyvernpy import wyvern
import asyncio
from datetime import datetime


bot = wyvern.wyvern_session("24448939", "1944823999", "!")


channel = bot.getChannel("1236687282", "general")
print(channel.server, channel.id)


def main():
  while True:
    res = asyncio.run(async_main())

@bot.command
async def time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  channel.send(bot, "Current bot time: "+current_time)
  print("cmd called")




async def async_main():
  res = await asyncio.gather(time())
  return res

main()





