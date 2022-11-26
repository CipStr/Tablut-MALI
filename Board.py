# The Board class represents the game board. It is responsible for storing the game state and checking the game rules.

import numpy as np


class Board:

    def __init__(self):
        self.__size = 9
        # initialize the board
        self.__board = np.zeros((self.__size, self.__size), dtype=int)
        # set the throne
        self.__board[self.getCenterCoordinate()][self.getCenterCoordinate()] = 3
        # set white pieces (in a cross shape around the throne)
        for i in range(self.getCenterCoordinate()-2,self.getCenterCoordinate()):
            self.__board[i][self.getCenterCoordinate()] = 1
            self.__board[self.getCenterCoordinate()][i] = 1
        for i in range(self.getCenterCoordinate()+1,self.getCenterCoordinate()+3):
            self.__board[i][self.getCenterCoordinate()] = 1
            self.__board[self.getCenterCoordinate()][i] = 1
        # set black pieces ( in the camps)
        for i in range(self.getCenterCoordinate()-1, self.getCenterCoordinate()+2):
            self.__board[i][0] = 2
            self.__board[i][self.__size-1] = 2
            self.__board[0][i] = 2
            self.__board[self.__size-1][i] = 2
        # set the last black pieces
        self.__board[self.getCenterCoordinate()][1] = 2
        self.__board[self.getCenterCoordinate()][self.__size-2] = 2
        self.__board[1][self.getCenterCoordinate()] = 2
        self.__board[self.__size-2][self.getCenterCoordinate()] = 2
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
        return self.__size // 2

    # return the board as a string
    def __str__(self):
        return str(self.__board)

    def getNeighbours(self, x, y):
        # return the neighbours of the piece at (x, y)
        neighbours = []
        if x > 0:
            neighbours.append((x - 1, y))
        if x < self.__size - 1:
            neighbours.append((x + 1, y))
        if y > 0:
            neighbours.append((x, y - 1))
        if y < self.__size - 1:
            neighbours.append((x, y + 1))
        return neighbours

    def isKingSurrounded(self):
        # check if the KING is surrounded by the opponent's pieces
        king = self.getKing()
        king_x = king[0][0]
        king_y = king[1][0]
        # check if the KING is surrounded by least 1 black piece
        if self.__board[king_x - 1][king_y] == 2 or self.__board[king_x + 1][king_y] == 2 or \
                self.__board[king_x][king_y - 1] == 2 or self.__board[king_x][king_y + 1] == 2:
            return True
        return False

    def isKingOnThrone(self):
        # check if the KING is on the throne
        king = self.getKing()
        return king[0][0] == self.getCenterCoordinate() and king[1][0] == self.getCenterCoordinate()

    def isKingNearCamp(self):
        # check if the KING is near the camp
        king = self.getKing()
        neighbours = self.getNeighbours(king[0][0], king[1][0])
        for neighbour in neighbours:
            if self.isCamp(neighbour[0], neighbour[1]):
                return True
        return False

    def isCamp(self, x, y):
        # check if the piece at (x, y) is a camp
        centerCoor = self.getCenterCoordinate()
        centerCoors = (centerCoor, centerCoor + 1, centerCoor - 1)
        if ((x == 0 and y in centerCoors) or (x == self.__size - 1 and y in centerCoors) or
                (y == 0 and x in centerCoors) or (y == self.__size - 1 and x in centerCoors)):
            return True
        if ((x == 1 and y == centerCoor) or (x == self.__size - 2 and y == centerCoor) or
                (y == 1 and x == centerCoor) or (y == self.__size - 2 and x == centerCoor)):
            return True
        return False

    def isCenter(self, x, y):
        # check if the piece at (x, y) is at the center of the board
        return x == self.getCenterCoordinate() and y == self.getCenterCoordinate()

    def nEnemiesCloseToKing(self):
        # return the number of enemies close to the KING
        closeToKing = (self.__board[self.getKing()[0][0] - 1][self.getKing()[1][0]],
                       self.__board[self.getKing()[0][0] + 1][self.getKing()[1][0]],
                       self.__board[self.getKing()[0][0]][self.getKing()[1][0] - 1],
                       self.__board[self.getKing()[0][0]][self.getKing()[1][0] + 1])
        # count the number of enemies close to the KING, where 2 represents a black piece
        return closeToKing.count(2)

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
        king = self.getKing()
        size = self.__size
        return king[0][0] == 0 or king[0][0] == size - 1 or \
            king[1][0] == 0 or king[1][0] == size - 1

    def isKingCaptured(self):
        # check if the KING is captured
        if self.isKingOnThrone() and self.nEnemiesCloseToKing() == 4:
            return True
        elif self.isKingNearThrone() and self.nEnemiesCloseToKing() == 3:
            return True
        elif self.nEnemiesCloseToKing() == 2:
            return True
        elif self.isKingNearCamp() and self.nEnemiesCloseToKing() == 1:
            return True
        return False

    # check if this works
    def getWhitePieces(self):
        # return the number of white pieces
        return self.getBoard().tolist().count(1)

    def getBlackPieces(self):
        # return the number of black pieces
        return self.getBoard().tolist().count(2)

    # given a board, return all the possible moves for the player
    def generateMoves(self, board, player):
        # moves are in format "xy_xnewynew"
        moves = []
        if player == "white":
            # get the position of all the white pieces
            whitePieces = np.where(board == 1)
            for i in range(len(whitePieces[0])):
                x = whitePieces[0][i]
                y = whitePieces[1][i]
                # check every possible move for the white piece
                if x > 0 and board[x - 1][y] == 0 and not self.isCamp(x - 1, y) and not self.isCenter(x - 1, y):
                    moves.append(str(x) + str(y) + "_" + str(x - 1) + str(y))
                if x < self.__size - 1 and board[x + 1][y] == 0 and not self.isCamp(x + 1, y) and not self.isCenter(
                        x + 1, y):
                    moves.append(str(x) + str(y) + "_" + str(x + 1) + str(y))
                if y > 0 and board[x][y - 1] == 0 and not self.isCamp(x, y - 1) and not self.isCenter(x, y - 1):
                    moves.append(str(x) + str(y) + "_" + str(x) + str(y - 1))
                if y < self.__size - 1 and board[x][y + 1] == 0 and not self.isCamp(x, y + 1) and not self.isCenter(x, y + 1):
                    moves.append(str(x) + str(y) + "_" + str(x) + str(y + 1))
        elif player == "black":
            # get the position of all the black pieces
            blackPieces = np.where(board == 2)
            for i in range(len(blackPieces[0])):
                x = blackPieces[0][i]
                y = blackPieces[1][i]
                # check every possible move for the black piece, black pieces can move in a camp until they leave it
                if x > 0 and board[x - 1][y] == 0 and self.isCamp(x, y) and self.isCamp(x - 1, y) and not self.isCenter(
                        x - 1, y):
                    moves.append(str(x) + str(y) + "_" + str(x - 1) + str(y))
                if x < self.__size - 1 and board[x + 1][y] == 0 and self.isCamp(x, y) and self.isCamp(x + 1,
                                                                                                      y) and not self.isCenter(
                    x + 1, y):
                    moves.append(str(x) + str(y) + "_" + str(x + 1) + str(y))
                if y > 0 and board[x][y - 1] == 0 and self.isCamp(x, y) and self.isCamp(x, y - 1) and not self.isCenter(
                        x, y - 1):
                    moves.append(str(x) + str(y) + "_" + str(x) + str(y - 1))
                if y < self.__size - 1 and board[x][y + 1] == 0 and self.isCamp(x, y) and self.isCamp(x,
                                                                                                      y + 1) and not self.isCenter(
                    x, y + 1):
                    moves.append(str(x) + str(y) + "_" + str(x) + str(y + 1))
                if x > 0 and board[x - 1][y] == 0 and not self.isCamp(x - 1, y) and not self.isCenter(x - 1, y):
                    moves.append(str(x) + str(y) + "_" + str(x - 1) + str(y))
                if x < self.__size - 1 and board[x + 1][y] == 0 and not self.isCamp(x + 1, y) and not self.isCenter(
                        x + 1, y):
                    moves.append(str(x) + str(y) + "_" + str(x + 1) + str(y))
                if y > 0 and board[x][y - 1] == 0 and not self.isCamp(x, y - 1) and not self.isCenter(x, y - 1):
                    moves.append(str(x) + str(y) + "_" + str(x) + str(y - 1))
                if y < self.__size - 1 and board[x][y + 1] == 0 and not self.isCamp(x, y + 1) and not self.isCenter(x,
                                                                                                                    y + 1):
                    moves.append(str(x) + str(y) + "_" + str(x) + str(y + 1))
        return moves

    def getValueAt(self, x, y):
        # return the value of the piece at (x, y)
        return self.__board[x][y]

    def canWhiteEatFrom(self, x, y):
        element = 0
        inc = 1
        # check if the piece at (x, y) can eat a black piece going right
        while element == 0:
            if self.isCamp(x, y + inc) or y + inc == self.__size:
                break
            element = self.getValueAt(x, y + inc)
            inc += 1
        if element == 2 and (
                y + inc == self.__size or self.getValueAt(x, y + inc) == 1 or self.getValueAt(x, y + inc) == 3):
            return True
        element = 0
        # check if the piece at (x, y) can eat a black piece going left
        inc = -1
        while element == 0:
            if self.isCamp(x, y + inc) or y + inc == self.__size:
                break
            element = self.getValueAt(x, y + inc)
            inc -= 1
        if element == 2 and (
                y + inc == self.__size or self.getValueAt(x, y + inc) == 1 or self.getValueAt(x, y + inc) == 3):
            return True
        # check if the piece at (x, y) can eat a black piece going down
        inc = 1
        while element == 0:
            if self.isCamp(x + inc, y) or x + inc == self.__size:
                break
            element = self.getValueAt(x + inc, y)
            inc += 1
        if element == 2 and (
                x + inc == self.__size or self.getValueAt(x + inc, y) == 1 or self.getValueAt(x + inc, y) == 3):
            return True
        # check if the piece at (x, y) can eat a black piece going up
        inc = -1
        while element == 0:
            if self.isCamp(x + inc, y) or x + inc == self.__size:
                break
            element = self.getValueAt(x + inc, y)
            inc -= 1
        if element == 2 and (
                x + inc == self.__size or self.getValueAt(x + inc, y) == 1 or self.getValueAt(x + inc, y) == 3):
            return True
        return False

    def canWhiteBlockFrom(self, x, y):
        element = 0
        inc = 1
        # check if the piece at (x, y) can eat a black piece going right
        while element == 0:
            if y + inc == self.__size or self.isCamp(x, y + inc):
                break
            element = self.getValueAt(x, y + inc)
            inc += 1
        if element == 2:
            return True
        element = 0
        # check if the piece at (x, y) can eat a black piece going left
        inc = -1
        while element == 0:
            if y + inc == self.__size or self.isCamp(x, y + inc):
                break
            element = self.getValueAt(x, y + inc)
            inc -= 1
        if element == 2:
            return True
        # check if the piece at (x, y) can eat a black piece going down
        inc = 1
        while element == 0:
            if x + inc == self.__size or self.isCamp(x + inc, y):
                break
            element = self.getValueAt(x + inc, y)
            inc += 1
        if element == 2:
            return True
        # check if the piece at (x, y) can eat a black piece going up
        inc = -1
        while element == 0:
            if x + inc == self.__size or self.isCamp(x + inc, y):
                break
            element = self.getValueAt(x + inc, y)
            inc -= 1
        if element == 2:
            return True
        return False

    def movePiece(self, move):
        # return a new board with the piece moved
        newBoard = self.getBoard().copy()
        x1 = int(move[0])
        y1 = int(move[1])
        x2 = int(move[3])
        y2 = int(move[4])
        newBoard[x2][y2] = newBoard[x1][y1]
        newBoard[x1][y1] = 0
        return newBoard

    def convertBoard(self, board):
        # convert the board to a 2D array
        self.__board = np.zeros((self.__size, self.__size), dtype=int)
        for i in range(self.__size):
            for j in range(self.__size):
                if board[i][j] == "WHITE":
                    self.__board[i][j] = 1
                elif board[i][j] == "BLACK":
                    self.__board[i][j] = 2
                elif board[i][j] == "KING":
                    self.__board[i][j] = 3

    def setBoard(self, board):
        self.__board = board