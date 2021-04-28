from .event import event
from .widget import Widget


class Frame(Widget):
    """
    Cette classe représente une frame.
    Elle n'est pas utilisée pour le moment dans le programme, et
    est donc pour le moment inutile.
    """

    @event
    def enter(self):
        pass

    @event
    def exit(self):
        pass

    @event
    def on_event(self, event):
        pass

    @event
    def on_key_event(self, keyboard):
        pass

    @event
    def draw(self, surface, position):
        pass