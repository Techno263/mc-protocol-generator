from abc import ABC, abstractmethod
from enum import Enum

class StaticPropertyDescriptor(object):
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

class BoundTo(Enum):
    CLIENT = 0
    SERVER = 1

    def __str__(self):
        return str(self.name).lower()

class A(ABC):

    def __init__(self):
        pass

    @staticproperty
    def baz():
        return 'apple'

    @staticmethod
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class B(A):
    def __init__(self):
        pass

    def foo(self):
        return 'hello world'

    def bar(self):
        return 'hello'

if __name__ == '__main__':
    a = BoundTo.CLIENT
    breakpoint()
    print(dir(a))
    print(a.value)
    print(a.name)
