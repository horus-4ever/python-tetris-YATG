from .gui_board import GuiBoard
from .gui_piece import GuiPiece
from .scoring import Scoring
from .next_pieces import NextPieces
from .colors import Colors
from .frame import Frame
import pygame
import numpy as np
from PIL import Image, ImageFilter


class GameScreen(Frame):
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.board.can_rotate(self.current_piece, 1):
                self.current_piece.rotate(1)
            elif event.key == pygame.K_p:
                self.layout.set_frame("pause_screen")
                return True
        return False

    def reset(self):
        self.board.reset()
        self.scoring.reset()

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



class LostScreen(Frame):
    TITLE_FONT = pygame.font.SysFont(None, 40)
    TEXT_FONT = pygame.font.SysFont(None, 20)

    def __init__(self, layout):
        self.layout = layout

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.layout["game_screen"].reset()
                self.layout.set_frame("game_screen")
                return True
        return False

    def draw(self, surface, position):
        surface.fill(Colors.BLACK)
        width, height = surface.get_rect().width, surface.get_rect().height
        title = self.TITLE_FONT.render("LOST !", True, (255, 255, 255), Colors.BLACK)
        text = self.TEXT_FONT.render("(press 'space' to start)", True, (255, 255, 255), Colors.BLACK)
        rect = title.get_rect(center=(width // 2, height // 2))
        surface.blit(title, rect)
        rect = text.get_rect(center=(width // 2, height // 2 + 40))
        surface.blit(text, rect)


class PauseScreen(Frame):
    FONT = pygame.font.SysFont(None, 30)
    TEXT = "PAUSE"

    def __init__(self, layout):
        self.layout = layout
        self.img = None

    def enter(self):
        self.img = None

    def exit(self):
        self.img = None

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.layout.set_frame("game_screen")
                return True
        return False

    def on_key_event(self, keyboard):
        pass

    def draw(self, surface, position):
        if self.img is None:
            array = pygame.surfarray.pixels3d(surface)
            image = Image.fromarray(array)
            image = image.filter(ImageFilter.GaussianBlur(10))
            self.img = pygame.surfarray.make_surface(np.array(image))
            del array # else : surface is locked
        surface.blit(self.img, position)
        width, height = surface.get_rect().size
        # render the text
        text = self.FONT.render(self.TEXT, True, (255, 255, 255), Colors.BLACK)
        text_size = max(self.FONT.size(self.TEXT))
        rect = text.get_rect(center=(width // 2, height // 2))
        where_to_draw = (
            width // 2 - text_size,
            height // 2 - text_size,
            text_size * 2,
            text_size * 2
        )
        rectangle = pygame.draw.rect(surface, Colors.DARK_GREY, where_to_draw, 3, 10)
        surface.fill(Colors.BLACK, rectangle)
        pygame.draw.rect(surface, Colors.LIGHT_GREY, where_to_draw, 3, 1)
        surface.blit(text, rect)