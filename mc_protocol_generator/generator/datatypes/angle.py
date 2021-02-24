from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string
from ast import Attribute, Name, Load

class Angle(Base):

    def __init__(self, name):
        super().__init__(name)

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        return Attribute(
            value=Name(
                id=sizer_name,
                ctx=Load(),
            ),
            attr='angle_size',
            ctx=Load()
        )

    def get_write_node(self, writer_name):
        pass

    def get_read_node(self, reader_name):
        pass

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Angle'
        name = data['name'] if 'name' in data else None
        return Angle(name)
