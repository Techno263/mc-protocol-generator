from ast import (
    Module, ClassDef, Assign, Name, Store, Constant,
    FunctionDef, arguments, arg, Attribute, Load, Return, BinOp, Add,
    JoinedStr, Expr, Call, unparse, fix_missing_locations, Pass
)
from mc_protocol_generator.generator.util import format_class_name
from black import Mode, format_str
from .datatypes import (
    Angle, Array, Bool, Byte, Chat, Compound, Double,
    EntityMetadata, Float, Identifier, Int, Long, NBT,
    Option, Position, Short, Slot, String, Switch, UByte,
    UShort, UUID, VarInt, VarLong
)
from mc_protocol_generator.generator.constants import (
    DATATYPE_SIZER_VAR, DATATYPE_WRITER_VAR, DATATYPE_READER_VAR,
    PACKET_CLASS_NAME_VAR, PACKET_CLASS_ID_VAR,
    PACKET_CLASS_STATE_VAR, PACKET_CLASS_BOUND_TO_VAR
)
from mc_protocol_generator.generator.datatypes.constants import (
    ANGLE_DATATYPE_NAME, ARRAY_DATATYPE_NAME, BOOL_DATATYPE_NAME,
    BYTE_DATATYPE_NAME, CHAT_DATATYPE_NAME, COMPOUND_DATATYPE_NAME,
    DOUBLE_DATATYPE_NAME, ENTITY_METADATA_DATATYPE_NAME,
    FLOAT_DATATYPE_NAME, IDENTIFIER_DATATYPE_NAME, INT_DATATYPE_NAME,
    LONG_DATATYPE_NAME, NBT_DATATYPE_NAME, OPTION_DATATYPE_NAME,
    POSITION_DATATYPE_NAME, SHORT_DATATYPE_NAME, SLOT_DATATYPE_NAME,
    STRING_DATATYPE_NAME, SWITCH_DATATYPE_NAME, UBYTE_DATATYPE_NAME,
    USHORT_DATATYPE_NAME, UUID_DATATYPE_NAME, VARINT_DATATYPE_NAME,
    VARLONG_DATATYPE_NAME
)

def parse_field(field_data):
    data_type = field_data['type']
    if data_type == BOOL_DATATYPE_NAME:
        return Bool.from_protocol_data(field_data)
    elif data_type == BYTE_DATATYPE_NAME:
        return Byte.from_protocol_data(field_data)
    elif data_type == UBYTE_DATATYPE_NAME:
        return UByte.from_protocol_data(field_data)
    elif data_type == SHORT_DATATYPE_NAME:
        return Short.from_protocol_data(field_data)
    elif data_type == USHORT_DATATYPE_NAME:
        return UShort.from_protocol_data(field_data)
    elif data_type == INT_DATATYPE_NAME:
        return Int.from_protocol_data(field_data)
    elif data_type == LONG_DATATYPE_NAME:
        return Long.from_protocol_data(field_data)
    elif data_type == FLOAT_DATATYPE_NAME:
        return Float.from_protocol_data(field_data)
    elif data_type == DOUBLE_DATATYPE_NAME:
        return Double.from_protocol_data(field_data)
    elif data_type == STRING_DATATYPE_NAME:
        return String.from_protocol_data(field_data)
    elif data_type == CHAT_DATATYPE_NAME:
        return Chat.from_protocol_data(field_data)
    elif data_type == IDENTIFIER_DATATYPE_NAME:
        return Identifier.from_protocol_data(field_data)
    elif data_type == VARINT_DATATYPE_NAME:
        return VarInt.from_protocol_data(field_data)
    elif data_type == VARLONG_DATATYPE_NAME:
        return VarLong.from_protocol_data(field_data)
    elif data_type == ENTITY_METADATA_DATATYPE_NAME:
        return EntityMetadata.from_protocol_data(field_data)
    elif data_type == SLOT_DATATYPE_NAME:
        return Slot.from_protocol_data(field_data)
    elif data_type == NBT_DATATYPE_NAME:
        return NBT.from_protocol_data(field_data)
    elif data_type == POSITION_DATATYPE_NAME:
        return Position.from_protocol_data(field_data)
    elif data_type == ANGLE_DATATYPE_NAME:
        return Angle.from_protocol_data(field_data)
    elif data_type == UUID_DATATYPE_NAME:
        return UUID.from_protocol_data(field_data)
    elif data_type == ARRAY_DATATYPE_NAME:
        return Array.from_protocol_data(field_data)
    elif data_type == SWITCH_DATATYPE_NAME:
        return Switch.from_protocol_data(field_data)
    elif data_type == OPTION_DATATYPE_NAME:
        return Option.from_protocol_data(field_data)
    elif data_type == COMPOUND_DATATYPE_NAME:
        return Compound.from_protocol_data(field_data)
    elif data_type == None:
        return None
    else:
        raise Exception("Unable to parse type:", data_type)

