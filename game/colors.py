from enum import IntEnum
from random import choice
from pygame import Color


class Colors(IntEnum):
    """
    ## Colors(IntEnum) ##
    The enumeration of all colors used in the game.

    CLASSMETHODS
    ------------
    random_color(cls) -> int:
        returns a random color from the members of the enumeration.
        The random color cannot be one of the 3 following reserved colors : DARK_GREY, BLACK and WHITE
    """
    ORANGE = Color(0xAADD00)
    YELLOW = Color(0xFFFF00)
    WHITE = Color(0xFFFFFF)
    GREEN = Color(0x00FF00)
    BLUE = Color(0x0099FF)
    RED = Color(0xFF3333)
    PURPLE = Color(0xEE00EE)
    DARK_GREY = Color(0x555555)
    LIGHT_GREY = Color(0xAAAAAA)
    BLACK = Color(0x000000)
    """
    ORANGE = Color(238, 153, 0)
    YELLOW = Color(221, 238, 0)
    WHITE = Color(255, 255, 255)
    GREEN = Color(0, 255, 51)
    BLUE = Color(0, 136, 255)
    RED = Color(255, 51, 51)
    PURPLE = Color(238, 0, 238)
    DARK_GREY = Color(68, 68, 68)
    LIGHT_GREY = Color(170, 170, 170)
    # BLACK = Color(0, 0, 0)
    """

    @classmethod
    def random_color(cls):
        return choice(list(set(cls.__members__.values()) - {cls.DARK_GREY, cls.BLACK, cls.WHITE, cls.LIGHT_GREY}))