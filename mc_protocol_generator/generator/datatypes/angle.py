from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string
from ast import Attribute, Name, Load, Expr, Call

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
                        attr='write_angle',
                        ctx=Load()
                    ),
                    args=[node],
                    keywords=[]
                )
            )
        ]

    def get_read_node(self, reader_name):
        pass

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Angle'
        name = data['name'] if 'name' in data else None
        return Angle(name)
