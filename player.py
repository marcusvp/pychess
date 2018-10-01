class Player:

    def __init__(self, name, color, IP):
        self.playerName = name
        self.playerIP = IP
        self.color = color
        if color == "white":
             self.isTurn = True
        else:
            self.isTurn = False
    