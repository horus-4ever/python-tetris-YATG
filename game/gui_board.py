from board import Board
from .colors import Colors
import pygame


class GuiBoard(Board):
    PIXEL_SIZE = 20
    WIDGET_WIDTH = Board.WIDTH * PIXEL_SIZE
    WIDGET_HEIGHT = Board.HEIGHT * PIXEL_SIZE

    def draw(self, surface, position):
        x, y = position
        pygame.draw.rect(surface, Colors.BLACK, (x, y, self.WIDTH, self.HEIGHT))
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                rectangle = (
                    x * self.PIXEL_SIZE,
                    y * self.PIXEL_SIZE,
                    self.PIXEL_SIZE,
                    self.PIXEL_SIZE
                )
                if self.board[y][x]:
                    pygame.draw.rect(surface, Colors.DARK_GREAY, rectangle)

    def draw_piece(self, piece, surface, position):
        piece.draw(surface, position, self.PIXEL_SIZE)