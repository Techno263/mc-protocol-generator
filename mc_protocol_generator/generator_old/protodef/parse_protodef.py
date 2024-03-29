game_states = ['handshaking', 'status', 'login', 'play']
packet_directions = ['toClient', 'toServer']

def get_group_packet_info(packet_data):
    packet_name_conversion = packet_data['packet'][1][1]['type'][1]['fields']
    packets = {packet_name: packet_data[long_packet_name][1] for packet_name, long_packet_name in packet_name_conversion.items()}
    packet_ids = packet_data['packet'][1][0]['type'][1]['mappings']
    packet_ids = {key: value for key, value in packet_ids.items()}
    return packet_ids, packets

def strip_protodef(protodef):
    data = {}
    for game_state in game_states:
        data[game_state] = game_state_data = {}
        for direction in packet_directions:
            game_state_data[direction] = direction_data = {}
            direction_data['packet_ids'], direction_data['packets'] = get_packet_info(mc_protocol[game_state][direction]['types'])
            assert len(direction_data['packet_ids']) == len(direction_data['packets'])
    return data

def build_packet_parsers(packet_data):
    