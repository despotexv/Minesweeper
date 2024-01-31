class Piece:
    """
    Represents a piece on the Minesweeper board. A piece can have a bomb, be clicked, be flagged, 
    and knows about its neighbors.
    """

    def __init__(self, has_bomb):
        """
        Initializes a piece with or without a bomb.
        
        :param has_bomb: Boolean indicating if the piece contains a bomb.
        """
        self.has_bomb = has_bomb
        self.around_bombs = 0
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def __str__(self):
        """
        Returns a string representation of the piece.
        """
        return 'B' if self.has_bomb else 'E'

    def toggle_flag(self):
        """
        Toggles the flagged state of the piece.
        """
        self.flagged = not self.flagged

    def handle_click(self):
        """
        Marks the piece as clicked.
        """
        if not self.flagged:  # Prevent clicking a flagged piece
            self.clicked = True

    def set_neighbors(self, neighbors):
        """
        Sets the neighboring pieces.
        
        :param neighbors: List of neighboring Piece instances.
        """
        self.neighbors = neighbors

    def calculate_bombs_around(self):
        """
        Calculates the number of bombs in neighboring pieces.
        """
        self.around_bombs = sum(neighbor.has_bomb for neighbor in self.neighbors)

    # Properties for accessing piece attributes
    @property
    def num_around(self):
        return self.around_bombs

    @property
    def has_bomb(self):
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