import pygame
from collections import deque
from .colors import Colors
from .gui_piece import GuiPiece


class NextPieces:
    """
    ## NextPieces(object) ##
    The gui component of the tetris game representing the next tetriminos to be played

    ATTRIBUTES
    ----------
    pieces: collections.deque[GuiPiece]
        the queue of the next tetriminos to be played
    
    METHODS
    -------
    pop(self) -> GuiPiece:
        pop off the queue the next tetrimino to be played, and push a new random tetrimino
    draw(self, surface: pygame.Surface, position: (int, int)) -> None:
        draw the widget on the given surface

    """
    NUMBER = 3
    PIXEL_SIZE = 15
    MAX_PIECE_WIDTH = 4
    PADDING = 5
    MARGIN = 10
    PLACEHOLDER_SIZE = MAX_PIECE_WIDTH * PIXEL_SIZE + 2 * PADDING
    WIDGET_WIDTH = 2 * MARGIN + (PLACEHOLDER_SIZE)
    WIDGET_HEIGHT = (NUMBER + 1) * MARGIN + (NUMBER * (PLACEHOLDER_SIZE))

    def __init__(self):
        self.pieces = deque(GuiPiece.random_piece() for _ in range(self.NUMBER))

    def pop(self):
        piece = self.pieces.popleft()
        self.pieces.append(GuiPiece.random_piece())
        return piece

    def _draw_placeholder(self, surface, positition):
        x, y = positition
        color = Colors.DARK_GREY
        square_size = self.PLACEHOLDER_SIZE
        pygame.draw.line(surface, color, (x, y), (x + square_size, y))
        pygame.draw.line(surface, color, (x, y), (x, y + square_size))
        pygame.draw.line(surface, color, (x + square_size, y), (x + square_size, y + square_size))
        pygame.draw.line(surface, color, (x, y + square_size), (x + square_size, y + square_size))

    def _draw_piece(self, surface, piece, position):
        posx, posy = position
        width, height = piece.size
        for x in range(width):
            for y in range(height):
                if piece.shape[y][x]:
                    rectangle = (
                        posx + x * self.PIXEL_SIZE,
                        posy + y * self.PIXEL_SIZE,
                        self.PIXEL_SIZE,
                        self.PIXEL_SIZE
                    )
                    pygame.draw.rect(surface, piece.color, rectangle)

    def draw(self, surface, position):
        posx, posy = position
        posx, posy = posx + self.MARGIN, posy + self.MARGIN
        for piece in self.pieces:
            width, height = piece.size
            x, y = posx + (self.MAX_PIECE_WIDTH - width) // 2 + self.PADDING, posy + (self.MAX_PIECE_WIDTH - height) // 2 + self.PADDING
            self._draw_placeholder(surface, (posx, posy))
            self._draw_piece(surface, piece, (x, y))
            posy += self.PLACEHOLDER_SIZE + self.MARGIN