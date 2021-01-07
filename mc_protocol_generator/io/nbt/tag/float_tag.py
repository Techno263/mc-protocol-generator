import struct
from . import TagBase
from .. import NBTTag

class FloatTag(TagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def type_id:
        return NBTTag.Float

    @staticmethod
    def read(reader):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Float:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        value = reader.read_float()
        return FloatTag(name, value)

    def __bytes__(self):
        output = bytes(NBTTag.Float)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>f', self.value)
        return output

    def __repr__(self):
        return f'FloatTag(name={repr(self.name)}, value={repr(self.value)})'
