from .frame import Frame


class StackedLayout(Frame):
    """
    Cette classe représente un gestionnaire de frames.
    Je me suis basé sur ma relative expérience de pyqt5 pour créer cette classe.

    Les règles du gestionnaire sont simples :
    - il existe une frame actuelle qui est la frame sélectionnée, et qui sera affichée
    - chaque frame porte un nom, et l'on sélectionne une frame par son nom
    - les évènements arrivant sur le gestionnaire sont redirigés à la frame sélectionnée
    """

    def __init__(self, **frames):
        self.frames = frames
        if self.frames:
            self.set_frame(next(self.frames.keys()))
        else:
            self.current = None

    def add_frames(self, **frames):
        self.frames.update(frames)

    def set_frame(self, frame_name):
        if self.current is not None:
            self.current.exit()
        self.current = self.frames[frame_name]
        self.current.enter()

    def draw(self, surface, position):
        if self.current is not None:
            self.current.draw(surface, position)

    def on_event(self, event):
        if self.current is not None:
            return self.current.on_event(event)
        return True

    def on_key_event(self, keyboard):
        if self.current is not None:
            self.current.on_key_event(keyboard)

    def __getitem__(self, key):
        return self.frames[key]