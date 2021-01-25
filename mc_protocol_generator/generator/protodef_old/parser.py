from .datatypes import (Switch, Option, Int8, UInt8,
    Int16, UInt16, Int32, Int64, Float32, Float64,
    Varint, Array, Container, ContainerItem, Count,
    Bool, CString, Void, Buffer, Bitfield,
    BitfieldItem, Mapper, PString)

def parse_type(name, options):
    if name == 'switch':
        return Switch.parse(options)
    elif name == 'option':
        return Option.parse(options)
    elif name == 'i8':
        return Int8.parse(options)
    elif name == 'u8':
        return UInt8.parse(options)
    elif name == 'i16':
        return Int16.parse(options)
    elif name == 'u16':
        return UInt16.parse(options)
    elif name == 'i32':
        return Int32.parse(options)
    elif name == 'i64':
        return Int64.parse(options)
    elif name == 'f32':
        return Float32.parse(options)
    elif name == 'f64':
        return Float64.parse(options)
    elif name == 'varint':
        return Varint.parse(options)
    elif name == 'array':
        return Array.parse(options)
    elif name == 'container':
        return Container.parse(options)
    elif name == 'bool':
        return Bool.parse(options)
    elif name == 'void':
        return Void.parse(options)
    elif name == 'buffer':
        return Buffer.parse(options)
    elif name == 'bitfield':
        return Bitfield.parse(options)
    elif name == 'mapper':
        return Mapper.parse(options)
    elif name == 'pstring':
        return PString.parse(options)
    else:
        raise Exception(f'Unexpected type protodef type: {name}')