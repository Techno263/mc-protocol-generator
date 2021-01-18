import struct
from .collections_tag_base import MutableSequenceTagBase
from .. import NBTTag

class IntArrayTag(MutableSequenceTagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def write(self, writer, write_type_id=True):
        if write_type_id:
            writer.write_ubyte(NBTTag.IntArray)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            writer.write_ushort(len(name_encoded))
            writer.write(name_encoded)
        writer.write_int(len(self.value))
        for v in self.value:
            writer.write_int(v)

    @staticmethod
    def type_id():
        return NBTTag.IntArray

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.IntArray:
                raise Exception
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        length = reader.read_int()
        value = [reader.read_int() for _ in range(length)]
        return IntArrayTag(name, value)

    def __repr__(self):
        return f'IntArrayTag(name={repr(self.name)}, value={repr(self.value)})'

    def __bytes__(self):
        output = bytes(NBTTag.IntArray)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>i', len(self.value))
        output += b''.join([struct.pack('>i', v) for v in self.value])
        return output
