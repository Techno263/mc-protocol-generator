from .base import Base

class Position(Base):
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Position'
        name = data['name'] if 'name' in data else None
        return Position(name)
