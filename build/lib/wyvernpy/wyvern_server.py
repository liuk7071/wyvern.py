import json

class server:
    __slots__ = ("name", "id", "owner", "channels", "date_of_creation", "users", "plan", "info")

    def __init__(self, json):
        self.name = json[1]
        self.id = json[2]
        self.owner = json[3]
        self.channels = json[4]
        self.date_of_creation = json[5]
        self.users = json[6]
        self.plan = json[7]
        self.info = json[8]
        