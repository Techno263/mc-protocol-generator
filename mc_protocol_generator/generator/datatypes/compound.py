from .base import Base
from mc_protocol_generator.generator.util import format_class_name
from mc_protocol_generator.generator.datatypes.constants import COMPOUND_DATATYPE_NAME
from mc_protocol_generator.generator.constants import (
    DATATYPE_SIZER_VAR, DATATYPE_WRITER_VAR, DATATYPE_READER_VAR
)
from ..code_generator_context import CodeGeneratorContext
from ast import (
    Call, Name, Load, Attribute, ClassDef, FunctionDef, Assign,
    Store, arguments, arg, BinOp, Add, Return, JoinedStr,
    Constant, Expr
)

def validate(compound):
    field_sets = [field.get_field_name_set() for field in compound.fields]
    has_field_intersection = any(
        field_set & other_set
        for index, field_set in enumerate(field_sets, start=1)
        for other_set in field_sets[index:]
    )
    if has_field_intersection:
        raise Exception(f'Compound field names must be distinct')

class Compound(Base):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields
        validate(self)

    @property
    def class_name(self):
        return format_class_name(self.name)

    def get_class_name_sets(self):
        return [
            {self.class_name}
        ] + [
            class_name_set
            for field in self.fields
            for class_name_set in field.get_class_name_sets()
            if len(class_name_set) > 0
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
                attr=self.field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return Call(
            func=Name(
                id='len',
                ctx=Load()
            ),
            args=[node],
            keywords=[]
        )

    def get_write_nodes(self, writer_name, node_override=None):
        if node_override == None:
            node = value=Attribute(
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
                        node,
                        attr='write_data',
                        ctx=Load()
                    ),
                    args=[Name(id=writer_name, ctx=Load())],
                    keywords=[]
                )
            )
        ]

    def get_read_nodes(self, reader_name, do_assign=True):
        value_op = Call(
            func=Attribute(
                value=Name(id=self.class_name, ctx=Load()),
                attr='read_data',
                ctx=Load()
            ),
            args=[Name(id=reader_name, ctx=Load())],
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

    def _get_class_init_arg_nodes(self):
        return arguments(
            posonlyargs=[],
            args=[
                arg(arg='self', annotation=None, type_comment=None)
            ] + [
                arg
                for field in self.fields
                for arg in field.get_init_args()
            ],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        )

    def _get_class_init_body_nodes(self):
        return [
            node
            for field in self.fields
            for node in field.get_init_body_nodes()
        ]

    def _get_class_len_body_nodes(self):
        if len(self.fields) == 0:
            return [Return(value=Constant(value=0, kind=None))]
        elif len(self.fields) == 1:
            return [Return(value=self.fields[0].get_len_node(DATATYPE_SIZER_VAR))]
        bin_op = BinOp(
            left=self.fields[0].get_len_node(DATATYPE_SIZER_VAR),
            op=Add(),
            right=self.fields[1].get_len_node(DATATYPE_SIZER_VAR)
        )
        for field in self.fields[2:]:
            bin_op = BinOp(
                left=bin_op,
                op=Add(),
                right=field.get_len_node(DATATYPE_SIZER_VAR)
            )
        return [Return(value=bin_op)]

    def _get_class_repr_body_nodes(self):
        field_nodes = [
            field_repr_node_list
            for field in self.fields
            for field_repr_node_list in field.get_repr_body_nodes()
        ]
        repr_nodes = (
            [None, [Constant(value=', ')]]
            * (len(field_nodes) - 1)
            + [None]
        )
        repr_nodes[::2] = field_nodes
        return [
            Return(
                value=JoinedStr(
                    values=[
                        Constant(value=self.class_name + '(')
                    ] + [
                        node
                        for node_list in repr_nodes
                        for node in node_list
                    ] + [
                        Constant(value=')')
                    ]
                )
            )
        ]

    def _get_class_write_data_body_nodes(self):
        return [
            node
            for field in self.fields
            for node in field.get_write_nodes(DATATYPE_WRITER_VAR)
        ]

    def _get_class_read_data_body_nodes(self):
        return [
            node
            for field in self.fields
            for node in field.get_read_nodes(DATATYPE_READER_VAR)
        ] + [
            Return(
                value=Call(
                    func=Name(id=self.class_name, ctx=Load()),
                    args=[
                        arg
                        for field in self.fields
                        for arg in field.get_init_args()
                    ],
                    keywords=[]
                )
            )
        ]

    def get_module_body_nodes(self):
        return [
            node
            for field in self.fields
            if (nodes := field.get_module_body_nodes()) != None
            for node in nodes
        ] + [
            ClassDef(
                name=format_class_name(self.name),
                bases=[],
                keywords=[],
                body=[
                    FunctionDef(
                        name='__init__',
                        args=self._get_class_init_arg_nodes(),
                        body=self._get_class_init_body_nodes(),
                        decorator_list=[],
                        returns=None,
                        type_comment=None
                    ),
                    FunctionDef(
                        name='__len__',
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='self', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[]
                        ),
                        body=self._get_class_len_body_nodes(),
                        decorator_list=[],
                        returns=None,
                        type_comment=None
                    ),
                    FunctionDef(
                        name='__repr__',
                        args=arguments(
                            posonlyargs=[],
                                args=[arg(arg='self', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[]
                        ),
                        body=self._get_class_repr_body_nodes(),
                        decorator_list=[],
                        returns=None,
                        type_comment=None
                    ),
                    FunctionDef(
                        name='write_data',
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='self'), arg(arg='writer')],
                            kwonlyargs=[],
                            kw_defaults=[],
                            defaults=[],
                        ),
                        body=self._get_class_write_data_body_nodes(),
                        decorator_list=[]
                    ),
                    FunctionDef(
                        name='read_data',
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='reader')],
                            kwonlyargs=[],
                            kw_defaults=[],
                            defaults=[],
                        ),
                        body=self._get_class_read_data_body_nodes(),
                        decorator_list=[Name(id='staticmethod', ctx=Load())]
                    )
                ],
                decorator_list=[]
            )
        ]

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == COMPOUND_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        fields = [parse_field(field) for field in data['options']['fields']]
        return Compound(name, fields)
