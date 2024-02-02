import pyautogui

class Solver:
    """A solver for Minesweeper, automating moves based on current board state."""

    def __init__(self, board):
        """
        Initializes the solver with a game board.

        Parameters:
        - board: The game board object, which the solver will interact with.
        """
        self.board = board

    def move(self):
        """Evaluates and performs moves on the Minesweeper board based on its current state."""
        for row in self.board.get_board():
            for piece in row:
                if not piece.get_clicked():
                    continue  # Skip already clicked (revealed) pieces

                around = piece.get_num_around()  # Bombs around the current piece
                unknown, flagged = 0, 0  # Count of unknown and flagged pieces around the current piece
                neighbors = piece.get_neighbors()  # Neighboring pieces

                for p in neighbors:
                    if not p.get_clicked():
                        unknown += 1
                    if p.get_flagged():
                        flagged += 1

                # If the number of bombs around a piece equals the number of flagged neighbors, open the rest
                if around == flagged:
                    self.open_unflagged(neighbors)

                # If the number of unknown pieces around a piece equals the number of bombs, flag all unknown pieces
                if around == unknown:
                    self.flag_all(neighbors)

    def open_unflagged(self, neighbors):
        """
        Opens all unflagged neighboring pieces.

        Parameters:
        - neighbors: A list of neighboring piece objects.
        """
        for piece in neighbors:
            if not piece.get_flagged():
                # Simulate a click on the unflagged piece
                self.board.handle_click(piece, False)

    def flag_all(self, neighbors):
        """
        Flags all unflagged neighboring pieces.

        Parameters:
        - neighbors: A list of neighboring piece objects.
        """
        for piece in neighbors:
            if not piece.get_flagged():
                # Simulate a right-click to flag the piece
                self.board.handle_click(piece, True)