from board import Board
from .gui_piece import GuiPiece
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
        fake_piece = GuiPiece(piece.shape, Colors.VERY_DARK_GREY, piece.position, piece.rotation)
        posx, posy = fake_piece.position
        while self.can_move(fake_piece, (posx, posy + 1)):
            fake_piece.move((posx, posy + 1))
            posy += 1
        fake_piece.draw(surface, position, self.PIXEL_SIZE)
        piece.draw(surface, position, self.PIXEL_SIZE)