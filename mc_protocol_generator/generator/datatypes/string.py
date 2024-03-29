from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string
from mc_protocol_generator.generator.datatypes.constants import STRING_DATATYPE_NAME
from ast import Call, Attribute, Name, Load, Expr, Assign, Store

class String(Base):
    @property
    def type(self):
        return str

    def __init__(self, name, max_length=32767):
        super().__init__(name)
        self.max_length = max_length

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        if object_override == None:
            obj = Name(
                id='self',
                ctx=Load()
            )
        else:
            obj = object_override
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
                attr='string_size',
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
                        attr='write_string',
                        ctx=Load()
                    ),
                    args=[node],
                    keywords=[]
                )
            )
        ]

    def get_read_nodes(self, reader_name, do_assign=True):
        value_op = Call(
            func=Attribute(
                value=Name(id=reader_name, ctx=Load()),
                attr='read_string',
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
        assert data['type'] == STRING_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        if 'options' in data:
            if 'max_length' in data['options']:
                max_length = data['options']['max_length']
            else:
                max_length = 32767
        else:
            max_length = 32767
        return String(name, max_length)
