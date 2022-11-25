# The Board class represents the game board. It is responsible for storing the game state and checking the game rules.

import numpy as np


class Board:

    def __init__(self, string_matrix):
        # need to convert the string matrix to a 2D numpy array where each element is an integer
        # where 0 represents an empty space, 1 represents a white piece, 2 represents a black piece, and 3 represents
        # the king
        self.__size = 9
        self.__board = np.zeros((self.__size, self.__size), dtype=int)
        # convert the string values to the corresponding integer values
        for i in range(self.__size):
            for j in range(self.__size):
                # matrix initialized as zeros, so case "EMPTY" is not needed
                if string_matrix[i][j] == 'WHITE':
                    self.__board[i][j] = 1
                elif string_matrix[i][j] == 'BLACK':
                    self.__board[i][j] = 2
                elif string_matrix[i][j] == 'KING':
                    self.__board[i][j] = 3
        # the score of the board
        self.__score = 0

    # return the board
    def getBoard(self):
        return self.__board
    
    def getKing(self):
        # return the position of the KING
        return np.where(self.__board == 3)
    
    def getCenterCoordinate(self):
        # return the coordinate of the center of the square board
        return self.__size//2

    # return the board as a string
    def __str__(self):
        return str(self.__board)

    def isKingSurrounded(self):
        # check if the KING is surrounded by the opponent's pieces
        king = self.getKing()
        king_x = king[0][0]
        king_y = king[1][0]
        # check if the KING is surrounded by the opponent's pieces
        if self.__board[king_x - 1][king_y] == 2 and self.__board[king_x + 1][king_y] == 2 and \
                self.__board[king_x][king_y - 1] == 2 and self.__board[king_x][king_y + 1] == 2:
            return True
        else:
            return False

    def isKingNearThrone(self):
        # check if the KING is near the throne in the middle of the board
        king = self.getKing()
        if (king[0][0] + 1 == self.getCenterCoordinate() and king[1][0] == self.getCenterCoordinate()) or \
            (king[0][0] - 1 == self.getCenterCoordinate() and king[1][0] == self.getCenterCoordinate()) or \
            (king[0][0] == self.getCenterCoordinate() and king[1][0] + 1 == self.getCenterCoordinate()) or \
            (king[0][0] == self.getCenterCoordinate() and king[1][0] - 1 == self.getCenterCoordinate()):
            return True
        pass

    def isKingAtEdge(self):
        # check if the KING is at the edge of the board
        pass

    def isKingCaptured(self):
        # check if the KING is captured
        pass

    def getWhitePieces(self):
        # return the number of white pieces
        pass

    def getBlackPieces(self):
        # return the number of black pieces
        pass
