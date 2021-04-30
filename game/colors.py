from enum import IntEnum
from random import choice
from pygame import Color


class Colors(IntEnum):
    """
    Cette énumération contient les différentes couleurs utilisées dans le jeu.

    La méthode 'random_color' retourne une couleur aléatoire parmi les membres
    de l'énumération, à l'exception de cinq couleurs réservées (DARK_GREY,
    BLACK, WHITE, LIGHT_GREY et VERY_DARK_GREY).
    """
    ORANGE = Color(0xFF5500)
    YELLOW = Color(0xFFFF00)
    WHITE = Color(0xFFFFFF)
    GREEN = Color(0x00FF00)
    BLUE = Color(0x0099FF)
    RED = Color(0xFF0000)
    PURPLE = Color(0xEE00EE)
    DARK_GREY = Color(0x555555)
    VERY_DARK_GREY = Color(0x333333)
    LIGHT_GREY = Color(0xAAAAAA)
    BLACK = Color(0x000000)

    @classmethod
    def random_color(cls):
        return choice(list(set(cls.__members__.values()) - {cls.DARK_GREY, cls.BLACK, cls.WHITE, cls.LIGHT_GREY, cls.VERY_DARK_GREY}))