def validate(packet):
    field_sets = [field.get_field_name_set() for field in packet.fields]
    has_field_intersection = any(
        field_set & other_set
        for index, field_set in enumerate(field_sets, start=1)
        for other_set in field_sets[index:]
    )
    if has_field_intersection:
        field_intersections = [
            field
            for index, field_set in enumerate(field_sets, start=1)
            for other_set in field_sets[index:]
            if field_set & other_set
            for field in field_set
        ]
        raise Exception(f'Packet field names must be distinct. Field intersection(s): {", ".join(field_intersections)}')
    class_name_sets = [
        class_name_set
        for field in packet.fields 
        for class_name_set in field.get_class_name_sets()
        if len(class_name_set) > 0
    ] + [
        {format_class_name(packet.name)}
    ]
    has_class_intersection = any(
        class_name_set & other_set
        for index, class_name_set in enumerate(class_name_sets, start=1)
        for other_set in class_name_sets[index:]
    )
    if has_class_intersection:
        class_intersections = [
            class_name
            for index, class_name_set in enumerate(class_name_sets, start=1)
            for other_set in class_name_sets[index:]
            if class_name_set & other_set
            for class_name in class_name_set
        ]
        raise Exception(f'Class names must be distinct. Class intersection(s): {", ".join(class_intersections)}')

