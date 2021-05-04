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
                    'type': 'array',
                    'options': {
                        'count': {
                            'type': 'varint'
                        },
                        'element': {
                            'type': 'int'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class IntArrayPacket:
                packet_name = 'Int Array Packet'
                packet_id = 16
                packet_state = 'handshaking'
                packet_bound_to = 'client'

                def __init__(self, int_array):
                    self.int_array = int_array

                def __len__(self):
                    return dl.varint_size(IntArrayPacket.packet_id) + (
                        dl.varint_size(len(self.int_array))
                        + sum((dl.int_size for item in self.int_array))
                    )
                
                def __repr__(self):
                    return f'IntArrayPacket(int_array={repr(self.int_array)})'

                def write_packet(self, writer):
                    writer.write_varint(IntArrayPacket.packet_id)
                    writer.write_varint(len(self.int_array))
                    for item in self.int_array:
                        writer.write_int(item)

                @staticmethod
                def read_packet(reader):
                    int_array = [reader.read_int() for _ in range(reader.read_varint())]
                    return IntArrayPacket(int_array)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Int Array Packet', packet.name)
        self.assertEqual(16, packet.id)
        self.assertEqual('handshaking', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'array',
                    'options': {
                        'count': {
                            'type': 'varint'
                        },
                        'element': {
                            'type': 'string'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class StringArrayPacket:
                packet_name = 'String Array Packet'
                packet_id = 1
                packet_state = 'login'
                packet_bound_to = 'server'

                def __init__(self, string_array):
                    self.string_array = string_array

                def __len__(self):
                    return dl.varint_size(StringArrayPacket.packet_id) + (
                        dl.varint_size(len(self.string_array))
                        + sum((dl.string_size(item) for item in self.string_array))
                    )
                
                def __repr__(self):
                    return f'StringArrayPacket(string_array={repr(self.string_array)})'

                def write_packet(self, writer):
                    writer.write_varint(StringArrayPacket.packet_id)
                    writer.write_varint(len(self.string_array))
                    for item in self.string_array:
                        writer.write_string(item)

                @staticmethod
                def read_packet(reader):
                    string_array = [
                        reader.read_string()
                        for _ in range(reader.read_varint())
                    ]
                    return StringArrayPacket(
                        string_array
                    )
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('String Array Packet', packet.name)
        self.assertEqual(1, packet.id)
        self.assertEqual('login', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'varint'
                },
                {
                    'name': 'Start',
                    'type': 'varint'
                },
                {
                    'name': 'Length',
                    'type': 'varint'
                },
                {
                    'name': 'Matches',
                    'type': 'array',
                    'options': {
                        'count': {
                            'type': 'varint'
                        },
                        'element': {
                            'type': 'compound',
                            'options': {
                                'fields': [
                                    {
                                        'name': 'Match',
                                        'type': 'string',
                                        'options': {
                                            'max_length': 32767
                                        }
                                    },
                                    {
                                        'name': 'Tooltip',
                                        'type': 'option',
                                        'options': {
                                            'optional': {
                                                'type': 'chat'
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
            dl.bool_size
            + (0 if self.tooltip == None else dl.chat_size(self.tooltip))
        )
    
    def __repr__(self):
        return f'MatchesItem(match={repr(self.match)}, tooltip={repr(self.tooltip)})'

    def write_data(self, writer):
        writer.write_string(self.match)
        tooltip_check = self.tooltip != None
        writer.write_bool(tooltip_check)
        if tooltip_check:
            writer.write_chat(self.tooltip)

    @staticmethod
    def read_data(reader):
        match = reader.read_string()
        tooltip = reader.read_chat() if reader.read_bool() else None
        return MatchesItem(
            match,
            tooltip
        )

class TabCompleteClientbound:
    packet_name = 'Tab-Complete (clientbound)'
    packet_id = 15
    packet_state = 'play'
    packet_bound_to = 'client'

    def __init__(self, id, start, length, matches):
        self.id = id
        self.start = start
        self.length = length
        self.matches = matches

    def __len__(self):
        return (
            dl.varint_size(TabCompleteClientbound.packet_id)
            + dl.varint_size(self.id)
            + dl.varint_size(self.start)
            + dl.varint_size(self.length)
            + (
                dl.varint_size(len(self.matches))
                + sum((len(item) for item in self.matches))
            )
        )
    
    def __repr__(self):
        return f'TabCompleteClientbound(id={repr(self.id)}, start={repr(self.start)}, length={repr(self.length)}, matches={repr(self.matches)})'

    def write_packet(self, writer):
        writer.write_varint(TabCompleteClientbound.packet_id)
        writer.write_varint(self.id)
        writer.write_varint(self.start)
        writer.write_varint(self.length)
        writer.write_varint(len(self.matches))
        for item in self.matches:
            item.write_data(writer)

    @staticmethod
    def read_packet(reader):
        id = reader.read_varint()
        start = reader.read_varint()
        length = reader.read_varint()
        matches = [
            MatchesItem.read_data(reader)
            for _ in range(reader.read_varint())
        ]
        return TabCompleteClientbound(
            id,
            start,
            length,
            matches
        )
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Tab-Complete (clientbound)', packet.name)
        self.assertEqual(15, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'array',
                    'options': {
                        'count': {
                            'type': 'int'
                        },
                        'element': {
                            'type': 'array',
                            'options': {
                                'count': {
                                    'type': 'varint'
                                },
                                'element': {
                                    'type': 'string'
                                }
                            }
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class ArrayArrayPacket:
                packet_name = 'Array Array Packet'
                packet_id = 0
                packet_state = 'play'
                packet_bound_to = 'client'

                def __init__(self, outer_array):
                    self.outer_array = outer_array

                def __len__(self):
                    return dl.varint_size(ArrayArrayPacket.packet_id) + (
                        dl.int_size
                        + sum((
                            dl.varint_size(len(item))
                            + sum((dl.string_size(item) for item in item))
                            for item in self.outer_array
                        ))
                    )

                def __repr__(self):
                    return f'ArrayArrayPacket(outer_array={repr(self.outer_array)})'

                def write_packet(self, writer):
                    writer.write_varint(ArrayArrayPacket.packet_id)
                    writer.write_int(len(self.outer_array))
                    for item in self.outer_array:
                        writer.write_varint(len(item))
                        for item in item:
                            writer.write_string(item)

                @staticmethod
                def read_packet(reader):
                    outer_array = [
                        [
                            reader.read_string()
                            for _ in range(reader.read_varint())
                        ]
                        for _ in range(reader.read_int())
                    ]
                    return ArrayArrayPacket(
                        outer_array
                    )
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Array Array Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'array',
                    'options': {
                        'count': {
                            'type': 'varint'
                        },
                        'element': {
                            'type': 'option',
                            'options': {
                                'optional': {
                                    'type': 'varint'
                                }
                            }
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
            class ArrayOptionPacket:
                packet_name = 'Array Option Packet'
                packet_id = 0
                packet_state = 'play'
                packet_bound_to = 'client'

                def __init__(self, outer_array):
                    self.outer_array = outer_array

                def __len__(self):
                    return (
                        dl.varint_size(ArrayOptionPacket.packet_id) + (
                            dl.varint_size(len(self.outer_array))
                            + sum ((
                                dl.bool_size
                                + (0 if item == None else dl.varint_size(item))
                                for item in self.outer_array
                            ))
                        )
                    )
                
                def __repr__(self):
                    return f'ArrayOptionPacket(outer_array={repr(self.outer_array)})'

                def write_packet(self, writer):
                    writer.write_varint(ArrayOptionPacket.packet_id)
                    writer.write_varint(len(self.outer_array))
                    for item in self.outer_array:
                        outer_array_item_check = item != None
                        writer.write_bool(outer_array_item_check)
                        if outer_array_item_check:
                            writer.write_varint(item)

                @staticmethod
                def read_packet(reader):
                    outer_array = [
                        reader.read_varint() if reader.read_bool() else None
                        for _ in range(reader.read_varint())
                    ]
                    return ArrayOptionPacket(
                        outer_array
                    )
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Array Option Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
    