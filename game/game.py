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
    ## Game(object) ##
    A class representing the tetris game in itself.
    This class contains the GUI of the game.

    CLASS ATTRIBUTES
    ----------------
    WIDTH: int
        width of the pygame window, based on the width of the sub-widgets
    HEIGHT: int
        height of the pygame window, based on the height of the sub-widgets
    FPS: int
        number of frame per seconds
    SPEED: int
        the timelapse between two ticks, in milliseconds

    ATTRIBUTES
    ----------
    window: pygame.Surface
        the window of the game
    clock: pygame.time.Clock
        the clock used to set the FPS limit
    TICK_EVENT: int
        a custom event number
    current_pieces: GuiPiece
        the current tetrimino displayed on the screen
    next_pieces: NextPieces
        the gui component containing the next tetriminos to be played
    scoring: Scoring
        the gui component displaying the score
    board: GuiBoard
        the gui component representing the game board
    running: bool
        boolean representing the state of the game

    METHODS
    -------
    run(self) -> None:
        run the game : this function contains the event loop
    draw_all(self) -> None:
        draw all gui components on the screen : the board, the current tetrimino and the next tetriminos
    [private] _on_key_event(self, key: int) -> None:
        callback when a key is pressed
    [private] _on_tick(self) -> None:
        callback when the 'TICK_EVENT' occurs : update the game
    """
    FPS = 20
    WIDTH = GameScreen.WIDGET_WIDTH
    HEIGHT = GameScreen.WIDGET_HEIGHT

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
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
        self.running = True

    def run(self):
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