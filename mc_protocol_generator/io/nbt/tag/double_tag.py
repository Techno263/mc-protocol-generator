import struct
from .tag_base import TagBase
from .. import NBTTag

class DoubleTag(TagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def write(self, writer, write_type_id=True):
        if write_type_id:
            writer.write_ubyte(NBTTag.Double)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            writer.write_ushort(len(name_encoded))
            writer.write(name_encoded)
        writer.write_double(self.value)

    @staticmethod
    def type_id():
        return NBTTag.Double

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Double:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        value = reader.read_double()
        return DoubleTag(name, value)

    def __bytes__(self):
        output = bytes(NBTTag.Double)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>d', self.value)
        return output

    def __repr__(self):
        return f'DoubleTag(name={repr(self.name)}, value={repr(self.value)})'
