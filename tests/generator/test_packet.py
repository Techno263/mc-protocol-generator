import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str

from .util import black_mode

class TestPacket(unittest.TestCase):
    def test_boss_bar(self):
        packet_data = {
            'name': 'Boss Bar',
            'id': 0x0C,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'UUID',
                    'type': 'UUID'
                },
                {
                    'name': 'Action',
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
                                        'name': 'Title',
                                        'type': 'Chat'
                                    },
                                    {
                                        'name': 'Health',
                                        'type': 'Float'
                                    },
                                    {
                                        'name': 'Color',
                                        'type': 'VarInt'
                                    },
                                    {
                                        'name': 'Division',
                                        'type': 'VarInt'
                                    },
                                    {
                                        'name': 'Flags',
                                        'type': 'UByte'
                                    }
                                ]
                            },
                            {
                                'value': 1,
                                'fields': []
                            },
                            {
                                'value': 2,
                                'fields': [
                                    {
                                        'name': 'Health',
                                        'type': 'Float'
                                    }
                                ]
                            },
                            {
                                'value': 3,
                                'fields': [
                                    {
                                        'name': 'Title',
                                        'type': 'Chat'
                                    }
                                ]
                            },
                            {
                                'value': 4,
                                'fields': [
                                    {
                                        'name': 'Color',
                                        'type': 'VarInt'
                                    },
                                    {
                                        'name': 'Division',
                                        'type': 'VarInt'
                                    }
                                ]
                            },
                            {
                                'value': 5,
                                'fields': [
                                    {
                                        'name': 'Flags',
                                        'type': 'UByte'
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
            class BossBar:
                name = 'Boss Bar'
                id = 12
                state = 'play'
                bound_to = 'client'

                def __init__(self,
                             uuid,
                             action,
                             title=None,
                             health=None,
                             color=None,
                             division=None,
                             flags=None
                ):
                    self.uuid = uuid
                    self.action = action
                    self.title = title
                    self.health = health
                    self.color = color
                    self.division = division
                    self.flags = flags

                def __len__(self):
                    return dl.uuid_size + (
                        dl.varint_size(self.action)
                        + (
                            dl.chat_size(self.title) + dl.float_size + dl.varint_size(self.color) + dl.varint_size(self.division) + dl.ubyte_size
                            if self.action == 0 else
                            0 if self.action == 1 else
                            dl.float_size if self.action == 2 else
                            dl.chat_size(self.title) if self.action == 3 else
                            dl.varint_size(self.color) + dl.varint_size(self.division)
                            if self.action == 4 else
                            dl.ubyte_size if self.action == 5 else 0
                        )
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
        self.assertEqual('Boss Bar', packet.name)
        self.assertEqual(12, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
