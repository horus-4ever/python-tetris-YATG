from abc import ABC, abstractmethod


class Frame(ABC):
    """
    Cette classe est une classe abstraite représentant une frame du jeu.

    Les méthodes 'enter' et 'exit' sont appelées respectivement lorsque l'on
    affiche la frame, et lorsque l'on change de frame.

    Les méthodes 'on_event' et 'on_key_event' sont appelées respectivement à
    chaque nouvel évènement pygame, et lorsque l'état du clavier change.

    La méthode 'draw' doit être obligatoirement implémentée et doit se charger
    de l'affichage de la frame.
    """

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
        return NotImplemented