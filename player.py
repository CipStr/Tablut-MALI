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

    def play(self, current_state):
        # receive the current state from the server
        # update the board
        self.board.convertBoard(current_state)
        # generate the tree
        minEval, move = tree.minimax(self.board, 4, self.color, -np.inf, np.inf)
        # convert the move to the format accepted by the server (rows from a-h and columns from 1-9)
        x1 = move[0]
        y1 = move[1]
        x2 = move[3]
        y2 = move[4]
        converted_move = [chr(x1 + 97) + str(y1 + 1), chr(x2 + 97) + str(y2 + 1)]
        return converted_move


player = Player("Luca", "black")
cns.connect_to_server(player)
