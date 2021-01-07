import struct
from . import TagBase
from .. import NBTTag

class ShortTag(TagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def type_id():
        return NBTTag.Short

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Short:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        value = reader.read_short()
        return ShortTag(name, value)

    def __bytes__(self):
        output = bytes(NBTTag.Short)
        if self.name:
            output += struct.pack('>H', len(self.name))
            output += self.name.encode('utf8')
        output += struct.pack('>h', self.values)
        return output

    def __repr__(self):
        return f'ShortTag(name={repr(self.name)}, value={repr(self.value)})'
