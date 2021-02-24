from .base import Base
from ast import Attribute, Name, Load

class UByte(Base):
    @property
    def type(self):
        return int

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        return Attribute(
            value=Name(
                id=sizer_name,
                ctx=Load()
            ),
            attr='ubyte_size',
            ctx=Load()
        )

    def get_write_node(self, writer_name):
        pass

    def get_read_node(self, reader_name):
        pass
    
    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'UByte'
        name = data['name'] if 'name' in data else None
        return UByte(name)
