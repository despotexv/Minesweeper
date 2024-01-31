import pygame
import os
from board import Board
from solver import Solver
from time import sleep

class Game:
    def __init__(self, size, prob):
        """Initialize the game with a board size and bomb probability."""
        self.board = Board(size, prob)
        pygame.init()
        self.screen_size = (800, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.piece_size = (self.screen_size[0] / size[1], self.screen_size[1] / size[0])
        self.load_images()
        self.solver = Solver(self.board)

    def load_images(self):
        """Load and scale images for the game pieces."""
        self.images = {}
        images_directory = "images"
        for file_name in os.listdir(images_directory):
            if file_name.endswith(".png"):
                path = os.path.join(images_directory, file_name)
                image = pygame.image.load(path).convert()
                image = pygame.transform.scale(image, (int(self.piece_size[0]), int(self.piece_size[1])))
                self.images[file_name.split(".")[0]] = image

    def run(self):
        """Main game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not (self.board.getWon() or self.board.getLost()):
                    right_click = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handle_click(pygame.mouse.get_pos(), right_click)
                elif event.type == pygame.KEYDOWN:
                    self.solver.move()

            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            if self.board.getWon():
                self.win()
                running = False

        pygame.quit()

    def draw(self):
        """Draw the board and pieces."""
        top_left = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                rect = pygame.Rect(top_left, self.piece_size)
                image_key = self.get_image_key(piece)
                self.screen.blit(self.images[image_key], top_left) 
                top_left = (top_left[0] + self.piece_size[0], top_left[1])
            top_left = (0, top_left[1] + self.piece_size[1])

    def get_image_key(self, piece):
        """Determine the correct image for a piece based on its state."""
        if piece.getClicked():
            return str(piece.getNumAround()) if not piece.getHasBomb() else 'bomb-at-clicked-block'
        if self.board.getLost():
            if piece.getHasBomb():
                return 'unclicked-bomb'
            return 'wrong-flag' if piece.getFlagged() else 'empty-block'
        return 'flag' if piece.getFlagged() else 'empty-block'

    def handle_click(self, position, flag):
        """Handle a click event at a given position."""
        index = tuple(int(pos // size) for pos, size in zip(position, self.piece_size))[::-1]
        self.board.handleClick(self.board.getPiece(index), flag)

    def win(self):
        """Play a win sound and pause."""
        sound = pygame.mixer.Sound('sound.wav')
        sound.play()
        sleep(3)