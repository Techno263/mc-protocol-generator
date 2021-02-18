from .base import Base
from ast import IfExp, Compare, Attribute, Name, Load, Eq, Constant

class Option(Base):
    def __init__(self, name, optional_type):
        super().__init__(name)
        self.optional_type = optional_type

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
        return IfExp(
            test=Compare(
                left=node,
                ops=[Eq()],
                comparators=[
                    Constant(
                        value=None
                    )
                ]
            ),
            body=Constant(
                value=0
            ),
            orelse=self.optional_type.get_len_node(
                sizer_name,
                object_override=object_override,
                node_override=node_override
            )
        )

    def get_repr_body_nodes(self, prefix):
        pass

    def get_write_node(self, writer_name):
        pass

    def get_read_node(self, reader_name):
        pass

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Option'
        name = data['name'] if 'name' in data else None
        optional_type = parse_field(data['options']['optional'])
        optional_type.name = name
        return Option(name, optional_type)
