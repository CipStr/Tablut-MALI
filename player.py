import time

import connect2server as cns
import Board
import tree
import numpy as np
import sys

# timer class
class Timer:
    def __init__(self, timeout):
        self.timeout = int(timeout) - 15
        self.time = 0


# create Player class
class Player:
    def __init__(self, name, color, server, timer):
        self.name = name
        self.color = color
        self.server = server
        self.board = Board.Board()
        self.move = []
        self.timer = timer

    def play(self, current_state):
        # receive the current state from the server
        # update the board
        self.timer.time = time.time()
        self.board.convertBoard(current_state)
        # generate the tree
        depth = 3
        try:
            minEval, move = tree.minimax(self.board.getBoard(), depth, self.color, -np.inf, np.inf, self.move, self.timer)
        except TimeoutError:
            self.timer.time = time.time()
            depth -= 2
            minEval, move = tree.minimax(self.board.getBoard(), depth, self.color, -np.inf, np.inf, self.move, self.timer)
        # convert the move to the format accepted by the server (rows from a-h and columns from 1-9)
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
        return converted_move


color = sys.argv[1]
timeout = sys.argv[2]
server_ip = sys.argv[3]
timer = Timer(timeout)
player = Player("MALI", color.lower(), server_ip, timer)
cns.connect_to_server(player)
