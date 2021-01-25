from .base import DatatypeBase

class Array(DatatypeBase):
    def __init__(self, type, count_type, count=None):
        self.type = type
        self.count_type = count_type
        self.count = count

class Container(DatatypeBase):
    def __init__(self, fields):
        self.fields = fields

class ContainerItem(DatatypeBase):
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Count(DatatypeBase):
    def __init__(self, type, count_for):
        self.type = type
        self.count_for = count_for