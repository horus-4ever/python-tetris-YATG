import pygame


class Scoring:
    """
    ## Scoring(object) ##
    The gui component containing the score info.

    CLASS ATTRIBUTES
    ----------------
    SCORE: dict[int, int]
        the mapping 'numbers of deleted lines' -> 'score'
    FONT: pygame.font.Font
        the font used to render the score
    WIDGET_HEIGHT: int
        the height of the widget

    ATTRIBUTES
    ----------
    score: int
        the current score

    METHODS
    -------
    add_score(self, score: int) -> None
        update the score
    draw(self, surface: pygame.Surface, position: (int, int))
        display the score board on the given surface at the given position
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

    def __init__(self):
        self.score = 0

    def reset(self):
        self.score = 0

    def draw(self, surface, position):
        posx, posy = position
        img = self.FONT.render(f"{self.score:04}", True, (255, 255, 255))
        surface.blit(img, (posx + 5, posy + 5))

    def add_score(self, score):
        four_lines, lines = divmod(score, 4)
        self.score += self.SCORES[4] * four_lines + self.SCORES[lines]