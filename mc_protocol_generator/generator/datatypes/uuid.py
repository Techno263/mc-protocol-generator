from .base import Base

class UUID(Base):
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'UUID'
        name = data['name'] if 'name' in data else None
        return UUID(name)
