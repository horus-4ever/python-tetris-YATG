import pygame
pygame.init()
pygame.font.init()


from game.game import Game

# TODO: place widgets at their creations (for fixed widgets only)

game = Game()
game.run()