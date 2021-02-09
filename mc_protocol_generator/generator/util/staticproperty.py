class StaticPropertyDescriptor:
    def __init__(self, fget):
        if not isinstance(fget, staticmethod):
            fget = staticmethod(fget)
        self.fget = fget

    def __get__(self, instance, cls):
        return self.fget.__get__(instance, cls)()

    def __set__(self, instance, value):
        raise AttributeError("can't set attribute")

def staticproperty(fget):
    return StaticPropertyDescriptor(fget)
