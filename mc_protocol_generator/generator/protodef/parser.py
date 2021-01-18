from datatypes import (Switch, Option, Int8, UInt8,
    Int16, UInt16, Int32, Int64, Float32, Float64,
    Array, Container, ContainerItem, Count, Bool,
    CString, Void, Buffer, Bitfield, BitfieldItem,
    Mapper, PString)

def parse_protodef(name, options):
    if name == 'switch':
        return Switch.parse(options)
    if name == 'option':
        return Option.parse(options)
    if name == 'i8':
        return Int8.parse(options)
    if name == 'container':
        print(name, ':', options)
        return Container.parse(options)
