import connect2server as cns
import Board
import tree
import numpy as np


# create Player class
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.board = Board.Board()
        self.move = []

    def play(self, current_state):
        # receive the current state from the server
        # update the board
        self.board.convertBoard(current_state)
        print("Current state", self.board.getBoard())
        # generate the tree
        minEval, move = tree.minimax(self.board.getBoard(), 3, self.color, -np.inf, np.inf, self.move)
        # convert the move to the format accepted by the server (rows from a-h and columns from 1-9)
        print(move)
        print(self.move)
        if len(self.move) == 5:
            # remove the first element of the list
            self.move.pop(0)
            # add the current move to the list
            self.move.append(move)
        else:
            self.move.append(move)
        x1 = move[0]
        y1 = move[1]
        x2 = move[3]
        y2 = move[4]
        converted_move = [chr(int(y1) + 97) + str(int(x1) + 1), chr(int(y2) + 97) + str(int(x2) + 1)]
        print(converted_move)
        return converted_move


player = Player("Luca", "black")
cns.connect_to_server(player)
