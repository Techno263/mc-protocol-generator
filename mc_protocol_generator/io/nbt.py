from enum import IntEnum

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

def read_name(reader):
    length = reader.read_ushort()
    name = reader.read(length).decode('utf8')
    return name

def parse_list_helper(reader, type_id):
    if type_id == NBTTag.End:
        return None
    elif type_id == NBTTag.Byte:
        value = reader.read_byte()
        return value
    elif type_id == NBTTag.Short:
        value = reader.read_short()
        return value
    elif type_id == NBTTag.Int:
        value = reader.read_int()
        return value
    elif type_id == NBTTag.Long:
        value = reader.read_long()
        return value
    elif type_id == NBTTag.Float:
        value = reader.read_float()
        return value
    elif type_id == NBTTag.Double:
        value = reader.read_double()
        return value
    elif type_id == NBTTag.ByteArray:
        length = reader.read_int()
        value = reader.read(length)
        return value
    elif type_id == NBTTag.String:
        length = reader.read_ushort()
        value = reader.read(length).decode('utf8')
        return value
    elif type_id == NBTTag.List:
        list_type = reader.read_ubyte()
        length = reader.read_int()
        value = [parse_list_helper(reader) for _ in range(length)]
        return value
    elif type_id == NBTTag.Compound:
        value = {}
        output = parse_nbt_helper(reader)
        while output != None:
            name, data = output
            value[name] = data
            output = parse_nbt_helper(reader)
        return value
    elif type_id == NBTTag.IntArray:
        length = reader.read_int()
        value = [reader.read_int() for _ in range(length)]
        return value
    elif type_id == NBTTag.LongArray:
        length = reader.read_int()
        value = [reader.read_long() for _ in range(length)]
        return value
    else:
        raise Exception('Unable to parse NBT data')

def parse_nbt_helper(reader):
    type_id = reader.read_ubyte()
    if type_id == NBTTag.End:
        return None
    elif type_id == NBTTag.Byte:
        name = read_name(reader)
        value = reader.read_byte()
        return name, value
    elif type_id == NBTTag.Short:
        name = read_name(reader)
        value = reader.read_short()
        return name, value
    elif type_id == NBTTag.Int:
        name = read_name(reader)
        value = reader.read_int()
        return name, value
    elif type_id == NBTTag.Long:
        name = read_name(reader)
        value = reader.read_long()
        return name, value
    elif type_id == NBTTag.Float:
        name = read_name(reader)
        value = reader.read_float()
        return name, value
    elif type_id == NBTTag.Double:
        name = read_name(reader)
        value = reader.read_double()
        return name, value
    elif type_id == NBTTag.ByteArray:
        name = read_name(reader)
        length = reader.read_int()
        value = reader.read(length)
        return name, value
    elif type_id == NBTTag.String:
        name = read_name(reader)
        length = reader.read_ushort()
        value = reader.read(length).decode('utf8')
        return name, value
    elif type_id == NBTTag.List:
        name = read_name(reader)
        list_type = reader.read_ubyte()
        length = reader.read_int()
        value = [parse_list_helper(reader, list_type) for _ in range(length)]
        return name, value
    elif type_id == NBTTag.Compound:
        name = read_name(reader)
        value = {}
        output = parse_nbt_helper(reader)
        while output != None:
            name, data = output
            value[name] = data
            output = parse_nbt_helper(reader)
        return name, value
    elif type_id == NBTTag.IntArray:
        name = read_name(reader)
        length = reader.read_int()
        value = [reader.read_int() for _ in range(length)]
        return name, value
    elif type_id == NBTTag.LongArray:
        name = read_name(reader)
        length = reader.read_int()
        value = [reader.read_long() for _ in range(length)]
        return name, value
    else:
        raise Exception('Unable to parse NBT data')

def parse_nbt(reader):
    output = parse_nbt_helper(reader)
    if output == None:
        return None
    else:
        name, value = output
        return {name: value}
