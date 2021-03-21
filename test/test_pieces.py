import unittest

from pieces import Piece, Pieces
import numpy as np


class TestPieces(unittest.TestCase):
    def test_rotation(self):
        random_piece = Piece(Pieces.random_shape(), (0, 0), rotation=0)
        self.assertEqual(random_piece.rotation, 0)
        random_piece.rotate(2)
        self.assertEqual(random_piece.rotation, 2)
        random_piece.rotate(-3)
        self.assertEqual(random_piece.rotation, 3)

    def test_shape(self):
        piece = Piece(Pieces.TETRIMINO_I, (0, 0), 0)
        # rotation, by 1
        piece.rotate(1)
        expected_matrix1 = np.array([
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ])
        self.assertTrue((piece.matrix == expected_matrix1).all())
        # rotation +1
        piece.rotate(1)
        expected_matrix2 = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ])
        self.assertTrue((piece.matrix == expected_matrix2).all())