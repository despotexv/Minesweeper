class Piece:
    """Represents a single piece on the Minesweeper board, which could be a bomb or safe spot."""

    def __init__(self, has_bomb):
        """
        Initializes a new piece.

        Parameters:
        - has_bomb (bool): Indicates whether this piece contains a bomb.
        """
        self.has_bomb = has_bomb
        self.around = 0  # Number of bombs around this piece
        self.clicked = False
        self.flagged = False
        self.neighbors = []  # Adjacent pieces

    def __str__(self):
        """Returns a string representation of the piece, primarily for debugging."""
        return 'B' if self.has_bomb else ' '

    def get_num_around(self):
        """Returns the number of bombs around this piece."""
        return self.around

    def get_has_bomb(self):
        """Returns True if this piece contains a bomb, False otherwise."""
        return self.has_bomb

    def get_clicked(self):
        """Returns True if the piece has been clicked (revealed), False otherwise."""
        return self.clicked

    def get_flagged(self):
        """Returns True if the piece has been flagged by the player, False otherwise."""
        return self.flagged

    def toggle_flag(self):
        """Toggles the flagged state of this piece."""
        self.flagged = not self.flagged

    def handle_click(self):
        """Marks the piece as clicked (revealed)."""
        self.clicked = True

    def set_num_around(self):
        """Calculates and sets the number of bombs in the adjacent pieces."""
        self.around = sum(1 for neighbor in self.neighbors if neighbor.get_has_bomb())

    def set_neighbors(self, neighbors):
        """
        Sets the adjacent pieces (neighbors) of this piece.

        Parameters:
        - neighbors (list[Piece]): A list of adjacent pieces.
        """
        self.neighbors = neighbors

    def get_neighbors(self):
        """Returns the adjacent pieces (neighbors) of this piece."""
        return self.neighbors