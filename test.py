import mc_protocol_generator.generator.protocol_generator as generator
from mc_protocol_generator.generator.packet import Packet
from pprint import pprint

handshake_packet = '''{
        "name": "Handshake",
        "id": "0x00",
        "state": "Handshaking",
        "bound_to": "Server",
        "fields": [
            {
                "name": "Protocol Version",
                "type": "VarInt"
            },
            {
                "name": "Server Address",
                "type": "String",
                "options": {
                    "max_length": 255
                }
            },
            {
                "name": "Server Port",
                "type": "UShort"
            },
            {
                "name": "Next State",
                "type": "VarInt",
                "options": {
                    "enum": "Handshaking Next State"
                }
            }
        ]
    }'''

if __name__ == '__main__':
    import json
    import os
    with open(os.path.join(os.path.dirname(__file__), 'mc_protocol_generator/generator/minecraft-protocol/1.16.5.json'), 'rt', encoding='utf8') as fp:
        packets_data = json.load(fp)
    packet_data = json.loads(handshake_packet)
    handshake = Packet.parse_packet_data(packet_data)
    print(handshake.get_code_str())
