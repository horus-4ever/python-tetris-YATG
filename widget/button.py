from .widget import Widget
from .event import event
import pygame


class Button(Widget):
    def __init__(self, position, size, text, font_size=25, **attributes):
        super().__init__(position, size)
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)
        self.attributes = attributes
    
    def draw(self, surface, position):
        px, py = position
        widgetx, widgety = self.position
        width, height = self.size
        rectangle = pygame.Rect(
            px + widgetx,
            py + widgety,
            width,
            height
        )
        # attributes
        bgcolor = self.attributes.get("bgcolor", (0, 0, 0))
        font_color = self.attributes.get("font_color", (255, 255, 255))
        border_color = self.attributes.get("border_color", (255, 255, 255))
        border_width = self.attributes.get("border_width", 2)
        border_radius = self.attributes.get("border_radius", 0)
        # text
        rendered_text = self.font.render(self.text, True, font_color)
        rendered_text_rect = rendered_text.get_rect(center=(
            (px + widgetx + width // 2),
            (py + widgety + height // 2)
        ))
        # draw
        surface.fill(bgcolor, rectangle)
        pygame.draw.rect(surface, border_color, rectangle, border_width, border_radius)
        surface.blit(rendered_text, rendered_text_rect)

    @event
    def on_mouse_enter(self, event):
        mouse_hover_color = self.attributes.get("mouse_hover_color", (0, 150, 255))
        mouse_hover_font_color = self.attributes.get("mouse_hover_font_color", (0, 150, 255))
        border_color = self.attributes.get("border_color", (255, 255, 255))
        font_color = self.attributes.get("font_color", (255, 255, 255))
        self.attributes["border_color"] = mouse_hover_color
        self.attributes["mouse_hover_color"] = border_color
        self.attributes["font_color"] = mouse_hover_font_color
        self.attributes["mouse_hover_font_color"] = font_color

    @event
    def on_mouse_leave(self, event):
        mouse_hover_color = self.attributes["mouse_hover_color"]
        mouse_hover_font_color = self.attributes["mouse_hover_font_color"]
        border_color = self.attributes["border_color"]
        font_color = self.attributes["font_color"]
        self.attributes["border_color"] = mouse_hover_color
        self.attributes["mouse_hover_color"] = border_color
        self.attributes["font_color"] = mouse_hover_font_color
        self.attributes["mouse_hover_font_color"] = font_color