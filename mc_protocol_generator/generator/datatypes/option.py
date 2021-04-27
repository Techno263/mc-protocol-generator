from .base import Base
from ast import (
    IfExp, Compare, Attribute, Name, Load, Eq, Constant,
    Assign, Store, NotEq, Expr, Call, If, BinOp, Add
)
from mc_protocol_generator.generator.datatypes.constants import OPTION_DATATYPE_NAME

def validate(option):
    from .datatype import all_types, switch_types, option_types
    if type(option.optional_type) not in (all_types - switch_types - option_types):
        raise Exception(f'Invalid optional type, {type(option.optional_type)}')

class Option(Base):
    def __init__(self, name, optional_type):
        self.optional_type = optional_type
        self.optional_type.name = name
        validate(self)

    @property
    def name(self):
        return self.optional_type.name

    @name.setter
    def name(self, value):
        self.optional_type.name = value

    @property
    def field_name(self):
        return self.optional_type.field_name
    
    @property
    def check_var_name(self):
        return f'{self.field_name}_check'

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
            obj = object_override
        if node_override == None:
            node = Attribute(
                value=obj,
                attr=self.field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return BinOp(
            left=Attribute(
                value=Name(id=sizer_name, ctx=Load()),
                attr='bool_size',
                ctx=Load()
            ),
            op=Add(),
            right=IfExp(
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
            Assign(
                targets=[Name(id=self.check_var_name, ctx=Store())],
                value=Compare(
                    left=node,
                    ops=[NotEq()],
                    comparators=[Constant(value=None)]
                )
            ),
            Expr(
                value=Call(
                    func=Attribute(
                        value=Name(id=writer_name, ctx=Load()),
                        attr='write_bool',
                        ctx=Load()
                    ),
                    args=[Name(id=self.check_var_name, ctx=Load())],
                    keywords=[]
                )
            ),
            If(
                test=Name(id=self.check_var_name, ctx=Load()),
                body=self.optional_type.get_write_nodes(
                    writer_name,
                    node
                ),
                orelse=[]
            )
        ]

    def get_read_node(self, reader_name):
        pass

    def get_module_body_nodes(self):
        nodes = self.optional_type.get_module_body_nodes()
        if nodes != None:
            return nodes

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == OPTION_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        optional_type = parse_field(data['options']['optional'])
        optional_type.name = name
        return Option(name, optional_type)
