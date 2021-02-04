from .base import Base

class Slot(Base):
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Slot'
        name = data['name'] if 'name' in data else None
        return Slot(name)
