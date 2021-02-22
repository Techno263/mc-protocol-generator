import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str

from .util import black_mode

class TestSwitch(unittest.TestCase):
    def test_basic_switch(self):
        packet_data = {
            'name': 'Switch Packet',
            'id': 0x11,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'Switch Value',
                    'type': 'Switch',
                    'options': {
                        'switch': {
                            'type': 'VarInt'
                        },
                        'cases': [
                            {
                                'value': 0,
                                'fields': [
                                    {
                                        'name': 'Field1',
                                        'type': 'VarInt',
                                    },
                                    {
                                        'name': 'Field2',
                                        'type': 'UByte'
                                    },
                                    {
                                        'name': 'Field3',
                                        'type': 'Short'
                                    }
                                ]
                            },
                            {
                                'value': 1,
                                'fields': [
                                    {
                                        'name': 'Field4',
                                        'type': 'String'
                                    }
                                ]
                            },
                            {
                                'value': 2,
                                'fields': []
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
class SwitchPacket:
    name = 'Switch Packet'
    id = 17
    state = 'play'
    bound_to = 'server'

    def __init__(self, switch_value, field1=None, field2=None, field3=None,
                 field4=None):
        self.switch_value = switch_value
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4

    def __len__(self):
        return dl.varint_size(self.switch_value) + (
            dl.varint_size(self.field1) + dl.ubyte_size + dl.short_size if self.switch_value == 0 else 
                dl.string_size(self.field4) if self.switch_value == 1 else
                    0 if self.switch_value == 2 else 0
        )
    
    def __repr__(self):
        pass

    def write_packet(self, writer):
        pass

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Switch Packet', packet.name)
        self.assertEqual(17, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
