from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string
from mc_protocol_generator.generator.datatypes.constants import ARRAY_DATATYPE_NAME
from ast import (
    BinOp, Add, Call, Name, Load, GeneratorExp, Attribute,
    comprehension, Store, Expr, For, ListComp, Assign
)

def validate(array):
    from .datatype import integer_types, all_types, switch_types
    if type(array.count_type) not in integer_types:
        raise Exception('Count type must be an integral type')
    if type(array.element_type) not in (all_types - switch_types):
        raise Exception(f'Invalid element type, {array.element_type}')

class Array(Base):
    def __init__(self, name, count_type, element_type):
        super().__init__(name)
        self.count_type = count_type
        self.element_type = element_type
        validate(self)
    
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
        len_obj = Call(
            func=Name(
                id='len',
                ctx=Load()
            ),
            args=[node],
            keywords=[]
        )
        return BinOp(
            left=self.count_type.get_len_node(
                sizer_name,
                node_override=len_obj
            ),
            op=Add(),
            right=Call(
                func=Name(
                    id='sum',
                    ctx=Load()
                ),
                args=[
                    GeneratorExp(
                        elt=self.element_type.get_len_node(
                            sizer_name,
                            node_override=Name(
                                id='item',
                                ctx=Load()
                            )
                        ),
                        generators=[
                            comprehension(
                                target=Name(
                                    id='item',
                                    ctx=Store()
                                ),
                                iter=node,
                                ifs=[],
                                is_async=0
                            )
                        ]
                    )
                ],
                keywords=[]
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
            self.count_type.get_write_nodes(
                writer_name,
                Call(
                    func=Name(id='len', ctx=Load()),
                    args=[node],
                    keywords=[]
                )
            ),
            For(
                target=Name(id='item', ctx=Store()),
                iter=node,
                body=self.element_type.get_write_nodes(
                    writer_name,
                    Name(id='item', ctx=Store())
                ),
                orelse=[]
            )
        ]

    def get_read_nodes(self, reader_name, do_assign=True):
        value_op = ListComp(
            elt=self.element_type.get_read_nodes(reader_name, False),
            generators=[
                comprehension(
                    target=Name(id='_', ctx=Store()),
                    iter=Call(
                        func=Name(id='range', ctx=Load()),
                        args=[
                            self.count_type.get_read_nodes(reader_name, False)
                        ],
                        keywords=[]
                    ),
                    ifs=[],
                    is_async=0
                )
            ]
        )
        if do_assign:
            return [
                Assign(
                    targets=[
                        Name(id=self.field_name, ctx=Store())
                    ],
                    value=value_op
                )
            ]
        return value_op


    def get_module_body_nodes(self):
        return self.element_type.get_module_body_nodes()

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == ARRAY_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        count_type = parse_field(data['options']['count'])
        element_type = parse_field(data['options']['element'])
        element_type.name = f'{name} Item'
        return Array(name, count_type, element_type)
