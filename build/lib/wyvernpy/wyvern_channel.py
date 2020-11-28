import json
import requests
from socketIO_client import SocketIO, LoggingNamespace



class channel:
    __slots__ = ("server", "id")
    def __init__(self, server, id):
        self.server = server
        self.id = id
      
    def send(self, bot, content):
      connection = SocketIO('wyvernapp.xyz', 80, LoggingNamespace)
      token = bot.token
      connection.emit('bot_message', {'data': str(content), 'token':token, 'room':str(self.id), 'serverid':self.server})
      print("[Sending] - ",str({'data': str(content), 'token':token, 'room':str(self.id), 'serverid':self.server}))
      connection.wait(seconds=0.1)