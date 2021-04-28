from numpy import array
from random import choice


I = array([
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])


O = array([
    [1, 1],
    [1, 1]
])


T = array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 0]
])


L = array([
    [0, 0, 0],
    [1, 1, 1],
    [1, 0, 0]
])


J = array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 1]
])


Z = array([
    [0, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
])


S = array([
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0]
])


class Pieces:
    """
    Cette classe fait office d'énumération et contient les différentes
    formes (des matrices numpy) des tetriminos.
    La méthode 'random_shape' permet de sélectionner l'une de ces formes
    aléatoirement.
    """

    TETRIMINO_I = I
    TETRIMINO_O = O
    TETRIMINO_T = T
    TETRIMINO_L = L
    TETRIMINO_J = J
    TETRIMINO_Z = Z
    TETRIMINO_S = S

    __members__ = (I, O, T, L, J, Z, S)
    @classmethod
    def random_shape(cls):
        return choice(cls.__members__)