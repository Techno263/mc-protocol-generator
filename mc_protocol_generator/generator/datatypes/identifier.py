from .base import Base
from ast import Call, Attribute, Name, Load, Expr
from mc_protocol_generator.generator.datatypes.constants import IDENTIFIER_DATATYPE_NAME

class Identifier(Base):
    @property
    def type(self):
        return str

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
                attr='identifier_size',
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
                ctx=Load(),
            )
        else:
            node = node_override
        return [
            Expr(
                value=Call(
                    func=Attribute(
                        value=Name(id=writer_name, ctx=Load()),
                        attr='write_identifier',
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
        assert data['type'] == IDENTIFIER_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        return Identifier(name)
