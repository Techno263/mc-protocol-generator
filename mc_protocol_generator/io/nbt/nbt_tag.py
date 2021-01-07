from enum import IntEnum
from tag import (EndTag, ByteTag, ShortTag, IntTag,
                 LongTag, FloatTag, DoubleTag, ByteArrayTag,
                 StringTag, ListTag, CompoundTag, IntArrayTag,
                 LongArrayTag)

class NBTTag(IntEnum):
    End = 0
    Byte = 1
    Short = 2
    Int = 3
    Long = 4
    Float = 5
    Double = 6
    ByteArray = 7
    String = 8
    List = 9
    Compound = 10
    IntArray = 11
    LongArray = 12

    def get_type(self):
        if self == End:
            return EndTag
        elif self == Byte:
            return ByteTag
        elif self == Short:
            return ShortTag
        elif self == Int:
            return IntTag
        elif self == Long:
            return LongTag
        elif self == Float:
            return FloatTag
        elif self == Double:
            return DoubleTag
        elif self == ByteArray:
            return ByteArray
        elif self == String:
            return StringTag
        elif self == List:
            return ListTag
        elif self == Compound:
            return CompoundTag
        elif self == IntArray:
            return IntArrayTag
        elif self == LongArray:
            return LongArrayTag
        else:
            raise Exception

    @staticmethod
    def from_bytes(bytes):
        return int.from_bytes(bytes, 'big')

    def __bytes__(self):
        return self.to_bytes(1, 'big')
