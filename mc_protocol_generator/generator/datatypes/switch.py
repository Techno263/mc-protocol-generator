from .base import Base

class Switch(Base):
    def __init__(self, name, switch_type, cases):
        super().__init__(name)
        self.switch_type = switch_type
        self.cases = cases

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Switch'
        name = data['name'] if 'name' in data else None
        switch_type = parse_field(data['options']['switch'])
        cases = [
            {
                "case": case,
                "fields": [parse_field(field) for field in fields]
            }
            for case, fields in data['options']['case'].items()
        ]
        return Switch(name, switch_type, cases)
