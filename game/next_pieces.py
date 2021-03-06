import pygame
import numpy as np
from collections import deque
from .colors import Colors
from .gui_piece import GuiPiece


class NextPieces:
    """
    Cette classe représente la gestion et l'affichage des tetriminos à venir.
    Les trois tetriminos sont placés dans un deque.
    """
    NUMBER = 3
    PIXEL_SIZE = 15
    MAX_PIECE_WIDTH = 4
    PADDING = 5
    MARGIN = 15
    PLACEHOLDER_SIZE = MAX_PIECE_WIDTH * PIXEL_SIZE + 2 * PADDING
    WIDGET_WIDTH = 2 * MARGIN + (PLACEHOLDER_SIZE)
    WIDGET_HEIGHT = (NUMBER + 1) * MARGIN + (NUMBER * (PLACEHOLDER_SIZE))

    def __init__(self):
        self.pieces = deque(GuiPiece.random_piece() for _ in range(self.NUMBER))

    def pop(self):
        piece = self.pieces.popleft()
        self.pieces.append(GuiPiece.random_piece())
        return piece

    def _draw_placeholder(self, surface, positition, color):
        # le placeholder correspond au carré contenant un aperçu de la pièce à venir
        x, y = positition
        square_size = self.PLACEHOLDER_SIZE
        pygame.draw.rect(surface, color, (x, y, square_size, square_size), 2, 10)

    def _draw_piece(self, surface, piece, position):
        posx, posy = position
        height, width = piece.size
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
                    pygame.draw.rect(surface, Colors.BLACK, rectangle, 1)

    def draw(self, surface, position):
        posx, posy = position
        posx, posy = posx + self.MARGIN, posy + self.MARGIN
        for piece in self.pieces:
            # on supprimes toutes les lignes contenant uniquement des 0
            # on créé ensuite une fausse pièce contenant la matrice modifiée
            # cela permet de pouvoir correctement centrer la pièce au sein du placeholder
            new_shape = piece.shape[~np.all(piece.shape == 0, axis=1)]
            new_piece = GuiPiece(new_shape, piece.color, piece.position, piece.rotation)
            height, width = new_shape.shape
            x, y = (
                posx + (1 - width / self.MAX_PIECE_WIDTH) * self.PIXEL_SIZE * 2 + self.PADDING,
                posy + (1 - height / self.MAX_PIECE_WIDTH) * self.PIXEL_SIZE * 2 + self.PADDING
            )
            self._draw_placeholder(surface, (posx, posy), piece.color)
            self._draw_piece(surface, new_piece, (x, y))
            posy += self.PLACEHOLDER_SIZE + self.MARGIN