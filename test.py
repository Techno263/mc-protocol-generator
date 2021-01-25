import minecraft_data as mcd

game_states = ['handshaking', 'status', 'login', 'play']
packet_directions = ['toClient', 'toServer']

def parse_packet_group(packet_data):
    pass

def get_packet_info(packet_data):
    packet_name_conversion = packet_data['packet'][1][1]['type'][1]['fields']
    packets = {packet_name: packet_data[long_packet_name][1] for packet_name, long_packet_name in packet_name_conversion.items()}
    packet_ids = packet_data['packet'][1][0]['type'][1]['mappings']
    packet_ids = {key: value for key, value in packet_ids.items()}
    return packet_ids, packets

def get_all_types(data):
    types = []
    for game_state in game_states:
        game_state_data = data[game_state]
        for direction in packet_directions:
            direction_data = game_state_data[direction]
            for packet in direction_data['packets'].values():
                for field in packet:
                    field_type = field['type']
                    if field_type not in types:
                        types.append(field_type)
    return types

if __name__ == '__main__':
    mc_protocol = mcd("1.16.4").protocol
    data = {}
    for game_state in game_states:
        data[game_state] = game_state_data = {}
        for direction in packet_directions:
            game_state_data[direction] = direction_data = {}
            direction_data['packet_ids'], direction_data['packets'] = get_packet_info(mc_protocol[game_state][direction]['types'])
            assert len(direction_data['packet_ids']) == len(direction_data['packets'])
    import json
    with open('packet_data.json', 'wt') as fp:
        json.dump(data, fp, indent=4)
    all_types = get_all_types(data)
    complex_types = [x[0] for x in all_types if isinstance(x, list)]
    simple_types = [x for x in all_types if isinstance(x, str)]
    print('simple:', sorted(set(simple_types)))
    print('complex:', sorted(set(complex_types)))
    with open('types.json', 'wt') as fp:
        json.dump(get_all_types(data), fp, indent=4)
