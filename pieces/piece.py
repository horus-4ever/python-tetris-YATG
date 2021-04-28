import numpy as np


class Piece:
    """
    Cette classe représente un tetrimino.
    Un tetrimino est simplement défini par une matrice 'shape',
    une position sur le plateau de jeu, ainsi qu'une rotation.
    L'information sur la couleur du tetrimino est laissé à la
    partie graphique, dans 'gui_piece'.
    """
    
    def __init__(self, shape, position, rotation=0):
        self.shape = shape
        self.position = position
        self.rotation = rotation % 4

    @property
    def size(cls):
        return cls.shape.shape

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value: int):
        self._rotation = value % 4

    @property
    def matrix(self) -> np.array:
        return np.rot90(self.shape, self.rotation)
    
    def rotate(self, n=1):
        self.rotation += n

    def move(self, position: (int, int)):
        self.position = position
