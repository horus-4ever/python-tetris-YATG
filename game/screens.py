from .gui_board import GuiBoard
from .gui_piece import GuiPiece
from .scoring import Scoring
from .next_pieces import NextPieces
from .colors import Colors
from .frame import Frame
from widget import Button
import pygame
import numpy as np
import random
import itertools
from PIL import Image, ImageFilter


class GameScreen(Frame):
    SPEED = 500
    WIDGET_WIDTH = GuiBoard.WIDGET_WIDTH + NextPieces.WIDGET_WIDTH
    WIDGET_HEIGHT = GuiBoard.WIDGET_HEIGHT + Scoring.WIDGET_HEIGHT

    def __init__(self, layout, position, size):
        self.position = position
        self.size = size
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.board.can_rotate(self.current_piece, 1):
                self.current_piece.rotate(1)
            elif event.key == pygame.K_p:
                self.layout.set_frame("pause_screen")
                return True
            elif event.key == pygame.K_SPACE:
                posx, posy = self.current_piece.position
                while self.board.can_move(self.current_piece, (posx, posy + 1)):
                    self.current_piece.move((posx, posy + 1))
                    posy += 1
            elif event.key == pygame.K_l:
                self.layout.set_frame("lost_screen")
                return True
        return False

    def reset(self):
        self.board.reset()
        self.scoring.reset()
        self.current_piece = GuiPiece.random_piece()

    def on_key_event(self, keyboard):
        piece = self.current_piece
        posx, posy = piece.position
        if keyboard[pygame.K_LEFT] and self.board.can_move(piece, (posx - 1, posy)):
            piece.move((posx - 1, posy))
        elif keyboard[pygame.K_RIGHT] and self.board.can_move(piece, (posx + 1, posy)):
            piece.move((posx + 1, posy))
        elif keyboard[pygame.K_DOWN] and self.board.can_move(piece, (posx, posy + 1)):
            piece.move((posx, posy + 1))

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


