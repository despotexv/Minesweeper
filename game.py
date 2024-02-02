import pygame
import os
from board import Board
from solver import Solver
from time import sleep

class Game:
    """A Minesweeper game class that initializes the game board, handles user input, and renders the game using Pygame."""

    def __init__(self, size, prob):
        """Initializes the game with a given board size and bomb probability."""
        self.board = Board(size, prob)
        pygame.init()
        self.screen_size = 800, 800
        self.screen = pygame.display.set_mode(self.screen_size)
        self.piece_size = (self.screen_size[0] / size[1], self.screen_size[1] / size[0])
        self.load_pictures()
        self.solver = Solver(self.board)

    def load_pictures(self):
        """Loads and scales images for the game pieces."""
        self.images = {}
        images_directory = "images"
        for file_name in os.listdir(images_directory):
            if file_name.endswith(".png"):
                path = os.path.join(images_directory, file_name)
                img = pygame.image.load(path).convert()
                img = pygame.transform.scale(img, (int(self.piece_size[0]), int(self.piece_size[1])))
                self.images[file_name.split(".")[0]] = img

    def run(self):
        """Runs the game loop, handling events and updating the game state."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not (self.board.get_won() or self.board.get_lost()):
                    right_click = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handle_click(pygame.mouse.get_pos(), right_click)
                elif event.type == pygame.KEYDOWN:
                    self.solver.move()

            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            if self.board.get_won():
                self.win()
                running = False
        pygame.quit()

    def draw(self):
        """Draws the game board and pieces."""
        top_left = (0, 0)
        for row in self.board.get_board():
            for piece in row:
                rect = pygame.Rect(top_left, self.piece_size)
                image = self.images[self.get_image_string(piece)]
                self.screen.blit(image, top_left)
                top_left = top_left[0] + self.piece_size[0], top_left[1]
            top_left = (0, top_left[1] + self.piece_size[1])

    def get_image_string(self, piece):
        """Determines the appropriate image for a piece based on its state."""
        if piece.get_clicked():
            return str(piece.get_num_around()) if not piece.get_has_bomb() else 'bomb-at-clicked-block'
        if self.board.get_lost():
            return 'unclicked-bomb' if piece.get_has_bomb() else 'wrong-flag' if piece.get_flagged() else 'empty-block'
        return 'flag' if piece.get_flagged() else 'empty-block'

    def handle_click(self, position, flag):
        """Converts a screen position to a board index and handles the click."""
        index = tuple(int(pos // size) for pos, size in zip(position, self.piece_size))[::-1]
        self.board.handle_click(self.board.get_piece(index), flag)

    def win(self):
        """Plays a win sound and pauses for a moment when the game is won."""
        sound = pygame.mixer.Sound('win.wav')
        sound.play()
        sleep(3)