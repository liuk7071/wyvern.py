from wyvernpy import wyvern
import asyncio
bot = wyvern.wyvern_session("61852242", "1944823999", "!")


channel = bot.getChannel("1236687282", "general")
print(channel.server, channel.id)
channel.send(bot, "idk lol 2")

def main():
  while True:
    res = asyncio.run(async_main())

@bot.command
async def idk():
  print("cmd called")

@bot.command
async def idk2():
  print("cmd 2 called")


async def async_main():
  res = await asyncio.gather(idk(), idk2())
  return res

main()





