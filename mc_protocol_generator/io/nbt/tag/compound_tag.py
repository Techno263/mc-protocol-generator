import struct
from .collections_tag_base import MutableMappingTagBase
from .. import NBTTag, tag

class CompoundTag(MutableMappingTagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def write(self, writer, write_type_id=True):
        if write_type_id:
            writer.write_ubyte(NBTTag.Compound)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            writer.write_ushort(len(name_encoded))
            writer.write(name_encoded)
        for t in self.value:
            t.write(writer)
        tag.EndTag().write(writer)

    @staticmethod
    def type_id():
        return NBTTag.Compound

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        from .. import parse_nbt
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.Compound:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        value = []
        t = parse_nbt(reader)
        while t != tag.EndTag():
            value.append(t)
            t = parse_nbt(reader)
        return CompoundTag(name, value)

    def __repr__(self):
        return f'CompoundTag(name={repr(self.name)}, value={repr(self.value)})'

    def __bytes__(self):
        output = bytes(NBTTag.Compound)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        output += b''.join([bytes(t) for t in self.value])
        output += bytes(tag.EndTag())
        return output
