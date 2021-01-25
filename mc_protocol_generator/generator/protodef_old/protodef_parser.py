from .parser import parse_type

'''
def parse_types(namespace, types):
    for name, value in types.items():
        if value == 'native':
            pass
        else:
            parse_type(*value)

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
'''

if __name__ == '__main__':
    import minecraft_data as mcd
    mc_data = mcd("1.16.4")
    parse_protodef(mc_data.protocol)
