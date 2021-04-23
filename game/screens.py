from .gui_board import GuiBoard
from .gui_piece import GuiPiece
from .scoring import Scoring
from .next_pieces import NextPieces
from .colors import Colors
import pygame
import numpy as np
from PIL import Image, ImageFilter


class GameScreen:
    SPEED = 500
    WIDGET_WIDTH = GuiBoard.WIDGET_WIDTH + NextPieces.WIDGET_WIDTH
    WIDGET_HEIGHT = GuiBoard.WIDGET_HEIGHT + Scoring.WIDGET_HEIGHT

    def __init__(self, layout):
        self.layout = layout
        self.current_piece = GuiPiece.random_piece()
        self.board = GuiBoard()
        self.scoring = Scoring()
        self.next_pieces = NextPieces()
        self.TICK_EVENT = pygame.USEREVENT + 1

    def enter(self):
        pygame.time.set_timer(self.TICK_EVENT, self.SPEED)

    def exit(self):
        pygame.time.set_timer(self.TICK_EVENT, 0)

    def on_event(self, event):
        if event.type == self.TICK_EVENT:
            return self.on_tick_event()
        return True

    def reset(self):
        self.board.reset()
        self.scoring.reset()

    def on_key_event(self, keyboard):
        piece = self.current_piece
        posx, posy = piece.position
        if keyboard[pygame.K_UP] and self.board.can_rotate(piece, 1):
            piece.rotate(1)
        elif keyboard[pygame.K_LEFT] and self.board.can_move(piece, (posx - 1, posy)):
            piece.move((posx - 1, posy))
        elif keyboard[pygame.K_RIGHT] and self.board.can_move(piece, (posx + 1, posy)):
            piece.move((posx + 1, posy))
        elif keyboard[pygame.K_DOWN] and self.board.can_move(piece, (posx, posy + 1)):
            piece.move((posx, posy + 1))
        elif keyboard[pygame.K_p]:
            self.layout.set_frame("pause_screen")

    def on_tick_event(self):
        posx, posy = self.current_piece.position
        if self.board.can_move(self.current_piece, (posx, posy + 1)):
            self.current_piece.move((posx, posy + 1))
        elif self.current_piece.position[1] == 0:
            self.layout.set_frame("lost_screen")
        else:
            self.board.fix(self.current_piece)
            self.current_piece = self.next_pieces.pop()
            deleted = self.board.strip()
            self.scoring.add_score(deleted)
        return True

    def draw(self, surface, position):
        surface.fill(Colors.BLACK)
        x, y = position
        self.scoring.draw(surface, (x, y))
        y += Scoring.WIDGET_HEIGHT
        self.board.draw(surface, (x, y))
        self.board.draw_piece(self.current_piece, surface, (x, y))
        pygame.draw.line(surface, Colors.WHITE, (0, y), (self.WIDGET_WIDTH, y), 2)
        x += GuiBoard.WIDGET_WIDTH
        pygame.draw.line(surface, Colors.WHITE, (x, 0), (x, self.WIDGET_HEIGHT), 2)
        self.next_pieces.draw(surface, (x, y))



class LostScreen:
    def __init__(self, layout):
        self.layout = layout
        self.img_array = None

    def enter(self):
        self.img_array = None

    def exit(self):
        self.img_array = None

    def on_event(self, event):
        return True

    def on_key_event(self, keyboard):
        if keyboard[pygame.K_SPACE]:
            self.layout["game_screen"].reset()
            self.layout.set_frame("game_screen")

    def draw(self, surface, position):
        if self.img_array is None:
            array = pygame.surfarray.pixels3d(surface)
            image = Image.fromarray(array)
            image = image.filter(ImageFilter.GaussianBlur(5))
            self.img_array = np.array(image)
        pygame.surfarray.blit_array(surface, self.img_array)


class PauseScreen:
    FONT = pygame.font.SysFont(None, 40)

    def __init__(self, layout):
        self.layout = layout
        self.img = None

    def enter(self):
        self.img = None

    def exit(self):
        self.img = None

    def on_event(self, event):
        return True

    def on_key_event(self, keyboard):
        if keyboard[pygame.K_p]:
            self.layout.set_frame("game_screen")

    def draw(self, surface, position):
        if self.img is None:
            array = pygame.surfarray.pixels3d(surface)
            image = Image.fromarray(array)
            image = image.filter(ImageFilter.GaussianBlur(5))
            self.img = pygame.surfarray.make_surface(np.array(image))
            del array # else : surface is locked
        surface.blit(self.img, position)
        width, height = surface.get_rect().width, surface.get_rect().height
        text = self.FONT.render("Pause", True, (200, 200, 200), Colors.BLACK)
        rect = text.get_rect(center=(width // 2, height // 2))
        rectangle = pygame.draw.rect(surface, Colors.DARK_GREY, (width // 2 - 60, height // 2 - 60, 120, 120), 3, 10)
        surface.fill(Colors.BLACK, rectangle)
        pygame.draw.rect(surface, Colors.LIGHT_GREY, (width // 2 - 60, height // 2 - 60, 120, 120), 2, 1)
        surface.blit(text, rect)