class Piece:
    """
    Represents a cell in Minesweeper. A cell can be a bomb, can be flagged, clicked,
    and knows about its neighboring cells.
    """

    def __init__(self, has_bomb):
        """
        Initializes a Piece object.

        :param has_bomb: Boolean indicating whether the piece contains a bomb.
        """
        self.has_bomb = has_bomb
        self.bombs_around = 0
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def __str__(self):
        """
        Provides a string representation of the Piece object.
        """
        return "B" if self.has_bomb else "0"

    def toggle_flag(self):
        """
        Toggles the flagged status of the piece.
        """
        self.flagged = not self.flagged

    def handle_click(self):
        """
        Marks the piece as clicked.
        """
        self.clicked = True

    def set_neighbors(self, neighbors):
        """
        Sets the neighboring pieces.

        :param neighbors: A list of neighboring Piece objects.
        """
        self.neighbors = neighbors

    def calculate_bombs_around(self):
        """
        Calculates the number of bombs in the adjacent pieces.
        """
        self.bombs_around = sum(1 for neighbor in self.neighbors if neighbor.has_bomb)

    # Property decorators for better encapsulation and readability
    @property
    def num_around(self):
        return self.bombs_around

    @property
    def is_bomb(self):
        return self.has_bomb

    @property
    def is_clicked(self):
        return self.clicked

    @property
    def is_flagged(self):
        return self.flagged

    @property
    def neighbors(self):
        return self.neighbors