from abc import ABC, abstractmethod


class Frame(ABC):
    def enter(self):
        pass

    def exit(self):
        pass

    def on_event(self, event):
        pass

    def on_key_event(self, keyboard):
        pass

    @abstractmethod
    def draw(self, surface, position):
        pass