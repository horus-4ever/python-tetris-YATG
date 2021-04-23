from board import Board
from .colors import Colors
import pygame


class GuiBoard(Board):
    """
    ## GuiBoard(Board) ##
    The gui component representing the game board.
    This class is an extension from the Board class.

    CLASS ATTRIBUTES
    ----------------
    PIXEL_SIZE: int
        the size of a pixel
    WIDGET_WIDTH: int
        the total width of the Board
    WIDGET_HEIGHT: int
        the total height of the Board
    [+inherited attributes from Board]
    
    ATTRIBUTES
    ----------
    [inherited attributes from Board]

    METHODS
    -------
    draw(self, surface: pygame.Surface, position: (int, int)) -> None:
        draw the widget on the given surface and at the given position
    draw_piece(self, piece: GuiPiece, surface: pygame.Surface, position: (int, int)) -> None:
        draw the given piece at the given position on the given surface
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