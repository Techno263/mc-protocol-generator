from .base import Base
from ast import (Attribute, Name, Load)

class Bool(Base):
    @property
    def type(self):
        return bool

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        return Attribute(
            value=Name(
                id=sizer_name,
                ctx=Load()
            ),
            attr='bool_size',
            ctx=Load()
        )

    def get_write_node(self, writer_name):
        pass

    def get_read_node(self, reader_name):
        pass

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Bool'
        name = data['name'] if 'name' in data else None
        return Bool(name)
