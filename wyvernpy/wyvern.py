import requests
from wyvernpy import wyvern_server
class wyvern_session:
    __slots__ = ("id", "token")

    def __init__(self, id: str, token: str):
        self.id = id
        self.token = token

    def getServersFromUser(self):
        try:
            servers = requests.get("http://78.141.209.47:3030/api/getserversfromuser?token=" + self.token)
            return servers[0]
        except:
            raise Exception("Failed to retreive servers from user with error code " + str(servers.status_code))

    def getServer(self, server_id: str):+
        try:
            server_json = requests.get("http://78.141.209.47:3030/api/getserver?serverid=" + server_id)
            return wyvern_server.server(server_json.json()[0])
        except:
            raise Exception("Failed to retreive server with error code " + str(server_json.status_code))