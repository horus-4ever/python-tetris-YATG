import pygame
from .gui_board import GuiBoard


class Scoring:
    """
    Cette classe représente la gestion du score.

    Le système de score est très simple :
    - au début, le score est à 0, et le level est à 1
    - toutes les 'level * 5' lignes supprimées, le level est incrémenté de 1
    - le level agit comme un multiplicateur du score :
        - 1 lignes supprimées = 'level * 40' points
        - 2 lignes supprimées = 'level * 100' points
        - 3 lignes supprimées = 'level * 300' points
        - 4 lignes supprimées (tetris) = 'level * 1200' points
        - n lignes supprimées, division euclidienne par 4
    """
    SCORES = {
        0: 0,
        1: 40,
        2: 100,
        3: 300,
        4: 1200
    }
    FONT = pygame.font.SysFont(None, 40)
    WIDGET_HEIGHT = 50
    WIDGET_WIDTH = GuiBoard.WIDGET_WIDTH

    def __init__(self):
        self.score = 0
        self.level = 1
        self.deleted_lines = 0

    def reset(self):
        self.score = 0
        self.level = 1
        self.deleted_lines = 0

    def draw(self, surface, position):
        posx, posy = position
        img = self.FONT.render(f"Lvl {self.level} : {self.score:04}", True, (255, 255, 255))
        rect = img.get_rect(center=(self.WIDGET_WIDTH // 2, self.WIDGET_HEIGHT // 2))
        surface.blit(img, rect)

    def add_score(self, deleted_lines):
        four_lines, lines = divmod(deleted_lines, 4)
        self.score += (self.SCORES[4] * four_lines) * self.level + self.SCORES[lines] * self.level
        self.deleted_lines += deleted_lines
        if self.deleted_lines >= 5 * self.level:
            self.deleted_lines %= 5 * self.level
            self.level += 1