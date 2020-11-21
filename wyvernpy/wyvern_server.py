import json

class server:
    __slots__ = ()

    def __init__(self, json):
        self.name = json[1]
        self.owner = json[2]
        self.channels = json[3]
        self.date_of_creation = json[4]
        self.users = json[5]
        self.plan = json[6]
        self.info = json[7]
        