from collections import deque
"""
from .gui_piece import GuiPiece
from .gui_board import GuiBoard
from .next_pieces import NextPieces
from .scoring import Scoring
"""
from .stackedlayout import StackedLayout
from .screens import GameScreen, LostScreen, PauseScreen, MenuScreen
from .colors import Colors
import pygame


class Game:
    """
    Cette classe représente la fenêtre de jeu du tetris.
    Elle est donc responsable de la boucle d'évènement ainsi que de la gestion des différentes parties graphiques.
    """
    FPS = 20
    WIDTH = GameScreen.WIDGET_WIDTH
    HEIGHT = GameScreen.WIDGET_HEIGHT

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.running = False
        # StackedLayout stockant les quatre principales frames du jeu
        self.layout = StackedLayout()
        self.game_frame = GameScreen(self.layout, (0, 0), (self.WIDTH, self.HEIGHT))
        self.lost_frame = LostScreen(self.layout, (0, 0), (self.WIDTH, self.HEIGHT))
        self.pause_frame = PauseScreen(self.layout, (0, 0), (self.WIDTH, self.HEIGHT))
        self.menu_frame = MenuScreen(self.layout, (0, 0), (self.WIDTH, self.HEIGHT))
        self.layout.add_frames(
            game_screen=self.game_frame,
            lost_screen=self.lost_frame,
            pause_screen=self.pause_frame,
            menu_screen=self.menu_frame
        )
        self.layout.set_frame("menu_screen")

    def run(self):
        self.running = True
        while self.running:
            frame_changed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    frame_changed = self.layout.on_event(event)
            keyboard = pygame.key.get_pressed()
            if any(keyboard) and not frame_changed:
                self.layout.on_key_event(keyboard)
            self.layout.draw(self.window, (0, 0))
            self.clock.tick(self.FPS)
            pygame.display.update()