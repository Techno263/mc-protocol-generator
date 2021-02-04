import mc_protocol_generator.generator.protocol_generator as generator
from mc_protocol_generator.generator.packet import Packet

if __name__ == '__main__':
    import json
    import os
    with open(os.path.join(os.path.dirname(__file__), 'mc_protocol_generator/generator/minecraft-protocol/1.16.5.json'), 'rt', encoding='utf8') as fp:
        packets_data = json.load(fp)
    packets = [Packet.parse_packet_data(packet_data) for packet_data in packets_data]
