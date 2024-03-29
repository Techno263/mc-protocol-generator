from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string
from mc_protocol_generator.generator.datatypes.constants import VARINT_DATATYPE_NAME
from ast import Call, Attribute, Name, Load, Expr, Assign, Store

class VarInt(Base):
    @property
    def type(self):
        return int

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        if object_override == None:
            obj = Name(
                id='self',
                ctx=Load()
            )
        else:
            obj = value_override
        if node_override == None:
            node = Attribute(
                value=obj,
                attr=self.field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return Call(
            func=Attribute(
                value=Name(
                    id=sizer_name,
                    ctx=Load()
                ),
                attr='varint_size',
                ctx=Load()
            ),
            args=[node],
            keywords=[]
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
                        attr='write_varint',
                        ctx=Load(),
                    ),
                    args=[node],
                    keywords=[],
                )
            )
        ]

    def get_read_nodes(self, reader_name, do_assign=True):
        value_op = Call(
            func=Attribute(
                value=Name(id=reader_name, ctx=Load()),
                attr='read_varint',
                ctx=Load()
            ),
            args=[],
            keywords=[]
        )
        if do_assign:
            return [
                Assign(
                    targets=[Name(id=self.field_name, ctx=Store())],
                    value=value_op
                )
            ]
        return value_op

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == VARINT_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        return VarInt(name)
