import random
from piece import Piece

class Board:
    """Represents the game board for Minesweeper, containing pieces with or without bombs."""

    def __init__(self, size, prob):
        """
        Initializes a new game board with pieces.

        Parameters:
        - size (tuple): The size of the board as (rows, cols).
        - prob (float): Probability of a piece containing a bomb.
        """
        self.size = size
        self.board = [[Piece(random.random() < prob) for _ in range(size[1])] for _ in range(size[0])]
        self.won = False
        self.lost = False
        self.set_neighbors()
        self.set_num_around()

    def print_board(self):
        """Prints a visual representation of the board to the console."""
        for row in self.board:
            print(' '.join(str(piece) for piece in row))

    def get_board(self):
        """Returns the board."""
        return self.board

    def get_size(self):
        """Returns the size of the board."""
        return self.size

    def get_piece(self, index):
        """Returns the piece at a specified index."""
        return self.board[index[0]][index[1]]

    def handle_click(self, piece, flag):
        """
        Processes a click action on a piece.

        Parameters:
        - piece (Piece): The piece that was clicked.
        - flag (bool): Whether the click is to toggle a flag.
        """
        if piece.get_clicked() or (piece.get_flagged() and not flag):
            return
        if flag:
            piece.toggle_flag()
        else:
            piece.handle_click()
            if piece.get_num_around() == 0:
                for neighbor in piece.get_neighbors():
                    self.handle_click(neighbor, False)
            if piece.get_has_bomb():
                self.lost = True
            else:
                self.won = self.check_won()

    def check_won(self):
        """Checks if all non-bomb pieces have been clicked."""
        return all(piece.get_clicked() or piece.get_has_bomb() for row in self.board for piece in row)

    def get_won(self):
        """Returns True if the game has been won."""
        return self.won

    def get_lost(self):
        """Returns True if the game has been lost."""
        return self.lost

    def set_neighbors(self):
        """Assigns neighbors to each piece on the board."""
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                neighbors = self.add_to_neighbors_list(row, col)
                self.board[row][col].set_neighbors(neighbors)

    def add_to_neighbors_list(self, row, col):
        """Generates a list of neighbors for a given piece."""
        return [self.board[r][c] for r in range(row - 1, row + 2) for c in range(col - 1, col + 2)
                if 0 <= r < self.size[0] and 0 <= c < self.size[1] and (r != row or c != col)]

    def set_num_around(self):
        """Calculates and sets the number of bombs around each piece."""
        for row in self.board:
            for piece in row:
                piece.set_num_around()