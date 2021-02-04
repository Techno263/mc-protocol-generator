from .base import Base

class VarLong(Base):
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'VarLong'
        name = data['name'] if 'name' in data else None
        return VarLong(name)
