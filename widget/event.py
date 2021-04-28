import types


class Event:
    """
    Cette classe est un descripteur définissant un évènement.

    Chaque widget comporte un dictionnaire 'events' des évènements
    qu'il redéfinit. Ces évènements sont spécifiques à l'instance.
    Lorsqu'un widget ne redéfinit pas un évènement, l'évènement par
    défaut, commun à toutes les instances du widget, doit être
    appelé.
    Ce descripteur permet donc de réaliser de manière transparente
    tout cela.

    Prenons en exemple le widget 'Button' (définit dans 'button.py').
    >>> button = Button(...)
    >>> button.on_click(...) # appel de l'évènement par défaut
    >>> button.on_click = some_callback # redéfinition de l'évènement
    pour cette instance de 'Button' ; le nouveau callback est stocké
    sous forme de 'method' ('MethodType') dans le dictionnaire
    'events' qu'il contient
    >>> button.on_click(...) # appel de l'évènement redéfinit
    """

    def __init__(self, func):
        self.callback = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.events.get(self.name) or types.MethodType(self.callback, instance)

    def __set__(self, instance, new_callback):
        instance.events[self.name] = types.MethodType(new_callback, instance)

    def __set_name__(self, cls, name):
        self.name = name


# fonction utilitaire directement associée à 'Event'
def event(func):
    return Event(func)