from ast import (BinOp, Call, Add, IfExp, Compare, Attribute, Name, Load, Eq,
                 Constant, arg, Assign, Store, FormattedValue, If, Pass)
from collections.abc import Iterator
from collections import namedtuple
from .base import Base
from mc_protocol_generator.generator.util import format_field_name
from mc_protocol_generator.generator.datatypes.constants import SWITCH_DATATYPE_NAME

Case = namedtuple('Case', ['value', 'fields'])

class OrderedSetItem:
    def __init__(self, value, order):
        self.value = value
        self.order = order

    def __repr__(self):
        return f'OrderedSetItem(value={repr(self.value)}, order={repr(self.order)})'

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other

def get_fields_len_node(sizer_name, fields, obj):
    if len(fields) == 0:
        return Constant(value=0, kind=None)
    elif len(fields) == 1:
        return fields[0].get_len_node(sizer_name, obj)
    bin_op = BinOp(
        left=fields[0].get_len_node(sizer_name, obj),
        op=Add(),
        right=fields[1].get_len_node(sizer_name, obj)
    )
    for field in fields[2:]:
        bin_op = BinOp(
            left=bin_op,
            op=Add(),
            right=field.get_len_node(sizer_name, obj)
        )
    return bin_op

def get_field_write_nodes(writer_name, fields):
    if len(fields) == 0:
        return [Pass()]
    return [
        node
        for field in fields
        for node in field.get_write_nodes(writer_name)
    ]

def get_cases_write_nodes(writer_name, cases, switch_value_node):
    if len(cases) == 0:
        return []
    if_op = If(
        test=Compare(
            left=switch_value_node,
            ops=[Eq()],
            comparators=[Constant(value=cases[-1].value)]
        ),
        body=get_field_write_nodes(writer_name, cases[-1].fields),
        orelse=[]
    )
    for case in cases[-2::-1]:
        if_op = If(
            test=Compare(
                left=switch_value_node,
                ops=[Eq()],
                comparators=[Constant(value=case.value)]
            ),
            body=get_field_write_nodes(writer_name, case.fields),
            orelse=[if_op]
        )
    return [if_op]

def get_field_read_nodes(reader_name, case, all_field_names):
    case_fields = {
        field.field_name
        for field in case.fields
    }
    return [
        node
        for field in case.fields
        for node in field.get_read_nodes(reader_name)
    ] + [
        Assign(
            targets=[Name(id=field_name, ctx=Store())],
            value=Constant(value=None)
        )
        for field_name in all_field_names
        if field_name not in case_fields
    ]

def get_cases_read_nodes(reader_name, cases, switch_value_node):
    if len(cases) == 0:
        return []
    all_field_names = [
        item.value
        for item in sorted(
            {
                OrderedSetItem(item, index)
                for index, item in enumerate(
                    field.field_name
                    for case in cases
                    for field in case.fields
                )
            },
            key=lambda set_item: set_item.order
        )
    ]
    if_op = If(
        test=Compare(
            left=switch_value_node,
            ops=[Eq()],
            comparators=[Constant(value=cases[-1].value)]
        ),
        body=get_field_read_nodes(reader_name, cases[-1], all_field_names),
        orelse=[]
    )
    for case in cases[-2::-1]:
        if_op = If(
            test=Compare(
                left=switch_value_node,
                ops=[Eq()],
                comparators=[Constant(value=case.value)]
            ),
            body=get_field_read_nodes(reader_name, case, all_field_names),
            orelse=[if_op]
        )
    return [if_op]

def validate(switch):
    from .datatype import all_types, switch_types
    switch_fields = {
        field_name
        for case in switch.cases
        for field in case.fields
        for field_name in field.get_field_name_set()
    }
    if switch.field in switch_fields:
        raise Exception(f'Case field names cannot intersect with switch name')
    valid_types = all_types - switch_types
    if any(
        (field_type := type(field)) not in valid_types 
        for case in switch.cases
        for field in case.fields
    ):
        raise Exception(f'Invalid field type, {field_type}')

