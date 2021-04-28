#!/usr/bin/python3
# INP 1A Nancy Tetris

import pygame
pygame.init()
pygame.font.init()


from game.game import Game


game = Game()
game.run()