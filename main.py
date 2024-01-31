import sys
from game import Game

def main():
    if len(sys.argv) != 4:
        print("Usage: python filename.py width height bomb_probability")
        sys.exit(1)  # Exit the script with an error code

    try:
        size = (int(sys.argv[1]), int(sys.argv[2]))
        prob = float(sys.argv[3])
    except ValueError:
        print("Error: Please ensure width and height are integers, and bomb_probability is a float.")
        sys.exit(1)  # Exit the script with an error code

    g = Game(size, prob)
    g.run()