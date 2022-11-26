# The engine represents the game algorithm. It is responsible for computing the game tree using the minimax algorithm.
# After the game tree is computed, the engine will return it to pruning.py to be pruned using alpha-beta pruning.
import numpy as np

import Board


# Define the heuristic function
def heuristic(board, score):
    # the move score is the sum of all the singular scores based on the board state
    move_score = score
    # check if the KING is surrounded by the opponent's pieces (not captured)
    if board.isKingSurrounded():
        move_score += 75*board.nEnemiesCloseToKing()
    # check if the KING is near the throne in the middle of the board
    if board.isKingNearThrone():
        move_score -= 50
    # check if the KING is at the edge of the board (WHITE wins)
    if board.isKingAtEdge():
        move_score -= 10000
    # check if the KING is captured (BLACK wins)
    if board.isKingCaptured():
        move_score += 10000
    # check if the WHITE has more pieces than the BLACK
    if board.getWhitePieces() > board.getBlackPieces():
        move_score -= (board.getWhitePieces() - board.getBlackPieces()) * 2  # multiply by 2 because the BLACK has in the
        # beginning of the game double the number of pieces than the WHITE
    # check if the BLACK has more pieces than the WHITE
    if board.getWhitePieces() < board.getBlackPieces():
        move_score += (board.getBlackPieces() - board.getWhitePieces())
    # sum to move score the number of good moves for the BLACK
    move_score += black_good_moves(board)
    # subtract to move score the number of good moves for the WHITE
    move_score -= white_good_moves(board)*2
    return move_score


def black_good_moves(board):
    # return the number of good moves for the BLACK given the board state
    # every black piece gets assigned a weight score, based on board state, for each quadrant
    # [top left, top right, bottom left, bottom right]
    # the weight score is the following:
    # very good move: 1
    # good move: 0.5
    # not so good move: 0.25
    # then sum all the weighted scores and return the sum
    king = board.getKing()
    king_x = king[0][0]
    king_y = king[1][0]
    weight_score = [0.5, 0.5, 0.5, 0.5]
    # if king is in the top left quadrant
    if king_x < board.getCenterCoordinate() and king_y < board.getCenterCoordinate():
        weight_score = [1, 0.5, 0.5, 0.25]
    # if king is in the top right quadrant
    elif king_x < board.getCenterCoordinate() < king_y:
        weight_score = [0.5, 1, 0.25, 0.5]
    # if king is in the bottom left quadrant
    elif king_x > board.getCenterCoordinate() > king_y:
        weight_score = [0.5, 0.25, 1, 0.5]
    # if king is in the bottom right quadrant
    elif king_x > board.getCenterCoordinate() and king_y > board.getCenterCoordinate():
        weight_score = [0.25, 0.5, 0.5, 1]
    # if king is in the top middle
    elif king_x < board.getCenterCoordinate() and king_y == board.getCenterCoordinate():
        weight_score = [1, 1, 0.25, 0.25]
    # if king is in the bottom middle
    elif king_x > board.getCenterCoordinate() and king_y == board.getCenterCoordinate():
        weight_score = [0.25, 0.25, 1, 1]
    # if king is in the left middle
    elif king_x == board.getCenterCoordinate() and king_y < board.getCenterCoordinate():
        weight_score = [1, 0.25, 1, 0.25]
    # if king is in the right middle
    elif king_x == board.getCenterCoordinate() and king_y > board.getCenterCoordinate():
        weight_score = [0.25, 1, 0.25, 1]
    # if king is in the center
    else:
        weight_score = [0.5, 0.5, 0.5, 0.5]
    # get the black pieces for each quadrant
    black_pieces = np.where(board.getBoard() == 2)
    black_pieces_x = black_pieces[0]
    black_pieces_y = black_pieces[1]
    tmp = black_pieces_y[black_pieces_x <= board.getCenterCoordinate()]
    top_right_pieces = len(tmp[tmp >= board.getCenterCoordinate()])
    tmp = black_pieces_y[black_pieces_x <= board.getCenterCoordinate()]
    top_left_pieces = len(tmp[tmp <= board.getCenterCoordinate()])
    tmp = black_pieces_y[black_pieces_x >= board.getCenterCoordinate()]
    bottom_right_pieces = len(tmp[tmp >= board.getCenterCoordinate()])
    tmp = black_pieces_y[black_pieces_x >= board.getCenterCoordinate()]
    bottom_left_pieces = len(tmp[tmp <= board.getCenterCoordinate()])
    # multiply the number of black pieces in each quadrant by the weight score
    top_right_score = top_right_pieces * weight_score[0]
    top_left_score = top_left_pieces * weight_score[1]
    bottom_right_score = bottom_right_pieces * weight_score[2]
    bottom_left_score = bottom_left_pieces * weight_score[3]
    # return the sum of all the weighted scores
    return top_right_score + top_left_score + bottom_right_score + bottom_left_score


def white_good_moves(board):
    # return the number of good moves for the WHITE given the board state (see black_good_moves)
    # good moves for white:
    # 1. try to block or eat the black pieces
    # get the white pieces
    white_pieces = np.where(board.getBoard() == 1)
    white_pieces_x = white_pieces[0]
    white_pieces_y = white_pieces[1]
    # for each white piece, check if it can eat or block a black piece
    # if it can, add 1 to the score for kill 0.75 for block
    score = 0
    for i in range(len(white_pieces_x)):
        x = white_pieces_x[i]
        y = white_pieces_y[i]
        # check if the piece can eat a black piece
        if board.canWhiteEatFrom(x, y):
            score += 1
        # check if the piece can block a black piece
        if board.canWhiteBlockFrom(x, y):
            score += 0.75
    return score


