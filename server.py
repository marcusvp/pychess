from __future__ import print_function

import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

class ServerChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        self.id = str(self._server.NextId())
        self.color = self._server.generate_color(int(self.id))
        
    def PassOn(self, data):
        data.update({"id": self.id})
        self._server.SendToAll(data)
        
    def Close(self):
        self._server.DelPlayer(self)
    
    def Network_move_piece(self, data):
        print("passed on ", data)
        self.PassOn(data)
        
    def Network_commence(self, data):
        self.PassOn(data)        
    
class ChessServer(Server):
    channelClass = ServerChannel
    
    def __init__(self, *args, **kwargs):
        self.id = 0
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('Server launched')
        self.players_count = 0
        self.id_list = []
            
    def NextId(self):
        self.id += 1
        self.id_list.append(self.id)
        return self.id
    
    def Connected(self, channel, addr):
        self.ConnectToPlayer(channel)
        
    def ConnectToPlayer(self, player):
        self.players_count += 1
        print("New Player" + str(player.addr))
        self.players[player] = True
        player.Send({"action": "message", "message": "connected lad"})
        player.Send({"action": "set_id", "net_id": player.id})
        if self.players_count == 2:
            self.SendPlayers()
            self.SendToAll({"action": "commence", "check": "start"})
        
    def DelPlayer(self, player):
        print("Deleting Player" + str(player.addr))
        del self.players[player]
        self.SendPlayers
        self.players_count -= 1
        
    def SendPlayers(self):
        self.SendToAll({"action": "players", "players": dict([(p.id, p.color) for p in self.players])})
        for p in self.players:
            print(p, self.players[p])
    
    def SendToAll(self, data):
        [p.Send(data) for p in self.players]    
        
    def generate_color(self, id_num):
        if (id_num % 2) == 1:
            return "white"
        else:
            return "black"
        
    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)
            

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = ChessServer(localaddr=(host, int(port)))
        s.Launch()