class Packet:
    def __init__(self, name, id, state, bound_to, fields):
        self.name = name
        self.id = id
        self.state = state
        self.bound_to = bound_to
        self.fields = fields
        validate(self)

    @property
    def class_name(self):
        return format_class_name(self.name)

    def get_init_args(self):
        # get args and optional args from fields
        args, opt_args = zip(*[field.get_init_args() for field in self.fields])
        # concatenate all arg lists into one list
        args = [arg for arg_list in args for arg in arg_list]
        # split optional arg variables and their default values into their own lists
        opt_args = tuple(
            map(
                list,
                zip(*[opt_arg for opt_arg_list in opt_args for opt_arg in opt_arg_list])
            )
        )
        # if there are no optional args, opt_args will be an empty tuple
        # check if there is an opt_args list and defaults list
        # if not make a tuple with two empty lists
        opt_args, defaults = opt_args if len(opt_args) == 2 else ([], [])
        args = [arg(arg='self', annotation=None, type_comment=None)] + args + opt_args
        return arguments(
            posonlyargs=[],
            args=args,
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=defaults
        )

    def get_init_body_nodes(self):
        return [
            node
            for field in self.fields
            for node in field.get_init_body_nodes()
        ]

    def get_len_body_nodes(self, sizer_name):
        bin_op = Call(
            func=Attribute(
                value=Name(id=sizer_name, ctx=Load()),
                attr='varint_size',
                ctx=Load()
            ),
            args=[
                Attribute(
                    value=Name(id=self.class_name, ctx=Load()),
                    attr=PACKET_CLASS_ID_VAR,
                    ctx=Load()
                )
            ],
            keywords=[]
        )
        if len(self.fields) == 0:
            return [Return(bin_op)]
        for field in self.fields:
            bin_op = BinOp(
                left=bin_op,
                op=Add(),
                right=field.get_len_node(sizer_name)
            )
        return [Return(value=bin_op)]

    def get_repr_body_nodes(self):
        field_nodes = [
            nodes
            for nodes_list in zip(
                *[
                    field.get_repr_body_nodes()
                    for field in self.fields
                ]
            )
            for nodes in nodes_list
            if len(nodes) > 0
        ]
        nodes = [None, [Constant(value=', ')]] * (len(field_nodes) - 1) + [None]
        nodes[0::2] = field_nodes
        return [
            Return(
                value=JoinedStr(
                    values=[
                        Constant(value=self.class_name + '(')
                    ] + [
                        node
                        for node_list in nodes
                        for node in node_list
                    ] + [
                        Constant(value=')')
                    ]
                )
            )
        ]

    def get_repr_body_nodes_old(self):
        def get_prefix(index):
            if index == 0:
                return self.class_name + '('
            return ', '
        return [
            Return(
                value=JoinedStr(
                    values=[
                        node
                        for index, field in enumerate(self.fields)
                        for nodes in field.get_repr_body_nodes(get_prefix(index))
                        for node in nodes
                    ]
                )
            )
        ]

    def get_write_packet_body_nodes(self, writer_name):
        return [
            Expr(
                value=Call(
                    func=Attribute(
                        value=Name(id=writer_name, ctx=Load()),
                        attr='write_varint',
                        ctx=Load()
                    ),
                    args=[
                        Attribute(
                            value=Name(id=self.class_name, ctx=Load()),
                            attr=PACKET_CLASS_ID_VAR,
                            ctx=Load()
                        )
                    ],
                    keywords=[]
                )
            )
        ] + [
            node
            for field in self.fields
            for node in field.get_write_nodes(writer_name)
        ]

    def get_read_packet_body_nodes(self, reader_name):
        from ast import Pass
        return [Pass()]
        return [
            field.get_read_node(reader_name)
            for field in self.fields
        ] + [
            Return(
                value=Call(
                    func=Name(id=self.class_name, ctx=Load()),
                    args=[
                        Name(id=field.field_name, ctx=Load())
                        for field in self.fields
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
        ]

    def test_get_packet_ast_node(self):
        module = Module(
            body=[
                *self.get_module_body_nodes(),
                ClassDef(
                    name=self.class_name,
                    bases=[],
                    keywords=[],
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Constant(value=self.name, kind=None),
                            type_comment=None
                        ),
                        Assign(
                            targets=[Name(id='id', ctx=Store())],
                            value=Constant(value=self.id, kind=None),
                            type_comment=None
                        ),
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=Constant(value=self.state, kind=None),
                            type_comment=None
                        ),
                        Assign(
                            targets=[Name(id='bound_to', ctx=Store())],
                            value=Constant(value=self.bound_to, kind=None),
                            type_comment=None
                        ),
                        FunctionDef(
                            name='__init__',
                            args=self.get_init_args(),
                            body=self.get_init_body_nodes(),
                            decorator_list=[],
                            returns=None,
                            type_comment=None
                        )
                    ],
                    decorator_list=[]
                )
            ],
            type_ignores=[]
        )
        fix_missing_locations(module)
        return module

    def get_packet_ast_node(self):
        module = Module(
            body=[
                *self.get_module_body_nodes(),
                ClassDef(
                    name=self.class_name,
                    bases=[],
                    keywords=[],
                    body=[
                        Assign(
                            targets=[Name(id=PACKET_CLASS_NAME_VAR, ctx=Store())],
                            value=Constant(value=self.name, kind=None),
                            type_comment=None
                        ),
                        Assign(
                            targets=[Name(id=PACKET_CLASS_ID_VAR, ctx=Store())],
                            value=Constant(value=self.id, kind=None),
                            type_comment=None
                        ),
                        Assign(
                            targets=[Name(id=PACKET_CLASS_STATE_VAR, ctx=Store())],
                            value=Constant(value=self.state, kind=None),
                            type_comment=None
                        ),
                        Assign(
                            targets=[Name(id=PACKET_CLASS_BOUND_TO_VAR, ctx=Store())],
                            value=Constant(value=self.bound_to, kind=None),
                            type_comment=None
                        ),
                        FunctionDef(
                            name='__init__',
                            args=self.get_init_args(),
                            body=self.get_init_body_nodes(),
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
                            body=self.get_len_body_nodes(DATATYPE_SIZER_VAR),
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
                            body=self.get_repr_body_nodes(),
                            decorator_list=[],
                            returns=None,
                            type_comment=None
                        ),
                        FunctionDef(
                            name='write_packet',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg=DATATYPE_WRITER_VAR, annotation=None, type_comment=None)
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[]
                            ),
                            body=self.get_write_packet_body_nodes(DATATYPE_WRITER_VAR),
                            decorator_list=[],
                            returns=None,
                            type_comment=None
                        ),
                        FunctionDef(
                            name='read_packet',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(
                                    arg=DATATYPE_READER_VAR,
                                    annotation=None,
                                    type_comment=None
                                )],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[]
                            ),
                            body=self.get_read_packet_body_nodes(DATATYPE_READER_VAR),
                            decorator_list=[Name(id='staticmethod', ctx=Load())],
                            returns=None,
                            type_comment=None
                        )
                    ],
                    decorator_list=[]
                )
            ],
            type_ignores=[]
        )
        fix_missing_locations(module)
        return module

    def get_packet_code(self):
        black_mode = Mode(
            target_versions=set(),
            line_length=88,
            is_pyi=False,
            string_normalization=False,
            experimental_string_processing=False
        )
        return format_str(unparse(self.get_packet_ast_node()), mode=black_mode)
    
    @staticmethod
    def parse_packet_data(packet_data):
        name = packet_data['name']
        id = packet_data['id']
        state = packet_data['state']
        bound_to = packet_data['bound_to']
        #state = State[packet_data['state']]
        #bound_to = BoundTo[packet_data['bound_to']]
        fields = [parse_field(field) for field in packet_data['fields']]
        return Packet(name, id, state, bound_to, fields)
