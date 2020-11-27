import requests
from wyvernpy import wyvern_server, wyvern_member, wyvern_channel

import json
import ast
import threading
import asyncio
from functools import wraps

class wyvern_session:
    __slots__ = ("id", "token", "prefix", "commands")

    def __init__(self, id: str, token: str, prefix: str):
        self.id = id
        self.token = token
        self.prefix = prefix
        self.commands = []
        session_check = requests.get("http://78.141.209.47:3030/api/getuser?token=" + token)
        if session_check.status_code == 200:
            if session_check.json()[2] == id:
                print("Ready")
            else:
                raise Exception("Wyvern ID does not match token.")
        else:
            raise Exception("Invalid token")


    def getServers(self, _token = None):
        try:
            if _token != None:
                servers = requests.get("http://78.141.209.47:3030/api/getserversfromuser?token=" + _token)
                servers = servers.json()[0]
                _servers = ast.literal_eval(servers)
                return _servers
            else:
                servers = requests.get("http://78.141.209.47:3030/api/getserversfromuser?token=" + self.token)
                servers = servers.json()[0]
                _servers = ast.literal_eval(servers)
                return _servers
        except:
            raise Exception("Failed to retreive servers from user with error code " + str(servers.status_code))

    def getServer(self, server_id: str):
        try:
            server_json = requests.get("http://78.141.209.47:3030/api/getserver?serverid=" + server_id)
            return wyvern_server.server(server_json.json()[0])
        except:
            raise Exception("Failed to retrieve server with error code " + str(server_json.status_code))
    
    def getUser(self, user_id = None):
        try:
            if user_id != None:
                user_json = requests.get("http://78.141.209.47:3030/api/getuserinfo?wyvernid=" + user_id)
                return wyvern_member.member(user_json.json())
            else:
                user_json = requests.get("http://78.141.209.47:3030/api/getuserinfo?wyvernid=" + self.id)
                return wyvern_member.member(user_json.json())
        except:
            raise Exception("Failed to retrieve user info with error code " + str(user_json.status_code))
    
    def getChannel(self, serverID, id):
      server = self.getServer(serverID)
      if id in server.channels:
        return wyvern_channel.channel(serverID, id)
      else:
        raise Exception("The channel ID could not be found in the specified server")
      


    # command handling
    def command(self, func):
      @wraps(func)
      async def wrapped(*args, **kwargs):
        async def async_while():
          run = False
          json = requests.get("http://78.141.209.47:3030/api/getmessagesfromuser?token=" + self.token).json()
          if json[4] == self.prefix + func.__name__:
            await func()
        loop = asyncio.get_event_loop()
        loop.create_task(async_while())
        try:
          loop.run_forever()
        except:
          pass
      return wrapped

    

      
      