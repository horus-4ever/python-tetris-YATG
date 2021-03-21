import unittest

from pieces import Piece, Pieces
from board import Board


class TestBoard(unittest.TestCase):
    def test_can_rotate(self):
        piece = Piece(Pieces.TETRIMINO_I, position=(-1, 0), rotation=1)
        board = Board()
        self.assertFalse(board.can_rotate(piece, 1))