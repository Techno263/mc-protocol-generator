import struct
from collections.abc import MutableSequence
from . import TagBase, LongTag
from .. import NBTTag

class LongArrayTag(TagBase, MutableSequence):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def insert(self, index, object):
        self.value.insert(index, object)

    @staticmethod
    def type_id():
        return NBTTag.LongArray

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.LongArray:
                raise Exception
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        length = reader.read_int()
        value = [LongTag.read(reader, False) for _ in range(length)]
        return LongArrayTag(name, value)
    
    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return f'LongArrayTag(name={repr(self.name)}, value={repr(self.value)})'

    def __bytes__(self):
        output = bytes(NBTTag.LongArray)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>i', len(self.value))
        output += b''.join([bytes(tag) for tag in self.values])
        return output
