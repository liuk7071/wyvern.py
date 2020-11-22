import json

class member:
    __slots__ = ("name", "id", "join_date")

    def __init__(self, json):
        self.name = json[1]
        self.id = json[2]
        self.join_date = json[3]
        
