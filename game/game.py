from collections import deque
from .gui_piece import GuiPiece
from .gui_board import GuiBoard
from .next_pieces import NextPieces
from .scoring import Scoring
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
    WIDTH = GuiBoard.WIDGET_WIDTH + NextPieces.WIDGET_WIDTH
    HEIGHT = GuiBoard.WIDGET_HEIGHT + Scoring.WIDGET_HEIGHT
    FPS = 20
    SPEED = 500

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.TICK_EVENT = pygame.USEREVENT + 1
        self.running = True
        self.current_piece = GuiPiece.random_piece()
        self.next_pieces = NextPieces()
        self.board = GuiBoard()
        self.scoring = Scoring()

    def run(self):
        pygame.time.set_timer(self.TICK_EVENT, self.SPEED)
        while self.running:
            self.window.fill(Colors.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == self.TICK_EVENT:
                    self._on_tick()
            keyboard = pygame.key.get_pressed()
            for key, state in enumerate(keyboard):
                if state:
                    self._on_key_event(key)
            self.draw_all()
            self.clock.tick(self.FPS)
            pygame.display.update()

    def draw_all(self):
        x, y = (0, 0)
        self.scoring.draw(self.window, (x, y))
        y += Scoring.WIDGET_HEIGHT
        self.board.draw(self.window, (x, y))
        self.board.draw_piece(self.current_piece, self.window, (x, y))
        pygame.draw.line(self.window, Colors.WHITE, (0, y), (self.WIDTH, y), 2)
        x += GuiBoard.WIDGET_WIDTH
        pygame.draw.line(self.window, Colors.WHITE, (x, 0), (x, self.HEIGHT), 2)
        self.next_pieces.draw(self.window, (x, y))

    def _on_tick(self):
        posx, posy = self.current_piece.position
        if self.board.can_move(self.current_piece, (posx, posy + 1)):
            self.current_piece.move((posx, posy + 1))
        elif self.current_piece.position[1] == 0:
            # TODO : add proper end of game
            print("lost")
            self.running = False
        else:
            self.board.fix(self.current_piece)
            self.current_piece = self.next_pieces.pop()
            deleted = self.board.strip()
            self.scoring.add_score(deleted)

    def _on_key_event(self, key):
        piece = self.current_piece
        posx, posy = piece.position
        if key == pygame.K_UP and self.board.can_rotate(piece, 1):
            piece.rotate(1)
        elif key == pygame.K_LEFT and self.board.can_move(piece, (posx - 1, posy)):
            piece.move((posx - 1, posy))
        elif key == pygame.K_RIGHT and self.board.can_move(piece, (posx + 1, posy)):
            piece.move((posx + 1, posy))
        elif key == pygame.K_DOWN and self.board.can_move(piece, (posx, posy + 1)):
            piece.move((posx, posy + 1))
        