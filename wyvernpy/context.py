import json
import requests
from wyvernpy import wyvern_channel
from wyvernpy import wyvern_member
from wyvernpy import wyvern

class ctx:
    __slots__ = ("channel", "author", "content")

    def __init__(self, json):
        self.channel = wyvern_channel.channel(json[1], json[3])
        auth = requests.get("http://78.141.209.47:3030/api/getuserinfo?wyvernid=" + json[2]).json()
        self.author = wyvern_member.member(auth)
        self.content = json[4]
        