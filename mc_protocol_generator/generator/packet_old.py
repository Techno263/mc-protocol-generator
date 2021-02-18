from enum import Enum, EnumMeta
from .datatypes import (Angle, Array, Bool, Byte, Chat, Compound, Double,
                        EntityMetadata, Float, Identifier, Int, Long, NBT,
                        Option, Position, Short, Slot, String, Switch, UByte,
                        UShort, UUID, VarInt, VarLong)
from .code_generator_context import CodeGeneratorContext
import re
from mc_protocol_generator.generator.util import replace_string, format_class_name, format_field_name
from black import Mode, format_str

writer_name = 'writer'
reader_name = 'reader'
sizer_name = 'dl'
packet_template = '''{{imports}}

{{util_block}}

class {{class_name}}:
    def __init__(self{{init_args}}):
        {{init_body}}

    @staticproperty
    def name():
        {{name_body}}

    @staticproperty
    def packet_id():
        {{packet_id_body}}

    @staticproperty
    def state():
        {{state_body}}

    @staticproperty
    def bound_to():
        {{bound_to_body}}

    def __len__(self):
        {{len_body}}
    
    def __repr__(self):
        {{repr_body}}

    def __bytes__(self):
        buffer = io.BytesIO()
        self.write_packet(buffer)
        buffer.seek(0, 0)
        return buffer.read()

    def write_packet(self, {{writer_name}}):
        {{write_packet_body}}

    @staticmethod
    def read_packet({{reader_name}}):
        {{read_packet_body}}
'''

class StrGetterEnumMeta(EnumMeta):
    def __getitem__(cls, element):
        element = element.upper()
        return super().__getitem__(element)

class BoundTo(Enum, metaclass=StrGetterEnumMeta):
    CLIENT = 0
    SERVER = 1

    def __str__(self):
        return self.name.lower()

class State(Enum, metaclass=StrGetterEnumMeta):
    HANDSHAKING = 0
    STATUS = 1
    LOGIN = 2
    PLAY = 3

    def __str__(self):
        return self.name.lower()

def parse_field(field_data):
    data_type = field_data['type']
    if data_type == 'Bool':
        return Bool.from_protocol_data(field_data)
    elif data_type == 'Byte':
        return Byte.from_protocol_data(field_data)
    elif data_type == 'UByte':
        return UByte.from_protocol_data(field_data)
    elif data_type == 'Short':
        return Short.from_protocol_data(field_data)
    elif data_type == 'UShort':
        return UShort.from_protocol_data(field_data)
    elif data_type == 'Int':
        return Int.from_protocol_data(field_data)
    elif data_type == 'Long':
        return Long.from_protocol_data(field_data)
    elif data_type == 'Float':
        return Float.from_protocol_data(field_data)
    elif data_type == 'Double':
        return Double.from_protocol_data(field_data)
    elif data_type == 'String':
        return String.from_protocol_data(field_data)
    elif data_type == 'Chat':
        return Chat.from_protocol_data(field_data)
    elif data_type == 'Identifier':
        return Identifier.from_protocol_data(field_data)
    elif data_type == 'VarInt':
        return VarInt.from_protocol_data(field_data)
    elif data_type == 'VarLong':
        return VarLong.from_protocol_data(field_data)
    elif data_type == 'EntityMetadata':
        return EntityMetadata.from_protocol_data(field_data)
    elif data_type == 'Slot':
        return Slot.from_protocol_data(field_data)
    elif data_type == 'NBT':
        return NBT.from_protocol_data(field_data)
    elif data_type == 'Position':
        return Position.from_protocol_data(field_data)
    elif data_type == 'Angle':
        return Angle.from_protocol_data(field_data)
    elif data_type == 'UUID':
        return UUID.from_protocol_data(field_data)
    elif data_type == 'Array':
        return Array.from_protocol_data(field_data)
    elif data_type == 'Switch':
        return Switch.from_protocol_data(field_data)
    elif data_type == 'Option':
        return Option.from_protocol_data(field_data)
    elif data_type == "Compound":
        return Compound.from_protocol_data(field_data)
    elif data_type == None:
        return None
    else:
        raise Exception("Unable to parse type:", data_type)


class Packet:
    def __init__(self, name, id, state, bound_to, fields):
        self.name = name
        self.id = id
        self.state = state
        self.bound_to = bound_to
        self.fields = fields

    def get_code_str(self):
        file_text = packet_template
        class_name = format_class_name(self.name)
        file_text = replace_string(file_text,
            {
                '{{class_name}}': class_name,
                '{{name_body}}': "return '%s'" % (self.name),
                '{{packet_id_body}}': 'return %s' % (self.id),
                '{{state_body}}': "return '%s'" % (str(self.state)),
                '{{bound_to_body}}': "return '%s'" % (str(self.bound_to)),
                '{{len_body}}': 'return %s.varint_size(self.packet_id()){{len_body}}' % (sizer_name),
                '{{repr_body}}': "return f'%s({{repr_body}}'" % (class_name),
                '{{write_packet_body}}': '%s.write_varint(self.packet_id());{{write_packet_body}}' % (writer_name),
                '{{writer_name}}': writer_name,
                '{{reader_name}}': reader_name
            })
        code_gen_ctxt = CodeGeneratorContext(reader_name, writer_name, sizer_name, 0)
        for field_index, field in enumerate(self.fields):
            code_gen_ctxt.field_index = field_index
            repr_body_str = '{{repr_body}}'
            if field_index != 0:
                repr_body_str = ', ' + repr_body_str
            file_text = replace_string(file_text,
                {
                    '{{init_args}}': ', {{init_args}}',
                    '{{init_body}}': 'self.{{init_body}}',
                    '{{len_body}}': ' + {{len_body}}',
                    '{{repr_body}}': repr_body_str
                })
            file_text = field.update_class_str(file_text, code_gen_ctxt)
        field_names = ', '.join(format_field_name(f.name) for f in self.fields)
        file_text = replace_string(file_text,
            {
                '{{imports}}': '',
                '{{util_block}}': '',
                '{{init_args}}': '',
                '{{init_body}}': '',
                '{{len_body}}': '',
                '{{repr_body}}': ')',
                '{{write_packet_body}}': '',
                '{{read_packet_body}}': f'return {class_name}({field_names})'
            })
        file_text = file_text.strip()
        black_mode = Mode(
            target_versions=set(),
            line_length=88,
            is_pyi=False,
            string_normalization=False,
            experimental_string_processing=False
        )
        return format_str(file_text, mode=black_mode)

    @staticmethod
    def parse_packet_data(packet_data):
        name = packet_data['name']
        id = packet_data['id']
        state = State[packet_data['state']]
        bound_to = BoundTo[packet_data['bound_to']]
        fields = [parse_field(field) for field in packet_data['fields']]
        return Packet(name, id, state, bound_to, fields)