class Switch(Base):
    def __init__(self, field, cases, error_on_invalid_case):
        super().__init__(None)
        self.field = field
        self.cases = cases
        self.error_on_invalid_case = error_on_invalid_case
        validate(self)

    @property
    def switch_field_name(self):
        return format_field_name(self.field)

    def get_field_name_set(self):
        return {
            field_name
            for case in self.cases
            for field in case.fields
            for field_name in field.get_field_name_set()
        }

    def get_ordered_field_names(self):
        return [
            item.value
            for item in sorted(
                {
                    OrderedSetItem(item, index)
                    for index, item in enumerate(
                        field.field_name
                        for case in self.cases
                        for field in case.fields
                    )
                },
                key=lambda set_item: set_item.order
            )
        ]

    def get_init_args(self):
        return [
            arg(arg=field_name)
            for field_name in self.get_ordered_field_names()
        ]

    def get_init_body_nodes(self):
        return [
            Assign(
                targets=[
                    Attribute(
                        value=Name('self', ctx=Load()),
                        attr=field_name,
                        ctx=Store()
                    )
                ],
                value=Name(id=field_name, ctx=Load())
            )
            for field_name in self.get_ordered_field_names()
        ]

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
                attr=self.switch_field_name,
                ctx=Load()
            )
        else:
            node = node_override
        if len(self.cases) == 0:
            return Constant(value=0)
        else:
            case_node = IfExp(
                test=Compare(
                    left=Attribute(
                        value=obj,
                        attr=self.switch_field_name,
                        ctx=Load()
                    ),
                    ops=[Eq()],
                    comparators=[
                        Constant(
                            value=self.cases[-1].value
                        )
                    ]
                ),
                body=get_fields_len_node(
                    sizer_name,
                    self.cases[-1].fields,
                    object_override
                ),
                orelse=Constant(value=0)
            )
            for case in self.cases[-2::-1]:
                case_node = IfExp(
                    test=Compare(
                        left=Attribute(
                            value=obj,
                            attr=self.switch_field_name,
                            ctx=Load()
                        ),
                        ops=[Eq()],
                        comparators=[
                            Constant(
                                value=case.value
                            )
                        ]
                    ),
                    body=get_fields_len_node(
                        sizer_name,
                        case.fields,
                        object_override
                    ),
                    orelse=case_node
                )
        return case_node

    def get_repr_body_nodes(self):
        return [
            [
                Constant(value=f'{field_name}='),
                FormattedValue(
                    value=Call(
                        func=Name(id='repr', ctx=Load()),
                        args=[
                            Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr=field_name,
                                ctx=Load()
                            )
                        ],
                        keywords=[]
                    ),
                    conversion=-1
                )
            ]
            for field_name in self.get_ordered_field_names()
        ]

    def get_write_nodes(self, writer_name, node_override=None):
        if node_override == None:
            node = Attribute(
                value=Name(id='self', ctx=Load()),
                attr=self.switch_field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return get_cases_write_nodes(
            writer_name,
            self.cases,
            node
        )

    def get_read_nodes(self, reader_name, do_assign=True):
        switch_value_node = Name(id=self.switch_field_name, ctx=Load())
        if do_assign:
            return get_cases_read_nodes(
                reader_name,
                self.cases,
                switch_value_node
            )
        raise Exception('Cannot get read nodes for switch type without assign')

    def get_module_body_nodes(self):
        return [
            node
            for case in self.cases
            for field in case.fields
            if (module_body_nodes := field.get_module_body_nodes()) != None
            for node in module_body_nodes
        ]

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == SWITCH_DATATYPE_NAME
        field = data['options']['switch']['field']
        cases = [
            Case(
                case['value'],
                [parse_field(field) for field in case['fields']]
            )
            for case in data['options']['cases']
        ]
        if 'error_on_invalid_case' in data:
            error_on_invalid_case = data['error_on_invalid_case']
        else:
            error_on_invalid_case = False
        return Switch(field, cases, error_on_invalid_case)
