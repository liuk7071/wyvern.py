import requests

class wyvern_session:
    __slots__ = ("id", "token")

    def __init__(self, id: str, token: str):
        self.id = id
        self.token = token

    def getServer(self, server_id: str):
        server = requests.get("http://78.141.209.47:3030/api/getserver?serverid=" + server_id)
        return server.json()
    
