import struct
from . import TagBase
from .. import NBTTag

class ByteTag(TagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def type_id():
        return NBTTag.Byte

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Byte:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        value = reader.read_byte()
        return ByteTag(name, value)

    def __bytes__(self):
        output = bytes(NBTTag.Byte)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>b', self.value)
        return output

    def __repr__(self):
        return f'ByteTag(name={repr(self.name)}, value={repr(self.value)})'
