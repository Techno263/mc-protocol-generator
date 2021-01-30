from .base import DatatypeBase

class Switch(DatatypeBase):
    def __init__(self, compare_to, fields, compare_to_value=None, default=None):
        self.compare_to = compare_to
        self.fields = fields
        self.compare_to_value = compare_to_value
        self.default = default
    '''
    @staticmethod
    def parse(options):
        compare_to = 
    '''

class Option(DatatypeBase):
    def __init__(self, types):
        self.types = types
