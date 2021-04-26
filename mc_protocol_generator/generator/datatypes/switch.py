from ast import (BinOp, Call, Add, IfExp, Compare, Attribute, Name, Load, Eq,
                 Constant, arg, Assign, Store, FormattedValue, If, Pass)
from collections.abc import Iterator
from collections import namedtuple
from .base import Base
from mc_protocol_generator.generator.util import format_field_name

Case = namedtuple('Case', ['value', 'fields'])

class StatefulIterator(Iterator):
    def __init__(self, iterable, stateful_enumerator):
        self.index = 0
        self.iterator = iter(iterable)
        self.stateful_enumerator = stateful_enumerator

    def __iter__(self):
        return self

    def __next__(self):
        next_value = next(self.iterator)
        t_index = self.stateful_enumerator.index
        self.stateful_enumerator.index += 1
        return t_index, next_value

class StatefulEnumerator:
    def __init__(self, start=0):
        self.start = start
        self.index = start

    def reset(self, start=None):
        if start != None:
            self.start = start
        self.index = self.start

    def __call__(self, iterable):
        return StatefulIterator(iterable, self)


class SetFilter:
    def __init__(self, key, value, index=0):
        self.key = key
        self.value = value
        self.index = index

    def __repr__(self):
        return f'SetFilter(key={repr(self.key)}, arg={repr(self.arg)}, index={repr(self.index)})'

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if hasattr(other, 'key'):
            return other.key == self.key
        return False

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

def get_cases_write_node(writer_name, cases, switch_value_node, ):
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
    def __init__(self, field, cases):
        super().__init__(None)
        self.field = field
        self.cases = cases
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

    def get_init_args(self):
        stateful_enumerate = StatefulEnumerator()
        opt_args = [
            set_filter.value
            for set_filter in sorted({
                SetFilter(
                    field.field_name,
                    (arg(arg=field.field_name), Constant(value=None)),
                    index
                )
                for case in self.cases
                for index, field in stateful_enumerate(case.fields)
            },
            key=lambda x: x.index)
        ]
        return [], opt_args

    def get_init_body_nodes(self):
        stateful_enumerate = StatefulEnumerator()
        return [
            Assign(
                targets=[
                    Attribute(
                        value=Name(
                            id='self',
                            ctx=Load()
                        ),
                        attr=set_filter.value.field_name,
                        ctx=Store()
                    )
                ],
                value=Name(
                    id=set_filter.value.field_name,
                    ctx=Load()
                )
            )
            for set_filter in sorted({
                SetFilter(
                    field.field_name,
                    field,
                    index
                )
                for case in self.cases
                for index, field in stateful_enumerate(case.fields)
            },
            key=lambda x: x.index)
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
        '''
        return BinOp(
            left=self.switch_type.get_len_node(
                sizer_name,
                object_override=object_override
            ),
            op=Add(),
            right=case_node
        )
        '''

    def get_repr_body_nodes(self):
        stateful_enumerate = StatefulEnumerator()
        opt_args = [
            set_filter.value
            for set_filter in sorted({
                SetFilter(
                    field.field_name,
                    [
                        Constant(value=f'{field.field_name}='),
                        FormattedValue(
                            value=Call(
                                func=Name(id='repr', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr=field.field_name,
                                        ctx=Load()
                                    )
                                ],
                                keywords=[]
                            ),
                            conversion=-1
                        )
                    ],
                    index
                )
                for case in self.cases
                for index, field in stateful_enumerate(case.fields)
            },
            key=lambda x: x.index)
        ]
        nodes = [None, [Constant(value=', ')]] * (len(opt_args) - 1) + [None]
        nodes[0::2] = opt_args
        nodes = [node for node_list in nodes for node in node_list]
        return [nodes]

    def get_write_nodes(self, writer_name, node_override=None):
        if node_override == None:
            node = Attribute(
                value=Name(id='self', ctx=Load()),
                attr=self.switch_field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return get_cases_write_node(
            writer_name,
            self.cases,
            node
        )
        

    def get_read_node(self, reader_name):
        pass

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
        assert data['type'] == 'Switch'
        field = data['options']['switch']['field']
        cases = [
            Case(
                case['value'],
                [parse_field(field) for field in case['fields']]
            )
            for case in data['options']['cases']
        ]
        return Switch(field, cases)
