from .base import Base
from ast import IfExp, Compare, Attribute, Name, Load, Eq, Constant

def validate(option):
    from .datatype import all_types, switch_types, option_types
    if type(option.optional_type) not in (all_types - switch_types - option_types):
        raise Exception(f'Invalid optional type, {type(option.optional_type)}')

class Option(Base):
    def __init__(self, name, optional_type):
        super().__init__(name)
        self.optional_type = optional_type
        validate(self)

    @property
    def field_name(self):
        return self.optional_type.field_name

    def get_field_name_set(self):
        return self.optional_type.get_field_name_set()

    def get_class_name_sets(self):
        return self.optional_type.get_class_name_sets()

    @property
    def type(self):
        return self.optional_type.type

    def get_init_args(self):
        return self.optional_type.get_init_args()

    def get_init_body_nodes(self):
        return self.optional_type.get_init_body_nodes()

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

    def get_module_body_nodes(self):
        nodes = self.optional_type.get_module_body_nodes()
        if nodes != None:
            return nodes

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Option'
        name = data['name'] if 'name' in data else None
        optional_type = parse_field(data['options']['optional'])
        optional_type.name = name
        return Option(name, optional_type)
