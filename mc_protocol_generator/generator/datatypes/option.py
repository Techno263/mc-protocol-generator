from .base import Base

class Option(Base):
    def __init__(self, name, optional_type):
        super().__init__(name)
        self.optional_type = optional_type

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Option'
        name = data['name'] if 'name' in data else None
        optional_type = parse_field(data['options']['optional'])
        return Option(name, optional_type)
