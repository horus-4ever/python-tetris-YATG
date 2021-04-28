import numpy as np


class Board:
    """
    Cette classe représente la plateau de jeu non graphique du tetris.
    """
    WIDTH = 10
    HEIGHT = 22

    def __init__(self):
        self.board = np.zeros(shape=(self.HEIGHT, self.WIDTH), dtype=int)

    def reset(self):
        self.board = np.zeros(shape=(self.HEIGHT, self.WIDTH), dtype=int)

    def can_rotate(self, piece: 'Piece', n: int) -> bool:
        fake_matrix = np.rot90(piece.matrix, n)
        return self._can_play(fake_matrix, piece.position, piece.size)

    def can_move(self, piece: 'Piece', position: (int, int)) -> bool:
        fake_position = (piece.position[0], piece.position[1] + 1)
        return self._can_play(piece.matrix, position, piece.size)
    
    def _can_play(self, matrix: np.array, piece_position: (int, int), piece_size: (int, int)) -> bool:
        width, height = piece_size
        posx, posy = piece_position
        for x in range(posx, posx + width):
            for y in range(posy, posy + height):
                data = matrix[y - posy][x - posx]
                if data and (x > self.WIDTH - 1 or y > self.HEIGHT - 1 or x < 0 or y < 0):
                    return False
                elif data and self.board[y][x]:
                    return False
        return True

    def fix(self, piece: 'Piece'):
        posx, posy = piece.position
        width, height = piece.size
        max_xbound = min((posx + width), self.WIDTH)
        max_ybound = min((posy + height), self.HEIGHT)
        for x in range(posx, max_xbound):
            for y in range(posy, max_ybound):
                self.board[y][x] |= piece.matrix[y - posy][x - posx]
    
    def strip(self) -> int:
        counter = 0
        new_board = self.board.copy()
        for i, line in enumerate(self.board):
            if all(line):
                new_board[1:i+1] = new_board[0:i]
                counter += 1
        self.board = new_board
        return counter