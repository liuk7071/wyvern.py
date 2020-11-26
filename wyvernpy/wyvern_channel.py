import json
import requests


class channel:
    __slots__ = ("server", "id")

    def __init__(self, server, id):
        self.server = server
        self.id = id
      
    def send(self, bot, content):
      requests.head("http://78.141.209.47:3030/api/sendmessage?serverid=" + self.server + "&wyvernid=" + bot.id + "&channelid=" + self.id + "&contents=" + content)
  