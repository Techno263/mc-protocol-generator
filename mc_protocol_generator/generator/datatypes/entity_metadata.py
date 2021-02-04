from .base import Base

class EntityMetadata(Base):
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'EntityMetadata'
        name = data['name'] if 'name' in data else None
        return EntityMetadata(name)
