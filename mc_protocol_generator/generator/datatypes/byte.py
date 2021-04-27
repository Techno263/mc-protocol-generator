from .base import Base
from ast import Attribute, Name, Load, Expr, Call
from mc_protocol_generator.generator.datatypes.constants import BYTE_DATATYPE_NAME

class Byte(Base):
    @property
    def type(self):
        return int

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        return Attribute(
            value=Name(
                id=sizer_name,
                ctx=Load()
            ),
            attr='byte_size',
            ctx=Load()
        )

    def get_write_nodes(self, writer_name, node_override=None):
        if node_override == None:
            node = Attribute(
                value=Name(id='self', ctx=Load()),
                attr=self.field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return [
            Expr(
                value=Call(
                    func=Attribute(
                        value=Name(id=writer_name, ctx=Load()),
                        attr='write_byte',
                        ctx=Load(),
                    ),
                    args=[node],
                    keywords=[],
                )
            )
        ]

    def get_read_node(self, reader_name):
        pass

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == BYTE_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        return Byte(name)
