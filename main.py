import sys
from game import Game

def main():
    """
    Main function to start the Minesweeper game.

    Expects three command-line arguments:
    - Width of the game board
    - Height of the game board
    - Probability of a mine being present in a cell
    """
    # Verifying the number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <width> <height> <mine_probability>")
        sys.exit(1)

    try:
        # Parse the command-line arguments
        size = (int(sys.argv[1]), int(sys.argv[2]))
        prob = float(sys.argv[3])

        # Ensure the probability is between 0 and 1
        if not 0 <= prob <= 1:
            raise ValueError("Mine probability must be between 0 and 1.")

        # Initialize and run the game
        game = Game(size, prob)
        game.run()

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(2)

if __name__ == '__main__':
    main()