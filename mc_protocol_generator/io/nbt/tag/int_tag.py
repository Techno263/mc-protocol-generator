import struct
from . import TagBase
from .. import NBTTag

class IntTag(TagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def type_id():
        return NBTTag.Int

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Int:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        value = reader.read_int()
        return IntTag(name, value)

    def __bytes__(self):
        output = bytes(NBTTag.Int)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>i', self.value)
        return output

    def __repr__(self):
        return f'IntTag(name={repr(self.name)}, value={repr(self.value)})'
