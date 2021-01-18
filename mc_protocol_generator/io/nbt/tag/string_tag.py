import struct
from .collections_tag_base import SequenceTagBase
from .. import NBTTag

class StringTag(SequenceTagBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def write(self, writer, write_type_id=True):
        if write_type_id:
            writer.write_ubyte(NBTTag.String)
        if self.name != None:
            name_encoded = self.name.encode('utf8')
            writer.write_ushort(len(name_encoded))
            writer.write(name_encoded)
        encoded = self.value.encode('utf8')
        writer.write_ushort(len(encoded))
        writer.write(encoded)

    @staticmethod
    def type_id():
        return NBTTag.String

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.String:
                raise Exception()
        if has_name:
            name_length = reader.read_ushort()
            name = reader.read(name_length).decode('utf8')
        else:
            name = None
        length = reader.read_ushort()
        value = reader.read(length).decode('utf8')
        return StringTag(name, value)

    def __bytes__(self):
        output = bytes(NBTTag.String)
        if self.name:
            name_encoded = self.name.encode('utf8')
            output += struct.pack('>H', len(name_encoded))
            output += name_encoded
        encoded = self.value.encode('utf8')
        output += struct.pack('>H', len(encoded))
        output += encoded
        return output
    
    def __repr__(self):
        return f'StringTag(name={repr(self.name)}, value={repr(self.value)})'
