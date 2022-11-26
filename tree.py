# this file generates a tree using minimax algorithm and alpha-beta pruning.
# the tree is generated using the Board class defined in Board.py
# the tree is generated using the heuristic function defined in heuristics.py

import numpy as np
import Board
import heuristics


# define the minimax algorithm
def minimax(board, depth, player, alpha, beta, preceding_moves):
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
        #print("Black moves: ", moves)
        # for each move, generate the new board and call the minimax algorithm recursively
        for move in moves:
            new_board = Board.Board()
            new_board.setBoard(board)
            new_board.setBoard(new_board.movePiece(move))
            tmp_eval, tmp_move = minimax(new_board.getBoard(), depth - 1, "white", alpha, beta, preceding_moves)
            maxEval = max(maxEval, tmp_eval)
            alpha = max(alpha, tmp_eval)
            if maxEval == tmp_eval:
                # if this move is in the player's best moves, then discard it
                if move not in preceding_moves:
                    best_move = move
            if beta <= alpha:
                break
        if best_move is None:
            best_move = moves[0]
        return maxEval, best_move
    # if the player is BLACK, return the minimum score
    else:
        minEval = np.inf
        best_move = None
        # generate all the possible moves for the BLACK
        moves = board_class.generateMoves(board, player)
        #print("White moves: ", moves)
        # for each move, generate the new board and call the minimax algorithm recursively
        for move in moves:
            new_board = Board.Board()
            new_board.setBoard(board)
            new_board.setBoard(new_board.movePiece(move))
            tmp_eval, tmp_move = minimax(new_board.getBoard(), depth - 1, "black", alpha, beta, preceding_moves)
            minEval = min(minEval, tmp_eval)
            beta = min(beta, tmp_eval)
            if minEval == tmp_eval:
                if move not in preceding_moves:
                    best_move = move
            if beta <= alpha:
                break
        if best_move is None:
            best_move = moves[0]
        return minEval, best_move

