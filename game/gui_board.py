from board import Board
from .colors import Colors
import pygame


class GuiBoard(Board):
    """
    Cette classe est une extension de la classe 'Board', ajoutant une surcouche graphique.
    """
    PIXEL_SIZE = 30
    WIDGET_WIDTH = Board.WIDTH * PIXEL_SIZE
    WIDGET_HEIGHT = Board.HEIGHT * PIXEL_SIZE

    def draw(self, surface, position):
        posx, posy = position
        pygame.draw.rect(surface, Colors.BLACK, (posx, posy, self.WIDTH, self.HEIGHT))
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                rectangle = (
                    posx + x * self.PIXEL_SIZE,
                    posy + y * self.PIXEL_SIZE,
                    self.PIXEL_SIZE,
                    self.PIXEL_SIZE
                )
                if self.board[y][x]:
                    pygame.draw.rect(surface, Colors.DARK_GREY, rectangle)

    def draw_piece(self, piece, surface, position):
        piece.draw(surface, position, self.PIXEL_SIZE)