class MenuScreen(Frame):
    TITLE_FONT = pygame.font.SysFont(None, 40)
    TEXT_FONT = pygame.font.SysFont(None, 20)

    def __init__(self, layout, position, size):
        self.position = position
        self.size = size
        self.layout = layout
        self.image = pygame.image.load("assets/tetris.png")
        x, y = self.position
        width, height = self.size
        self.button = Button(
            (x + width // 2 - 100, y + height // 2 - 25 + 80),
            (200, 50),
            "Play",
            border_radius=5
        )
        self.button.on_click = lambda button, _: self.play()

    def play(self):
        self.layout["game_screen"].reset()
        self.layout.set_frame("game_screen")
        return True

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.play()
                return True
        if self.button.on_event(event):
            return True
        return False

    def draw(self, surface, position):
        surface.fill(Colors.BLACK)
        width, height = surface.get_rect().width, surface.get_rect().height
        title = self.TITLE_FONT.render("THE TETRIS GAME !", True, (255, 255, 255), Colors.BLACK)
        text = self.TEXT_FONT.render("(press 'space' to start)", True, (255, 255, 255), Colors.BLACK)
        rect = title.get_rect(center=(width // 2, height // 2))
        surface.blit(title, rect)
        rect = text.get_rect(center=(width // 2, height // 2 + 20))
        surface.blit(text, rect)
        image_rect = self.image.get_rect(center=(width // 2, height // 2 - 40 - self.image.get_rect().size[1] // 2))
        surface.blit(self.image, image_rect)
        self.button.draw(surface, (0, 0))


class LostScreen(Frame):
    TITLE_FONT = pygame.font.SysFont(None, 40)
    TEXT_FONT = pygame.font.SysFont(None, 20)

    def __init__(self, layout, position, size):
        self.position = position
        self.size = size
        self.layout = layout
        x, y = self.position
        width, height = self.size
        self.replay_button = Button(
            (x + width // 2 - 100, y + height // 2 - 25 + 80),
            (200, 50),
            "Play",
            border_radius=5
        )
        self.replay_button.on_click = lambda button, _: self.replay()
        self.menu_button = Button(
            (x + width // 2 - 100, y + height // 2 - 25 + 140),
            (200, 50),
            "Menu",
            border_radius=5,
            mouse_hover_color=Colors.GREEN, mouse_hover_font_color=(0, 255, 0)
        )
        self.menu_button.on_click = lambda button, _: self.menu()
        self.in_animation = False
        self.tick = 0
        self.positions1 = []
        self.positions2 = []

    def enter(self):
        self.in_animation = True
        self.tick = 0

    def menu(self):
        self.layout.set_frame("menu_screen")

    def replay(self):
        self.layout["game_screen"].reset()
        self.layout.set_frame("game_screen")

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.replay()
                return True
        self.menu_button.on_event(event)
        self.replay_button.on_event(event)
        return False

    def draw(self, surface, position):
        if self.in_animation:
            self._lost_animation(surface)
            self.tick += 1
        else:
            surface.fill(Colors.BLACK)
            width, height = surface.get_rect().width, surface.get_rect().height
            title = self.TITLE_FONT.render("LOST !", True, (255, 255, 255), Colors.BLACK)
            text = self.TEXT_FONT.render("(press 'space' to start)", True, (255, 255, 255), Colors.BLACK)
            rect = title.get_rect(center=(width // 2, height // 2))
            surface.blit(title, rect)
            rect = text.get_rect(center=(width // 2, height // 2 + 20))
            surface.blit(text, rect)
            self.replay_button.draw(surface, (0, 0))
            self.menu_button.draw(surface, (0, 0))

    def _lost_animation(self, surface):
        if self.tick == 0:
            width, height = surface.get_rect().size
            posx, posy = width // 2, height // 2
            self.positions1 = sorted(
                [(x, y) for x in range(0, width, 5) for y in range(0, height, 5)],
                key=(lambda pos: ((pos[0] - posx) ** 2 + (pos[1] - posy) ** 2) ** 0.5),
                reverse=True
            )
            self.positions2 = self.positions1[:]
        colors = [Colors.BLACK, Colors.DARK_GREY, Colors.LIGHT_GREY]
        for _ in range(200):
            if not self.positions2:
                self.in_animation = False
                break
            elif self.positions1:
                position = self.positions1.pop()
                surface.fill(Colors.random_color(), pygame.Rect(position, (10, 10)))
            if self.tick >= 1:
                position = self.positions2.pop()
                surface.fill(Colors.BLACK, pygame.Rect(position, (10, 10)))
        self.first_time = False


class PauseScreen(Frame):
    FONT = pygame.font.SysFont(None, 30)
    TEXT = "PAUSE"

    def __init__(self, layout, position, size):
        self.position = position
        self.size = size
        self.layout = layout
        self.first_time = False

    def enter(self):
        self.first_time = True

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.layout.set_frame("game_screen")
                return True
        return False

    def on_key_event(self, keyboard):
        pass

    def draw(self, surface, position):
        if not self.first_time:
            return
        else:
            self.first_time = False
        # get the current surface's image and blur it
        array = pygame.surfarray.pixels3d(surface)
        image = Image.fromarray(array)
        image = image.filter(ImageFilter.GaussianBlur(10))
        new_image = pygame.surfarray.make_surface(np.array(image))
        del array # else : surface is locked
        surface.blit(new_image, position)
        width, height = surface.get_rect().size
        # render the text box
        text = self.FONT.render(self.TEXT, True, (255, 255, 255))
        text_size = max(self.FONT.size(self.TEXT))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        where_to_draw = (
            width // 2 - text_size,
            height // 2 - text_size,
            text_size * 2,
            text_size * 2
        )
        surface.fill(Colors.BLACK, where_to_draw)
        pygame.draw.rect(surface, Colors.LIGHT_GREY, where_to_draw, 3, 1)
        surface.blit(text, text_rect)