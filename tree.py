# this file generates a tree using minimax algorithm and alpha-beta pruning.
# the tree is generated using the Board class defined in Board.py
# the tree is generated using the heuristic function defined in heuristics.py

import numpy as np
import Board
import heuristics


# define the minimax algorithm
def minimax(board, depth, player, alpha, beta):
    board_class = Board.Board()
    board_class.setBoard(board)
    # if the depth is 0, return the heuristic score of the board
    if depth == 0:
        return heuristics.heuristic(board_class, 0), None
    # if the player is WHITE, return the maximum score
    if player == "black":
        maxEval = -np.inf
        best_move = None
        # generate all the possible moves for the WHITE
        moves = board_class.generateMoves(board, player)
        # for each move, generate the new board and call the minimax algorithm recursively
        for move in moves:
            new_board = Board.Board()
            new_board.setBoard(board)
            new_board.setBoard(new_board.movePiece(move))
            tmp_eval, tmp_move = minimax(new_board.getBoard(), depth - 1, "white", alpha, beta)
            maxEval = max(maxEval, tmp_eval)
            alpha = max(alpha, tmp_eval)
            if maxEval == tmp_eval:
                best_move = move
            if beta <= alpha:
                break
        return maxEval, best_move
    # if the player is BLACK, return the minimum score
    else:
        minEval = np.inf
        best_move = None
        # generate all the possible moves for the BLACK
        moves = board_class.generateMoves(board, player)
        # for each move, generate the new board and call the minimax algorithm recursively
        for move in moves:
            new_board = Board.Board()
            new_board.setBoard(board)
            new_board.setBoard(new_board.movePiece(move))
            tmp_eval, tmp_move = minimax(new_board.getBoard(), depth - 1, "black", alpha, beta)
            minEval = min(minEval, tmp_eval)
            beta = min(beta, tmp_eval)
            if minEval == tmp_eval:
                best_move = move
            if beta <= alpha:
                break
        return minEval, best_move

