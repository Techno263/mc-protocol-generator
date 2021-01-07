import struct
from collections.abc import MutableMapping, Iterator
from . import (TagBase, EndTag, ByteTag, ShortTag, IntTag,
               LongTag, FloatTag, DoubleTag, ByteArrayTag,
               StringTag, ListTag)
from .. import NBTTag

class CompoundTagNameIterator(Iterator):
    def __init__(self, compound_iter):
        self._iter = compound_iter

    def __next__(self):
        return next(self._iter).name

class CompoundTag(TagBase, MutableMapping):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def type_id():
        return NBTTag.Compound

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Compound:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        # TODO: parse nested tags inside the compound

    def __getitem__(self, key):
        for tag in self.value:
            if tag.name == key:
                return tag
        raise KeyError

    def __setitem__(self, key, value: TagBase):
        if key != None and key != value.name:
            self.value.append(value)
        else:
            raise KeyError

    def __delitem__(self, key):
        for i, tag in enumerate(self.value):
            if tag.name == key:
                del self.value[i]
        return KeyError

    def __iter__(self):
        return CompoundTagNameIterator(iter(self.value))

    def __len__(self):
        return len(self.value)
    
    def __repr__(self):
        return f'CompoundTag(name={repr(self.name)}, value={repr(self.value)})'

    def __bytes__(self):
        output = bytes(NBTTag.Compound)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += b''.join([bytes(tag) for tag in self.value])
        output += bytes(EndTag())
        return output
