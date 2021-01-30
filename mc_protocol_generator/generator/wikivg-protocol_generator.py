import minecraft_data as mcd
import re
from packet import Packet, PacketJSONEncoder

bound_to_map = {
    'toClient': 'clientbound',
    'toServer': 'serverbound'
}

datatype_map = {
    'varint': 'varint',
    'optvarint': 'optvarint',
    'pstring': 'pstring',
    'u16': 'ushort',
    'u8': 'ubyte',
    'i64': 'long',
    'buffer': 'buffer',
    'i32': 'int',
    'i8': 'byte',
    'bool': 'bool',
    'i16': 'short',
    'f32': 'float',
    'f64': 'double',
    'UUID': 'uuid',
    'option': 'option',
    'entityMetadataLoop': 'entity_metadata_loop',
    'topBitSetTerminatedArray': 'top_bit_set_terminated_array',
    'bitfield': 'bitfield',
    'container': 'container',
    'switch': 'switch',
    'void': 'void',
    'array': 'array',
    'restBuffer': 'rest_buffer',
    'nbt': 'nbt',
    'optionalNbt': 'optnbt',
    'string': 'string',
    'slot': 'slot',
    'particle': 'particle',
    'particleData': 'particle_data',
    'ingredient': 'ingredient',
    'position': 'position',
    'entityMetadataItem': 'entity_metadata_item',
    'entityMetadata': 'entity_metadata',
    
}

_c2s_regex1 = re.compile('(.)([A-Z][a-z]+)')
_c2s_regex2 = re.compile('([a-z0-9])([A-Z])')
_c2s_repl = r'\1_\2'

def camal2snake(value):
    s1 = re.sub(_c2s_regex1, _c2s_repl, value)
    return re.sub(_c2s_regex2, _c2s_repl, s1).lower()

def parse_bound_to_group(bound_to, state_data, state):
    bound_to_name = bound_to_map[bound_to]
    bound_to_data = state_data[bound_to]
    # dict: packet_name -> dict_packet_name
    name_lookup = bound_to_data['types']['packet'][1][1]['type'][1]['fields']
    # dict: packet_id -> packet_name
    packet_id_map = bound_to_data['types']['packet'][1][0]['type'][1]['mappings']
    packets = []
    for packet_id, packet_name in packet_id_map.items():
        dict_packet_name = name_lookup[packet_name]
        packet_data = bound_to_data['types'][dict_packet_name][1]
        fields = [{'name':camal2snake(d['name']), 'type':d['type']} for d in packet_data]
        packets.append(Packet(packet_name, packet_id, state, bound_to_name, fields))
    return packets

def parse_packet_state(state_name, protocol_data):
    state_data = protocol_data[state_name]
    packets = parse_bound_to_group('toClient', state_data, state_name)
    packets.extend(parse_bound_to_group('toServer', state_data, state_name))
    return packets

def parse_packets(mc_data):
    protocol_data = mc_data.protocol
    packets = parse_packet_state('handshaking', protocol_data)
    packets.extend(parse_packet_state('status', protocol_data))
    packets.extend(parse_packet_state('login', protocol_data))
    packets.extend(parse_packet_state('play', protocol_data))
    return packets

def main():
    mc_data = mcd("1.16.4")
    packets = parse_packets(mc_data)
    print(packets)

if __name__ == '__main__':
    main()
