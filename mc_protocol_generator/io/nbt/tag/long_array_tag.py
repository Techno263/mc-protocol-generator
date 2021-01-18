import struct
from .collections_tag_base import MutableSequenceTagBase
from .. import NBTTag

class LongArrayTag(MutableSequenceTagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def write(self, writer, write_type_id=True):
        if writer_type_id:
            writer.write_ubyte(NBTTag.LongArray)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            writer.write_ushort(len(name_encoded))
            writer.write(name_encoded)
        writer.write_int(len(self.value))
        for v in self.value:
            writer.write_long(v)

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

    def __repr__(self):
        return f'LongArrayTag(name={repr(self.name)}, value={repr(self.value)})'

    def __bytes__(self):
        output = bytes(NBTTag.LongArray)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += struct.pack('>i', len(self.value))
        output += b''.join([bytes(tag) for tag in self.value])
        return output
