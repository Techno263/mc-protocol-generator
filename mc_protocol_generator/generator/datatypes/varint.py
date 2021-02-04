from .base import Base

class VarInt(Base):
    def generate_read_code(self, reader_name, assignment=True):
        if assignment:
            return f'{self.name} = {reader_name}.read_varint()'
        else:
            return f'{reader_name}.read_varint()'
    
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'VarInt'
        name = data['name'] if 'name' in data else None
        return VarInt(name)
