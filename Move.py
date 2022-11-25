class Move():

    def __init__(self, from_, to_, turn):
        self.from_ = from_
        self.to_ = to_
        self.turn = turn

    def get(self):
        move = {"from": self.from_, "to": self.to_, "turn": self.turn}
        return move