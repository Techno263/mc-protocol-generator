from struct import pack
from uuid import UUID

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
        writer.write_boolean = write_boolean
        writer.write_byte = write_byte
        writer.write_ubyte = write_ubyte
        writer.write_short = write_short
        writer.write_ushort = write_ushort
        writer.write_int = write_int
        writer.write_long = write_long
        writer.write_float = write_float
        writer.write_double = writer_double
        writer.write_string = write_string
        writer.write_chat = write_chat
        writer.write_identifier = write_identifier
        writer.write_varint = write_varint
        writer.write_varlong = write_varlong
        writer.write_entity_metadata = write_entity_metadata
        writer.write_slot = write_slot
        writer.write_nbt = write_nbt
        writer.write_position = write_position
        writer.write_angle = write_angle
        writer.write_uuid = write_uuid
        writer.write_byte_array = write_byte_array
        return writer
