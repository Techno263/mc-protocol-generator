from struct import pack
from uuid import UUID
import types

def write_boolean(writer, value):
    if not isinstance(value, bool):
        value = bool(value)
    writer.write(pack('>B', value))

def write_byte(writer, value):
    writer.write(pack('>b', value))

def write_ubyte(writer, value):
    writer.write(pack('>B', value))

def write_short(writer, value):
    writer.write(pack('>h', value))

def write_ushort(writer, value):
    writer.write(pack('>H', value))

def write_int(writer, value):
    writer.write(pack('>i', value))

def write_long(writer, value):
    writer.write(pack('>q', value))

def write_float(writer, value):
    writer.write(pack('>f', value))

def write_double(writer, value):
    writer.write(pack('>d', value))

def write_string(writer, value):
    encoded = value.encode('utf8')
    write_varint(writer, len(encoded))
    writer.write(encoded)

def write_chat(writer, value):
    write_string(writer, value)

def write_identifier(writer, value):
    write_string(writer, value)

def write_varint(writer, value):
    if value < 0:
        value += 0x100000000
    count = 5
    while True:
        temp = value & 0b01111111
        value >>= 7
        if value != 0:
            temp |= 0b10000000
        write_byte(writer, temp)
        if value == 0:
            break
        count -= 1
        if count <= 0:
            raise Exception('Value too large for varint')

def write_varlong(writer, value):
    if value < 0:
        value += 0x10000000000000000
    count = 10
    while True:
        temp = value & 0b01111111
        value >>= 7
        if value != 0:
            temp |= 0b10000000
        write_byte(writer, temp)
        if value == 0:
            break
        count -= 1
        if count <= 0:
            raise Exception('Value too large for varlong')

def write_entity_metadata(writer, value):
    raise NotImplementedError()

def write_slot(writer, value):
    raise NotImplementedError()

def write_nbt(writer, value):
    raise NotImplementedError()

def write_position(writer, value):
    x, y, z = value
    write_long(writer, ((x & 0x3FFFFFF) << 38) | ((z & 0x3FFFFFF) << 12) | (y & 0xFFF))

def write_angle(writer, value):
    write_byte(writer, int(value * 256))

def write_uuid(writer, value):
    writer.write(value.bytes)

def write_byte_array(writer, value):
    writer.write(value)

class DataWriter:
    def __new__(cls, writer):
        writer.write_boolean = types.MethodType(write_boolean, writer)
        writer.write_byte = types.MethodType(write_byte, writer)
        writer.write_ubyte = types.MethodType(write_ubyte, writer)
        writer.write_short = types.MethodType(write_short, writer)
        writer.write_ushort = types.MethodType(write_ushort, writer)
        writer.write_int = types.MethodType(write_int, writer)
        writer.write_long = types.MethodType(write_long, writer)
        writer.write_float = types.MethodType(write_float, writer)
        writer.write_double = types.MethodType(write_double, writer)
        writer.write_string = types.MethodType(write_string, writer)
        writer.write_chat = types.MethodType(write_chat, writer)
        writer.write_identifier = types.MethodType(write_identifier, writer)
        writer.write_varint = types.MethodType(write_varint, writer)
        writer.write_varlong = types.MethodType(write_varlong, writer)
        writer.write_entity_metadata = types.MethodType(write_entity_metadata, writer)
        writer.write_slot = types.MethodType(write_slot, writer)
        writer.write_nbt = types.MethodType(write_nbt, writer)
        writer.write_position = types.MethodType(write_position, writer)
        writer.write_angle = types.MethodType(write_angle, writer)
        writer.write_uuid = types.MethodType(write_uuid, writer)
        writer.write_byte_array = types.MethodType(write_byte_array, writer)
        return writer
