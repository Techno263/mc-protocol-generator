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
                    'type': 'uuid'
                },
                {
                    'name': 'Action',
                    'type': 'varint'
                },
                {
                    'type': 'switch',
                    'options': {
                        'switch': {
                            'field': 'Action'
                        },
                        'cases': [
                            {
                                'value': 0,
                                'fields': [
                                    {
                                        'name': 'Title',
                                        'type': 'chat'
                                    },
                                    {
                                        'name': 'Health',
                                        'type': 'float'
                                    },
                                    {
                                        'name': 'Color',
                                        'type': 'varint'
                                    },
                                    {
                                        'name': 'Division',
                                        'type': 'varint'
                                    },
                                    {
                                        'name': 'Flags',
                                        'type': 'ubyte'
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
                                        'type': 'float'
                                    }
                                ]
                            },
                            {
                                'value': 3,
                                'fields': [
                                    {
                                        'name': 'Title',
                                        'type': 'chat'
                                    }
                                ]
                            },
                            {
                                'value': 4,
                                'fields': [
                                    {
                                        'name': 'Color',
                                        'type': 'varint'
                                    },
                                    {
                                        'name': 'Division',
                                        'type': 'varint'
                                    }
                                ]
                            },
                            {
                                'value': 5,
                                'fields': [
                                    {
                                        'name': 'Flags',
                                        'type': 'ubyte'
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
                packet_name = 'Boss Bar'
                packet_id = 12
                packet_state = 'play'
                packet_bound_to = 'client'

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
                    return (
                        dl.varint_size(BossBar.packet_id)
                        + dl.uuid_size
                        + dl.varint_size(self.action)
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
                    return f'BossBar(uuid={repr(self.uuid)}, action={repr(self.action)}, title={repr(self.title)}, health={repr(self.health)}, color={repr(self.color)}, division={repr(self.division)}, flags={repr(self.flags)})'

                def write_packet(self, writer):
                    writer.write_varint(BossBar.packet_id)
                    writer.write_uuid(self.uuid)
                    writer.write_varint(self.action)
                    if self.action == 0:
                        writer.write_chat(self.title)
                        writer.write_float(self.health)
                        writer.write_varint(self.color)
                        writer.write_varint(self.division)
                        writer.write_ubyte(self.flags)
                    elif self.action == 1:
                        pass
                    elif self.action == 2:
                        writer.write_float(self.health)
                    elif self.action == 3:
                        writer.write_chat(self.title)
                    elif self.action == 4:
                        writer.write_varint(self.color)
                        writer.write_varint(self.division)
                    elif self.action == 5:
                        writer.write_ubyte(self.flags)

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
