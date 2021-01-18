from . import NBTTag, tag

def parse_nbt(reader, has_name=True, has_type_id=True):
    type_id = NBTTag(reader.read_ubyte())
    if type_id == NBTTag.End:
        return tag.EndTag.read(reader)
    if type_id == NBTTag.Byte:
        return tag.ByteTag.read(reader)
    elif type_id == NBTTag.Short:
        return tag.ShortTag.read(reader)
    elif type_id == NBTTag.Int:
        return tag.IntTag.read(reader)
    elif type_id == NBTTag.Long:
        return tag.LongTag.read(reader)
    elif type_id == NBTTag.Float:
        return tag.FloatTag.read(reader)
    elif type_id == NBTTag.Double:
        return tag.DoubleTag.read(reader)
    elif type_id == NBTTag.ByteArray:
        return tag.ByteArrayTag.read(reader)
    elif type_id == NBTTag.String:
        return tag.StringTag.read(reader)
    elif type_id == NBTTag.List:
        return tag.ListTag.read(reader)
    elif type_id == NBTTag.Compound:
        return tag.CompoundTag.read(reader)
    elif type_id == NBTTag.IntArray:
        return tag.IntArrayTag.read(reader)
    elif type_id == NBTTag.LongArray:
        return tag.LongArrayTag.read(reader)
    else:
        raise Exception
