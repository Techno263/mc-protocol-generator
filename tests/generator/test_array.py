import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str

from .util import black_mode

class TestArray(unittest.TestCase):
    def test_int_array_packet(self):
        packet_data = {
            'name': 'Int Array Packet',
            'id': 0x10,
            'state': 'handshaking',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Int Array',
                    'type': 'Array',
                    'options': {
                        'count': {
                            'type': 'VarInt'
                        },
                        'element': {
                            'type': 'Int'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class IntArrayPacket:
                name = 'Int Array Packet'
                id = 16
                state = 'handshaking'
                bound_to = 'client'

                def __init__(self, int_array):
                    self.int_array = int_array

                def __len__(self):
                    return (
                        dl.varint_size(len(self.int_array))
                        + sum((dl.int_size for item in self.int_array))
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
        self.assertEqual('Int Array Packet', packet.name)
        self.assertEqual(16, packet.id)
        self.assertEqual('handshaking', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_string_array(self):
        packet_data = {
            'name': 'String Array Packet',
            'id': 0x01,
            'state': 'login',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'String Array',
                    'type': 'Array',
                    'options': {
                        'count': {
                            'type': 'VarInt'
                        },
                        'element': {
                            'type': 'String'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class StringArrayPacket:
                name = 'String Array Packet'
                id = 1
                state = 'login'
                bound_to = 'server'

                def __init__(self, string_array):
                    self.string_array = string_array

                def __len__(self):
                    return (
                        dl.varint_size(len(self.string_array))
                        + sum((dl.string_size(item) for item in self.string_array))
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
        self.assertEqual('String Array Packet', packet.name)
        self.assertEqual(1, packet.id)
        self.assertEqual('login', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_compound_array(self):
        packet_data = {
            'name': 'Tab-Complete (clientbound)',
            'id': 0x0f,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'ID',
                    'type': 'VarInt'
                },
                {
                    'name': 'Start',
                    'type': 'VarInt'
                },
                {
                    'name': 'Length',
                    'type': 'VarInt'
                },
                {
                    'name': 'Matches',
                    'type': 'Array',
                    'options': {
                        'count': {
                            'type': 'VarInt'
                        },
                        'element': {
                            'type': 'Compound',
                            'options': {
                                'fields': [
                                    {
                                        'name': 'Match',
                                        'type': 'String',
                                        'options': {
                                            'max_length': 32767
                                        }
                                    },
                                    {
                                        'name': 'Tooltip',
                                        'type': 'Option',
                                        'options': {
                                            'optional': {
                                                'type': 'Chat'
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
class MatchesItem:
    def __init__(self, match, tooltip):
        self.match = match
        self.tooltip = tooltip

    def __len__(self):
        return dl.string_size(self.match) + (
            0 if self.tooltip == None else dl.chat_size(self.tooltip)
        )
    
    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class TabCompleteClientbound:
    name = 'Tab-Complete (clientbound)'
    id = 15
    state = 'play'
    bound_to = 'client'

    def __init__(self, id, start, length, matches):
        self.id = id
        self.start = start
        self.length = length
        self.matches = matches

    def __len__(self):
        return (
            dl.varint_size(self.id)
            + dl.varint_size(self.start)
            + dl.varint_size(self.length)
            + (
                dl.varint_size(len(self.matches))
                + sum((len(item) for item in self.matches))
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
        self.assertEqual('Tab-Complete (clientbound)', packet.name)
        self.assertEqual(15, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_array_array(self):
        packet_data = {
            'name': 'Array Array Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Outer Array',
                    'type': 'Array',
                    'options': {
                        'count': {
                            'type': 'Int'
                        },
                        'element': {
                            'type': 'Array',
                            'options': {
                                'count': {
                                    'type': 'VarInt'
                                },
                                'element': {
                                    'type': 'String'
                                }
                            }
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class ArrayArrayPacket:
                name = 'Array Array Packet'
                id = 0
                state = 'play'
                bound_to = 'client'

                def __init__(self, outer_array):
                    self.outer_array = outer_array

                def __len__(self):
                    return (
                        dl.int_size
                        + sum((
                            dl.varint_size(len(item))
                            + sum((dl.string_size(item) for item in item))
                            for item in self.outer_array
                        ))
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
        self.assertEqual('Array Array Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_array_option(self):
        packet_data = {
            'name': 'Array Option Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Outer Array',
                    'type': 'Array',
                    'options': {
                        'count': {
                            'type': 'VarInt'
                        },
                        'element': {
                            'type': 'Option',
                            'options': {
                                'optional': {
                                    'type': 'VarInt'
                                }
                            }
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class ArrayOptionPacket:
                name = 'Array Option Packet'
                id = 0
                state = 'play'
                bound_to = 'client'

                def __init__(self, outer_array):
                    self.outer_array = outer_array

                def __len__(self):
                    return (
                        dl.varint_size(len(self.outer_array))
                        + sum ((
                            0 if item == None else dl.varint_size(item)
                            for item in self.outer_array
                        ))
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
        self.assertEqual('Array Option Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
    