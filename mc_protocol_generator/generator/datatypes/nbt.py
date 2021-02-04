from .base import Base

class NBT(Base):
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'NBT'
        name = data['name'] if 'name' in data else None
        return NBT(name)
