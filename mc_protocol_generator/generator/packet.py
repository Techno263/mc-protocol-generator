from enum import Enum, EnumMeta
from .datatypes import (Angle, Array, Bool, Byte, Chat, Compound, Double,
                        EntityMetadata, Float, Identifier, Int, Long, NBT,
                        Option, Position, Short, Slot, String, Switch, UByte,
                        UShort, UUID, VarInt, VarLong)

class StrGetterEnumMeta(EnumMeta):
    def __getitem__(cls, element):
        element = element.upper()
        return super().__getitem__(element)

class BoundTo(Enum, metaclass=StrGetterEnumMeta):
    CLIENT = 0
    SERVER = 1

class State(Enum, metaclass=StrGetterEnumMeta):
    HANDSHAKING = 0
    STATUS = 1
    LOGIN = 2
    PLAY = 3

def _format_label(label):
    if label != None:
        return label.lower().replace(' ', '_')

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

    @staticmethod
    def parse_packet_data(packet_data):
        name = _format_label(packet_data['name'])
        id = int(packet_data['id'], 16)
        state = State[packet_data['state']]
        bound_to = BoundTo[packet_data['bound_to']]
        fields = [parse_field(field) for field in packet_data['fields']]
        return Packet(name, id, state, bound_to, fields)
