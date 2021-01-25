from .base import Base
from .bool import Bool
from .buffer import Buffer
from .entity_metadata import EntityMetadata
from .float32 import Float32
from .float64 import Float64
from .int8 import Int8
from .int16 import Int16
from .int32 import Int32
from .int64 import Int64
from .nbt import NBT
from .position import Position
from .rest_buffer import RestBuffer
from .slot import Slot
from .string import String
from .uint8 import UInt8
from .uint16 import UInt16
from .uuid import UUID
from .varint import Varint

def get_type(type_str):
    if type_str == 'bool': return Bool
    elif type_str == 'buffer': return Buffer
    elif type_str == 'entityMetadata': return EntityMetadata
    elif type_str == 'f32': return Float32
    elif type_str == 'f64': return Float64
    elif type_str == 'i8': return Int8
    elif type_str == 'i16': return Int16
    elif type_str == 'i32': return Int32
    elif type_str == 'i64': return Int64
    elif type_str == 'nbt': return NBT
    elif type_str == 'position': return Position
    elif type_str == 'restBuffer': return RestBuffer
    elif type_str == 'slot': return Slot
    elif type_str == 'string': return String
    elif type_str == 'u8': return UInt8
    elif type_str == 'u16': return UInt16
    elif type_str == 'UUID': return UUID
    elif type_str == 'varint': return Varint
    else: raise Exception(f'Invalid type string: {type_str}')

class Array(Base):
    def __init__(self, name, count_type, array_type):
        super(Array, self).__init__(name)
        self.count_type = get_type(count_type)(f'{self.name}_count')
        self.array_type = get_type(array_type)(f'{self.name}_element')

    def generate_read_code(self, reader_name):
        return (f'{self.count_type.generate_read_code(reader_name)}\n'
                f'{self.name} = [ for _ in range({self.name}_count)]'