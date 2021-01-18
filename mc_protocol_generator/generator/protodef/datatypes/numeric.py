from .base import DatatypeBase

class Int8(DatatypeBase):
    def __init__(self, size=1):
        self.size = size

class UInt8(DatatypeBase):
    def __init__(self, size=1):
        self.size = size

class Int16(DatatypeBase):
    def __init__(self, size=2):
        self.size = size

class UInt16(DatatypeBase):
    def __init__(self, size=2):
        self.size = size

class Int32(DatatypeBase):
    def __init__(self, size=4):
        self.size = size

class Int64(DatatypeBase):
    def __init__(self, size=8):
        self.size = size

class Float32(DatatypeBase):
    def __init__(self, size=4):
        self.size = size

class Float64(DatatypeBase):
    def __init__(self, size=8):
        self.size = size

class Varint(DatatypeBase):
    pass
