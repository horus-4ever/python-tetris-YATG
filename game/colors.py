from enum import IntEnum
from random import choice


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
    ORANGE = 0xEE9900
    YELLOW = 0xDDEE00
    WHITE = 0xFFFFFF
    GREEN = 0x00FF33
    BLUE = 0x0088FF
    RED = 0xFF3333
    PURPLE = 0xFF00FF
    DARK_GREY = 0x444444
    LIGHT_GREY = 0xaaaaaa
    BLACK = 0x000000

    @classmethod
    def random_color(cls):
        return choice(list(set(cls.__members__.values()) - {cls.DARK_GREY, cls.BLACK, cls.WHITE, cls.LIGHT_GREY}))