import numpy as np


class Piece:
    """
    ## Piece(object) ##
    A class used to represent a tetrimino.

    ATTRIBUTES
    ----------
    shape: np.array
        the shape of the tetrimino
    position: tuple[int, int]
        the position of the tetrimino on the board
    rotation: int
        the rotation of the tetrimino

    PROPERTIES
    ----------
    size (getter only): tuple[int, int]
        the shape of the np.array representing the tetrimino
    matrix (getter only): np.array
        returns a copy of the shape np.array, with the applied rotation

    METHODS
    -------
    rotate(self, n=1)
        add n to the current rotation
    move(self, position)
        change the current position of the tetrimino
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
