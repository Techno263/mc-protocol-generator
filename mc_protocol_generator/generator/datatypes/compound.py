from .base import Base
from mc_protocol_generator.generator.util import format_class_name
from ..code_generator_context import CodeGeneratorContext
from ast import (Call, Name, Load, Attribute, ClassDef, FunctionDef,
                 Assign, Store, arguments, arg, BinOp, Add, Return)

compound_class_template = '''class {{class_name}}
    def __init__(self{{init_args}}):
        {{init_body}}

    def __len__(self):
        return {{len_body}}

    def __repr__(self):
        return {{repr_body}}

    def write_data(self, {{writer_name}}):
        {{write_data_body}}

    @staticmethod
    def read_data({{reader_name}}):
        {{reader_body}}
'''

class_sizer_name = 'dl'
class_writer_name = 'writer'
class_reader_name = 'reader'

class Compound(Base):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields

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

    def get_repr_body_nodes(self, prefix):
        pass

    def get_write_node(self, writer_name):
        pass

    def get_read_node(self, reader_name):
        pass

    def _get_class_init_arg_nodes(self):
        return [
            arg(arg=field.field_name)
            for field in self.fields
        ]

    def _get_class_init_body_nodes(self):
        return [
            Assign(
                targets=[
                    Attribute(
                        value=Name(
                            id='self',
                            ctx=Load()
                        ),
                        attr=field.field_name,
                        ctx=Store()
                    )
                ],
                value=Name(
                    id=field.field_name,
                    ctx=Load()
                )
            )
            for field in self.fields
        ]

    def _get_class_len_body_nodes(self):
        if len(self.fields) == 0:
            return [Return(value=Constant(value=0, kind=None))]
        elif len(self.fields) == 1:
            return [Return(value=self.fields[0].get_len_node(class_sizer_name))]
        bin_op = BinOp(
            left=self.fields[0].get_len_node(class_sizer_name),
            op=Add(),
            right=self.fields[1].get_len_node(class_sizer_name)
        )
        for field in self.fields[2:]:
            bin_op = BinOp(
                left=bin_op,
                op=Add(),
                right=field.get_len_node(class_sizer_name)
            )
        return [Return(value=bin_op)]

    def _get_class_repr_body_nodes(self):
        from ast import Pass
        return [Pass()]

    def _get_class_write_data_body_nodes(self):
        from ast import Pass
        return [Pass()]

    def _get_class_read_data_body_nodes(self):
        from ast import Pass
        return [Pass()]

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
                        args=arguments(
                            posonlyargs=[],
                            args=[
                                arg(arg='self'),
                                *self._get_class_init_arg_nodes()
                            ],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[]
                        ),
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
        assert data['type'] == 'Compound'
        name = data['name'] if 'name' in data else None
        fields = [parse_field(field) for field in data['options']['fields']]
        return Compound(name, fields)
