from .base import DatatypeBase

class Buffer(DatatypeBase):
    def __init__(self, count_type, count=None, rest=None):
        self.count_type = count_type
        self.count = count
        self.rest = rest

class Bitfield(DatatypeBase):
    def __init__(self, fields):
        self.fields = fields

class BitfieldItem(DatatypeBase):
    def __init__(self, name, size, signed):
        self.name = name
        self.size = size
        self.signed = signed

class Mapper(DatatypeBase):
    def __init__(self, type, mappings):
        self.type = type
        self.mappings = mappings

class PString(DatatypeBase):
    def __init__(self, count_type, count=None):
        self.count_type = count_type
        self.count = count
