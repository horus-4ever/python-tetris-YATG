from pieces import Pieces, Piece
from .colors import Colors
import pygame


class GuiPiece(Piece):
    """
    Cette classe est une extension de la classe 'Piece' rajoutant la partie graphique.
    """
    def __init__(self, shape, color, position=(0, 0), rotation=0):
        super().__init__(shape, position, rotation)
        self.color = color

    @classmethod
    def random_piece(cls):
        shape = Pieces.random_shape()
        color = Colors.random_color()
        return cls(shape, color)

    def draw(self, surface, position, pixel_size):
        x_origin, y_origin = position
        posx, posy = self.position
        height, width = self.size
        matrix = self.matrix
        for x in range(width):
            for y in range(height):
                rectangle = (
                    x_origin + pixel_size * (posx + x),
                    y_origin + pixel_size * (posy + y),
                    pixel_size,
                    pixel_size
                )
                if matrix[y][x]:
                    pygame.draw.rect(surface, self.color, rectangle)
                    pygame.draw.rect(surface, Colors.BLACK, rectangle, 1)