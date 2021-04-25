import types


class Event:
    def __init__(self, func=None):
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


def event(func):
    return Event(func)