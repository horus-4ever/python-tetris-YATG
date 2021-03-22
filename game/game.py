from collections import deque
from .gui_piece import GuiPiece
from .gui_board import GuiBoard
from .next_pieces import NextPieces
from .colors import Colors
import pygame


class Game:
    WIDTH = GuiBoard.WIDGET_WIDTH + NextPieces.WIDGET_WIDTH
    HEIGHT = GuiBoard.WIDGET_HEIGHT
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
        self.board.draw(self.window, (x, y))
        self.board.draw_piece(self.current_piece, self.window, (x, y))
        x += GuiBoard.WIDGET_WIDTH
        pygame.draw.line(self.window, Colors.WHITE, (x, y), (x, y + self.HEIGHT), 2)
        self.next_pieces.draw(self.window, (x, y))

    def _on_tick(self):
        posx, posy = self.current_piece.position
        if self.board.can_move(self.current_piece, (posx, posy + 1)):
            self.current_piece.move((posx, posy + 1))
        elif self.current_piece.position[1] == 0:
            print("lost")
            self.running = False
        else:
            self.board.fix(self.current_piece)
            self.current_piece = self.next_pieces.pop()
            self.board.strip()

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
        