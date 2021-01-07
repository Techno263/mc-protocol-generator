import struct
from collections.abc import MutableSequence
from . import (TagBase, EndTag, ByteTag, ShortTag, IntTag,
               LongTag, FloatTag, DoubleTag, ByteArrayTag,
               StringTag, CompoundTag, IntArrayTag, LongArrayTag)
from .. import NBTTag

def read_list_helper(reader, type_id, length):
    if type_id == NBTTag.End:
        raise Exception('Cannot have list of End tags')
    elif type_id == NBTTag.Byte:
        return [ByteTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Short:
        return [ShortTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Int:
        return [IntTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Long:
        return [LongTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Float:
        return [FloatTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Double:
        return [DoubleTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.ByteArray:
        return [ByteArrayTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.String:
        return [StringTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.List:
        return [ListTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Compound:
        return [CompoundTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.IntArray:
        return [IntArrayTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.LongArray:
        return [LongArrayTag.read(reader, False, False) for _ in range(length)]
    else:
        raise Exception

class ListTag(TagBase, MutableSequence[TagBase]):
    def __init__(self, name, value, list_type):
        self.name = name
        self.value = value
        self.list_type = list_type

    @staticmethod
    def type_id():
        return NBTTag.List

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.List:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        list_type_id = NBTTag(reader.read_ubyte())
        list_length = reader.read_int()
        value = read_list_helper(reader, list_type_id, list_length)
        return ListTag(name, value, list_type_id.get_type())

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        if not isinstance(value, self.list_type):
            raise TypeError(f'Expected type {self.list_type}, got {type(value)}')
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __len__(self):
        return len(self.value)

    def insert(self, index, object):
        if not isinstance(value, self.list_type):
            raise TypeError(f'Expected type {self.list_type}, got {type(value)}')
        return self.value.insert(index, object)

    def __bytes__(self):
        output = bytes(NBTTag.List)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += 

    def __repr__(self):
        return f'ListTag(name={repr(self.name)}, value={repr(self.value)}, list_type={repr(self.list_type)})'
