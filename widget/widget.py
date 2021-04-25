from .event import event, Event
import pygame


class Widget:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.mouse_was_hover = False
        self.mouse_button_was_down = False
        self.events = {}

    @event
    def on_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self._mouse_in(event):
                if not self.mouse_was_hover:
                    self.on_mouse_enter(event)
                    self.mouse_was_hover = True
                self.on_mouse_motion(event)
            else:
                if self.mouse_was_hover:
                    self.on_mouse_leave(event)
                self.mouse_was_hover = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self._mouse_in(event):
                if event.button == 1:
                    self.mouse_button_was_down = True
                    self.on_button_down(event)
                else:
                    self.mouse_button_was_down = False
            else:
                self.mouse_button_was_down = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if self._mouse_in(event):
                if event.button == 1:
                    if self.mouse_button_was_down:
                        self.on_click(event)
                    self.on_button_up(event)
            self.mouse_button_was_down = False
        elif event.type == pygame.KEYDOWN:
            self.on_key_down(self, event)

    def _mouse_in(self, event):
        return (self.position[0] <= event.pos[0] <= self.position[0] + self.size[0]
                and self.position[1] <= event.pos[1] <= self.position[1] + self.size[1])

    @event
    def draw(self, surface, position):
        pass

    @event
    def on_mouse_motion(self, event):
        pass

    @event
    def on_mouse_enter(self, event):
        pass

    @event
    def on_mouse_leave(self, event):
        pass

    @event
    def on_key_down(self, event):
        pass

    @event
    def on_click(self, event):
        pass

    @event
    def on_button_down(self, event):
        pass

    @event
    def on_button_up(self, event):
        pass