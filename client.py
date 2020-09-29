from __future__ import print_function

import sys
from time import sleep

from PodSixNet.Connection import connection, ConnectionListener
from board import Board

class Client(ConnectionListener, Board):
    def __init__(self, host, port):
        self.Connect((host, port))
        self.players = {}
        self.game_started = False
        self.net_id = None
        self.color = None
        
    def Loop(self):
        self.Pump()
        connection.Pump()
        if self.game_started:
            self.start_game()
        
    def Network_commence(self, data):
        print("received ", data)
        if data['check'] == "start":
            Board.__init__(self)
            self.commence_game()
            print("commence lad")
            
    def Network_message(self, data):
        print(data['message'])
    
    def Network_move_piece(self, data):
        print(data)
        if self.piece_movement.move_network(data['positions']):
            self.change_turn()
                
    def Network_players(self, data):
        print("received ", data)
        self.players_label = str(len(data['players'])) + " players"
        self.color = data['players'][str(self.net_id)]
        print(self.color)
        mark = []
        
        for i in data['players']:
            if not i in self.players:
                self.players[i] = {'color': data['players'][i]}
        for i in self.players:
            if not i in data['players'].keys():
                mark.append(i)
                
        for m in mark:
            del self.players[m]            
            
    def Network(self, data):
        pass
    
    def Network_error(self, data):
        print(data)
        import traceback
        traceback.print_exc()
        self.status_label = data['error'][1]
        connection.Close()
    
    def Network_set_id(self, data):
        self.net_id = data['net_id']
        print(self.net_id)
    
    def clients_move_piece(self, positions):
        connection.Send({"action": "move_piece", "positions": positions})
        print("client sent: ", positions)
    
    def net_color(self):
        return self.color
        
if __name__ == '__main__':
    #if len(sys.argv) != 2:
    #    print("Usage:", sys.argv[0], "host:port")
    #    print("e.g.", sys.argv[0], "localhost:31425")
    #else:
    #host, port = sys.argv[1].split(":")
    #c = Client(host, int(port))
    c = Client("127.0.0.1", int(7777))
    while 1:
        c.Loop()
        sleep(0.001)