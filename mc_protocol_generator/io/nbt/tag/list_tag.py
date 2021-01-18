import struct
from .collections_tag_base import MutableSequenceTagBase
from .. import NBTTag, tag

def read_list_helper(reader, type_id, length):
    if type_id == NBTTag.End:
        if type_id != NBTTag.End:
            raise Exception('Cannot have list of end tags')
        return []
    elif type_id == NBTTag.Byte:
        return [tag.ByteTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Short:
        return [tag.ShortTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Int:
        return [tag.IntTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Long:
        return [tag.LongTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Float:
        return [tag.FloatTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Double:
        return [tag.DoubleTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.ByteArray:
        return [tag.ByteArrayTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.String:
        return [tag.StringTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.List:
        return [tag.ListTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.Compound:
        return [tag.CompoundTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.IntArray:
        return [tag.IntArrayTag.read(reader, False, False) for _ in range(length)]
    elif type_id == NBTTag.LongArray:
        return [tag.LongArrayTag.read(reader, False, False) for _ in range(length)]
    else:
        raise Exception

def get_tag_type(type_id):
    if type_id == NBTTag.End:
        return tag.EndTag
    elif type_id == NBTTag.Byte:
        return tag.ByteTag
    elif type_id == NBTTag.Short:
        return tag.ShortTag
    elif type_id == NBTTag.Int:
        return tag.IntTag
    elif type_id == NBTTag.Long:
        return tag.LongTag
    elif type_id == NBTTag.Float:
        return tag.FloatTag
    elif type_id == NBTTag.Double:
        return tag.DoubleTag
    elif type_id == NBTTag.ByteArray:
        return tag.ByteArray
    elif type_id == NBTTag.String:
        return tag.StringTag
    elif type_id == NBTTag.List:
        return tag.ListTag
    elif type_id == NBTTag.Compound:
        return tag.CompoundTag
    elif type_id == NBTTag.IntArray:
        return tag.IntArrayTag
    elif type_id == NBTTag.LongArray:
        return tag.LongArrayTag
    else:
        raise Exception

def check_item_type(item, target_type):
    return isinstance(item, target_type)

class ListTag(MutableSequenceTagBase):
    def __init__(self, name, value, list_type):
        self.name = name
        if any(not isinstance(item, list_type) for item in value):
            raise Exception(f'Invalid type in list')
        self.value = value
        self.list_type = list_type

    def insert(self, index, object):
        if not isinstance(value, self.list_type):
            raise TypeError(f'Invalid item type. Expected type {self.list_type}, got {type(value)}')
        super().insert(index, object)

    def write(self, writer, write_type_id=True):
        if write_type_id:
            writer.write_ubyte(NBTTag.List)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            writer.write_ushort(len(name_encoded))
            writer.write(name_encoded)
        writer.write_ubyte(self.list_type.type_id())
        writer.write_int(len(self.value))
        for t in self.value:
            t.write(writer, False)

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
        return ListTag(name, value, get_tag_type(list_type_id))

    def __setitem__(self, key, value):
        if not isinstance(value, self.list_type):
            raise TypeError(f'Invalid item type. Expected type {self.list_type}, got {type(value)}')
        super().__setitem__(key, value)

    def __repr__(self):
        return f'ListTag(name={repr(self.name)}, value={repr(self.value)}, list_type={repr(self.list_type)})'

    def __bytes__(self):
        output = bytes(NBTTag.List)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += bytes(self.list_type.type_id())
        output += struct.pack('>i', len(self.value))
        output += b''.join(bytes(t) for t in self.value)
        return output
