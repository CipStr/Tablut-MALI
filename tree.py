# this file generates a tree using minimax algorithm and alpha-beta pruning.
# the tree is generated using the Board class defined in Board.py
# the tree is generated using the heuristic function defined in heuristics.py

import numpy as np
import Board
import heuristics


# define the minimax algorithm
def minimax(board, depth, player, alpha, beta):
    # if the depth is 0, return the heuristic score of the board
    if depth == 0:
        return heuristics.heuristic(board, 0)
    # if the player is WHITE, return the maximum score
    if player == "WHITE":
        maxEval = -np.inf
        best_move = None
        # generate all the possible moves for the WHITE
        moves = board.generateMoves(board, player)
        # for each move, generate the new board and call the minimax algorithm recursively
        for move in moves:
            new_board = board.copy()
            new_board.movePiece(move)
            tmp_eval = minimax(new_board, depth - 1, "BLACK", alpha, beta)
            maxEval = max(maxEval, tmp_eval)
            alpha = max(alpha, tmp_eval)
            best_move = move
            if beta <= alpha:
                break
        return maxEval, best_move
    # if the player is BLACK, return the minimum score
    else:
        minEval = np.inf
        best_move = None
        # generate all the possible moves for the BLACK
        moves = board.generateMoves(board, player)
        # for each move, generate the new board and call the minimax algorithm recursively
        for move in moves:
            new_board = board.copy()
            new_board.movePiece(move)
            tmp_eval = minimax(new_board, depth - 1, "WHITE", alpha, beta)
            minEval = min(minEval, tmp_eval)
            beta = min(beta, tmp_eval)
            best_move = move
            if beta <= alpha:
                break
        return minEval, best_move
