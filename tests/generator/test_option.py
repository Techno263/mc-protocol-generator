import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str

from .util import black_mode

class TestOption(unittest.TestCase):
    def test_option_int(self):
        packet_data = {
            'name': 'Int Option Packet',
            'id': 0x02,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Optional Int',
                    'type': 'Option',
                    'options': {
                        'optional': {
                            'type': 'Int'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class IntOptionPacket:
                name = 'Int Option Packet'
                id = 2
                state = 'play'
                bound_to = 'client'

                def __init__(self, optional_int):
                    self.optional_int = optional_int

                def __len__(self):
                    return 0 if self.optional_int == None else dl.int_size
                
                def __repr__(self):
                    pass

                def write_packet(self, writer):
                    pass

                @staticmethod
                def read_packet(reader):
                    pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Int Option Packet', packet.name)
        self.assertEqual(2, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_option_string(self):
        packet_data = {
            'name': 'String Option Packet',
            'id': 0x03,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'Optional String',
                    'type': 'Option',
                    'options': {
                        'optional': {
                            'type': 'String'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class StringOptionPacket:
                name = 'String Option Packet'
                id = 3
                state = 'play'
                bound_to = 'server'

                def __init__(self, optional_string):
                    self.optional_string = optional_string

                def __len__(self):
                    return 0 if self.optional_string == None else dl.string_size(self.optional_string)

                def __repr__(self):
                    pass

                def write_packet(self, writer):
                    pass

                @staticmethod
                def read_packet(reader):
                    pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('String Option Packet', packet.name)
        self.assertEqual(3, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
