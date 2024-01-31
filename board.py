import random
from piece import Piece

class Board:
    def __init__(self, size, prob):
        """Initialize the board with a given size and bomb probability."""
        self.size = size
        self.board = [[Piece(random.random() < prob) for _ in range(size[1])] for _ in range(size[0])]
        self.won = False
        self.lost = False
        self.setNeighbors()
        self.setNumAround()

    def print_board(self):
        """Print the board state."""
        for row in self.board:
            print(" ".join(str(piece) for piece in row))

    def getBoard(self):
        """Return the board."""
        return self.board

    def getSize(self):
        """Return the size of the board."""
        return self.size

    def getPiece(self, index):
        """Return a piece at a specific index."""
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        """Handle a click event on a piece."""
        if piece.getClicked() or (piece.getFlagged() and not flag):
            return
        if flag:
            piece.toggleFlag()
        else:
            piece.handleClick()
            if piece.getNumAround() == 0:
                for neighbor in piece.getNeighbors():
                    self.handleClick(neighbor, False)
            if piece.getHasBomb():
                self.lost = True
            else:
                self.won = self.checkWon()

    def checkWon(self):
        """Check if the game is won."""
        return all(piece.getClicked() or piece.getHasBomb() for row in self.board for piece in row)

    def getWon(self):
        """Return the win state."""
        return self.won

    def getLost(self):
        """Return the lose state."""
        return self.lost

    def setNeighbors(self):
        """Set neighbors for each piece."""
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.getPiece((row, col))
                neighbors = self.findNeighbors(row, col)
                piece.setNeighbors(neighbors)

    def findNeighbors(self, row, col):
        """Find and return valid neighbors of a given piece."""
        neighbors = []
        for r in range(max(0, row-1), min(row+2, self.size[0])):
            for c in range(max(0, col-1), min(col+2, self.size[1])):
                if (r, c) != (row, col):
                    neighbors.append(self.getPiece((r, c)))
        return neighbors

    def setNumAround(self):
        """Set the number of bombs around each piece."""
        for row in self.board:
            for piece in row:
                piece.setNumAround()