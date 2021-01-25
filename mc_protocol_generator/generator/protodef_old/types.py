from .datatypes import (Switch, Option, Int8, UInt8,
    Int16, UInt16, Int32, Int64, Float32, Float64,
    Varint, Array, Container, ContainerItem, Count,
    Bool, CString, Void, Buffer, Bitfield,
    BitfieldItem, Mapper, PString)

def _get_namespace(namespace):
    if isinstance(namespace, str):
        if len(namespace) > 0:
            namespace = namespace.split('.')
            if '' in namespace:
                raise Exception('Namespace cannot have empty string')
            return namespace
        else:
            return []
    elif isinstance(namespace, list):
        return namespace
    else:
        raise Exception('Cannot parse namespace: {namespace}')

def _get_type_helper(protocol, name, namespace):
    if len(namespace) > 0:
        sub_protocol = protocol[namespace[0]]
        ret = _get_type_helper(sub_protocol, name, namespace[1:])
        if ret == None:
            if 'types' in protocol:
                if name in protocol['types']:
                    return protocol['types'][name]
                else:
                    return None
            else:
                return None
        else:
            return ret
    else:
        if 'types' in protocol:
            if name in protocol['types']:
                return protocol['types'][name]
            else:
                return None
        else:
            return None

def _parse_protodef(protodef, namespace, type_def):
    for key, value in type_def.items():
        if key == 'types':
            for t_name, t_obj in value.items():
                protodef.add_type(namespace, t_name, t_obj)
        else:
            subnamespace = namespace.copy()
            subnamespace.append(key)
            _parse_protodef(protodef, subnamespace, value)

def _parse_type(type_name, type_options):
    if type_name == 'switch':
        return Switch.parse(type_options)
    elif type_name == 'option':
        return Option.parse(type_options)
    elif type_name == 'i8':
        return Int8.parse(type_options)
    elif type_name == 'u8':
        return UInt8.parse(type_options)
    elif type_name == 'i16':
        return Int16.parse(type_options)
    elif type_name == 'u16':
        return UInt16.parse(type_options)
    elif type_name == 'i32':
        return Int32.parse(type_options)
    elif type_name == 'i64':
        return Int64.parse(type_options)
    elif type_name == 'f32':
        return Float32.parse(type_options)
    elif type_name == 'f64':
        return Float64.parse(type_options)
    elif type_name == 'varint':
        return Varint.parse(type_options)
    elif type_name == 'array':
        return Array.parse(type_options)
    elif type_name == 'container':
        return Container.parse(type_options)
    elif type_name == 'bool':
        return Bool.parse(type_options)
    elif type_name == 'void':
        return Void.parse(type_options)
    elif type_name == 'buffer':
        return Buffer.parse(type_options)
    elif type_name == 'bitfield':
        return Bitfield.parse(type_options)
    elif type_name == 'mapper':
        return Mapper.parse(type_options)
    elif type_name == 'pstring':
        return PString.parse(type_options)
    else:
        raise Exception(f'Unexpected type protodef type: {type_name}')

class Protodef:
    def __init__(self, type_def):
        self.protocol = {}
        _parse_protodef(self, [], type_def)

    def add_type(self, namespace, name, obj):
        namespace = _get_namespace(namespace)
        protocol = self.protocol
        for ns in namespace:
            if ns not in protocol:
                protocol[ns] = {}
            protocol = protocol[ns]
        if 'types' not in protocol:
            protocol['types'] = {}
        protocol['types'][name] = obj if obj == 'native' else _parse_type(*obj)

    def get_type(self, name, namespace=''):
        namespace = _get_namespace(namespace)
        value = _get_type_helper(self.protocol, name, namespace)
        return value

'''
class ProtodefTypes(dict):

    def __init__(self, protodef_protocol):
        self.types = {}
        self.subnamespaces = {}

    def __getitem__(self, key):
        ns = _get_namespace(key)
        if len(ns) > 1:
            if ns[0] in self.subnamespaces:
                self.subnamespaces[1:]
            else:
                raise Exception(f'Cannot find namespce {key}')
        else:
            return self.types[ns[0]]

    def __setitem__(self, key, value):
        ns = _get_namespace(key)
        if len(ns) > 1:
            if ns[0] not in self.subnamespaces:
                self.subnamespaces[ns[0]] = ProtodefTypes()
            self.subnamespaces[ns[1:]] = value
        else:
            self.types[ns[0]] = value

    def __delitem__(self, key):
        ns = _get_namespace(key)
        if len(ns) > 1:
            if ns[0] in self.subnamespaces:
                del self.subnamespaces[ns[1:]]
            else:
                raise Exception(f'Cannot find namespce {ns[0]}')
        else:
            if ns[0] in self.types:
                del self.types[ns[0]]
            elif ns[0] in self.subnamespaces:
                del self.subnamespaces[ns[0]]
            else:
                raise Exception(f'Cannot find namespace or type {ns[0]}')

    def __iter__(self):
        yield from iter(self.types)
        for ns in self.subnamespaces.values():
            yield from iter(ns)

    def __len__(self):
        return len(self.types) + sum(len(sns) for sns in self.subnamespaces)

    def _get_namespace(key):
        if isinstance(key, str):
            ns = key.split('.')
        elif isinstance(key, list):
            ns = key
        else:
            raise KeyError(key)

    def _parse_protodef(self, protocol):
        for key, value in protocol.items():
            if key == 'types':
'''