from datatypes import (Switch, Option, Int8, UInt8,
    Int16, UInt16, Int32, Int64, Float32, Float64,
    Array, Container, ContainerItem, Count, Bool,
    CString, Void, Buffer, Bitfield, BitfieldItem,
    Mapper, PString)

def parse_types(namespace, types):
    for name, value in types.items():
        if value == 'native':
            pass
            #print(key, ':', 'native')
        else:
            global a
            if type(value) != list:
                print(type(value), ':', value)
            a.add(type(value))

def parse_nested_protodef(proto, namespace):
    for key, value in proto.items():
        if key == 'types':
            parse_types(namespace, value)
        else:
            parse_nested_protodef(value, f'{namespace}.{key}')

def parse_protodef(proto):
    for key, value in proto.items():
        if key == 'types':
            parse_types('', value)
        else:
            parse_nested_protodef(value, key)

if __name__ == '__main__':
    import minecraft_data as mcd
    a = set()
    mc_data = mcd("1.16.4")
    parse_protodef(mc_data.protocol)
    print(a)
