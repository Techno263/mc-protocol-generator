from .base import Base
from ast import Attribute, Name, Load, Expr, Call, Assign, Store
from mc_protocol_generator.generator.datatypes.constants import DOUBLE_DATATYPE_NAME

class Double(Base):
    @property
    def type(self):
        return float

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        return Attribute(
            value=Name(
                id=sizer_name,
                ctx=Load()
            ),
            attr='double_size',
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
                        attr='write_double',
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
                attr='read_double',
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
        assert data['type'] == DOUBLE_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        return Double(name)
