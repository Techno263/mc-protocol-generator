from struct import unpack
from uuid import UUID
from collections import namedtuple
import types
from .nbt import parse_nbt

Rotation = namedtuple('Rotation', ['x', 'y', 'z'])
VillagerData = namedtuple('VillagerData', ['type', 'profession', 'level'])
Particle = namedtuple('Particle', ['id', 'data'])

def read_boolean(reader):
    return bool(unpack('>B', reader.read(1))[0])

def read_byte(reader):
    return unpack('>b', reader.read(1))[0]

def read_ubyte(reader):
    return unpack('>B', reader.read(1))[0]

def read_short(reader):
    return unpack('>h', reader.read(2))[0]

def read_ushort(reader):
    return unpack('>H', reader.read(2))[0]

def read_int(reader):
    return unpack('>i', reader.read(4))[0]

def read_long(reader):
    return unpack('>q', reader.read(8))[0]

def read_float(reader):
    return unpack('>f', reader.read(4))[0]

def read_double(reader):
    return unpack('>d', reader.read(8))[0]

def read_string(reader):
    length = read_varint(reader)
    string = reader.read(length).decode('utf8')
    return string

def read_chat(reader):
    return read_string(reader)

def read_identifier(reader):
    return read_string(reader)

def read_varint(reader):
    num_read = 0
    result = 0
    while True:
        read = read_byte(reader)
        value = read & 0b01111111
        result |= value << (7 * num_read)
        num_read += 1
        if num_read > 5:
            raise Exception('VarInt is too large')
        if read & 0b10000000 == 0:
            break
    return result

def read_varlong(reader):
    num_read = 0
    result = 0
    while True:
        read = read_byte(reader)
        value = read & 0b01111111
        result |= value << (7 * num_read)
        num_read += 1
        if num_read > 10:
            raise Exception('VarLong is too large')
        if read & 0b10000000 == 0:
            break
    return result

def read_particle(reader):
    particle_id = reader.read_varint()
    if particle_id == 3:
        return Particle(particle_id, {
            'block_state': reader.read_varint()
        })
    elif particle_id == 14:
        return Particle(particle_id, {
            'red': read_float(reader),
            'green': read_float(reader),
            'blue': read_float(reader),
            'scale': read_float(reader)
        })
    elif particle_id == 23:
        return Particle(particle_id, {
            'block_state': reader.read_varint()
        })
    elif particle_id == 32:
        return Particle(particle_id, {
            'item': reader.read_slot()
        })
    else:
        return Particle(particle_id, None)

def read_entity_metadata(reader):
    metadata = {}
    index = reader.read_ubyte()
    while index != 0xff:
        value_type = reader.read_varint()
        if value_type == 0:
            metadata[index] = reader.read_byte()
        elif value_type == 1:
            metadata[index] = reader.read_varint()
        elif value_type == 2:
            metadata[index] = reader.read_float()
        elif value_type == 3:
            metadata[index] = reader.read_string()
        elif value_type == 4:
            metadata[index] = reader.read_chat()
        elif value_type == 5:
            if reader.read_boolean():
                metadata[index] = reader.read_chat()
        elif value_type == 6:
            metadata[index] = reader.read_slot()
        elif value_type == 7:
            metadata[index] = reader.read_boolean()
        elif value_type == 8:
            metadata[index] = Rotation(
                reader.read_float(),
                reader.read_float(),
                reader.read_float()
            )
        elif value_type == 9:
            metadata[index] = reader.read_position()
        elif value_type == 10:
            if reader.read_boolean():
                metadata[index] = reader.read_position()
        elif value_type == 11:
            metadata[index] = reader.read_varint()
        elif value_type == 12:
            if reader.read_boolean():
                metadata[index] = reader.read_uuid()
        elif value_type == 13:
            metadata[index] = reader.read_varint()
        elif value_type == 14:
            metadata[index] = reader.read_nbt()
        elif value_type == 15:
            metadata[index] = read_particle(reader)
        elif value_type == 16:
            metadata[index] = VillagerData(
                reader.read_varint(),
                reader.read_varint(),
                reader.read_varint()
            )
        elif value_type == 17:
            if reader.read_boolean():
                metadata[index] = reader.read_varint()
        elif value_type == 18:
            metadata[index] = reader.read_varint()
    return metadata

def read_slot(reader):
    return reader.read_nbt()

def read_nbt(reader):
    return parse_nbt(reader)

def read_position(reader):
    value = reader.read_long()
    x = (value & (0x3FFFFFF << 38)) >> 38
    y = value & 0xFFF
    z = (value & (0x3FFFFFF << 12)) >> 12
    if x >= 0x2000000:
        x -= 0x4000000
    if y >= 0x800:
        y -= 0x1000
    if z >= 0x2000000:
        z -= 0x4000000
    return x, y, z

def read_angle(reader):
    return read_byte(reader) / 256

def read_uuid(reader):
    return UUID(bytes=reader.read(16))

def read_byte_array(reader, length):
    return reader.read(length)

class DataReader:
    def __new__(cls, reader):
        reader.read_boolean = types.MethodType(read_boolean, reader)
        reader.read_byte = types.MethodType(read_byte, reader)
        reader.read_ubyte = types.MethodType(read_ubyte, reader)
        reader.read_short = types.MethodType(read_short, reader)
        reader.read_ushort = types.MethodType(read_ushort, reader)
        reader.read_int = types.MethodType(read_int, reader)
        reader.read_long = types.MethodType(read_long, reader)
        reader.read_float = types.MethodType(read_float, reader)
        reader.read_double = types.MethodType(read_double, reader)
        reader.read_string = types.MethodType(read_string, reader)
        reader.read_chat = types.MethodType(read_chat, reader)
        reader.read_identifier = types.MethodType(read_identifier, reader)
        reader.read_varint = types.MethodType(read_varint, reader)
        reader.read_varlong = types.MethodType(read_varlong, reader)
        reader.read_entity_metadata = types.MethodType(read_entity_metadata, reader)
        reader.read_slot = types.MethodType(read_slot, reader)
        reader.read_nbt = types.MethodType(read_nbt, reader)
        reader.read_position = types.MethodType(read_position, reader)
        reader.read_angle = types.MethodType(read_angle, reader)
        reader.read_uuid = types.MethodType(read_uuid, reader)
        reader.read_byte_array = types.MethodType(read_byte_array, reader)
        return reader
