from enum import IntEnum
from random import choice


class Colors(IntEnum):
    ORANGE = 0xEE9900
    YELLOW = 0xDDEE00
    WHITE = 0xFFFFFF
    GREEN = 0x00FF55
    BLUE = 0x0088FF
    DARK_GREY = 0x444444
    BLACK = 0x000000

    @classmethod
    def random_color(cls):
        return choice(list(set(cls.__members__.values()) - {cls.DARK_GREY, cls.BLACK}))