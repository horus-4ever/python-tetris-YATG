from numpy import array
from random import choice
from .piece import Piece


class I(Piece):
    SHAPE = array([
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])


class O(Piece):
    SHAPE = array([
        [1, 1],
        [1, 1]
    ])


class T(Piece):
    SHAPE = array([
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])


class L(Piece):
    SHAPE = array([
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ])


class J(Piece):
    SHAPE = array([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 1]
    ])


class Z(Piece):
    SHAPE = array([
        [0, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ])


class S(Piece):
    SHAPE = array([
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ])


class Pieces:
    __members__ = (I.SHAPE, O.SHAPE, T.SHAPE, L.SHAPE, J.SHAPE, Z.SHAPE, S.SHAPE)
    @classmethod
    def random_shape(cls):
        return choice(cls.__members__)