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
                packet_name = 'Int Option Packet'
                packet_id = 2
                packet_state = 'play'
                packet_bound_to = 'client'

                def __init__(self, optional_int):
                    self.optional_int = optional_int

                def __len__(self):
                    return (
                        dl.varint_size(IntOptionPacket.packet_id)
                        + (0 if self.optional_int == None else dl.int_size)
                    )
                
                def __repr__(self):
                    return f'IntOptionPacket(optional_int={repr(self.optional_int)})'

                def write_packet(self, writer):
                    writer.write_varint(IntOptionPacket.packet_id)
                    optional_int_check = self.optional_int != None
                    writer.write_bool(optional_int_check)
                    if optional_int_check:
                        writer.write_int(self.optional_int)

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
                packet_name = 'String Option Packet'
                packet_id = 3
                packet_state = 'play'
                packet_bound_to = 'server'

                def __init__(self, optional_string):
                    self.optional_string = optional_string

                def __len__(self):
                    return (
                        dl.varint_size(StringOptionPacket.packet_id)
                        + (0 if self.optional_string == None else dl.string_size(self.optional_string))
                    )

                def __repr__(self):
                    return f'StringOptionPacket(optional_string={repr(self.optional_string)})'

                def write_packet(self, writer):
                    writer.write_varint(StringOptionPacket.packet_id)
                    optional_string_check = self.optional_string != None
                    writer.write_bool(optional_string_check)
                    if optional_string_check:
                        writer.write_string(self.optional_string)

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

    def test_option_array(self):
        packet_data = {
            'name': 'Array Option Packet',
            'id': 0x03,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'Optional Array',
                    'type': 'Option',
                    'options': {
                        'optional': {
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
                    }
                }
            ]
        }
        packet_src_code = '''
            class ArrayOptionPacket:
                packet_name = 'Array Option Packet'
                packet_id = 3
                packet_state = 'play'
                packet_bound_to = 'server'

                def __init__(self, optional_array):
                    self.optional_array = optional_array

                def __len__(self):
                    return (
                        dl.varint_size(ArrayOptionPacket.packet_id)
                        + (
                            0 if self.optional_array == None else 
                            dl.varint_size(len(self.optional_array))
                            + sum((dl.int_size for item in self.optional_array))
                        )
                    )

                def __repr__(self):
                    return f'ArrayOptionPacket(optional_array={repr(self.optional_array)})'

                def write_packet(self, writer):
                    writer.write_varint(ArrayOptionPacket.packet_id)
                    optional_array_check = self.optional_array != None
                    writer.write_bool(optional_array_check)
                    if optional_array_check:
                        writer.write_varint(len(self.optional_array))
                        for item in self.optional_array:
                            writer.write_int(item)

                @staticmethod
                def read_packet(reader):
                    pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Array Option Packet', packet.name)
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

    def test_option_compound(self):
        packet_data = {
            'name': 'Compound Option Packet',
            'id': 0x03,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'Optional Compound',
                    'type': 'Option',
                    'options': {
                        'optional': {
                            'type': 'Compound',
                            'options': {
                                'fields': [
                                    {
                                        'name': 'Field1',
                                        'type': 'Short'
                                    },
                                    {
                                        'name': 'Field2',
                                        'type': 'String'
                                    }
                                ]
                            }
                        }
                    }
                }
            ]
        }
        packet_src_code = '''
class OptionalCompound:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __len__(self):
        return dl.short_size + dl.string_size(self.field2)

    def __repr__(self):
        return f'OptionalCompound(field1={repr(self.field1)}, field2={repr(self.field2)})'

    def write_data(self, writer):
        writer.write_short(self.field1)
        writer.write_string(self.field2)

    @staticmethod
    def read_data(reader):
        pass

class CompoundOptionPacket:
    packet_name = 'Compound Option Packet'
    packet_id = 3
    packet_state = 'play'
    packet_bound_to = 'server'

    def __init__(self, optional_compound):
        self.optional_compound = optional_compound

    def __len__(self):
        return (
            dl.varint_size(CompoundOptionPacket.packet_id)
            + (0 if self.optional_compound == None else len(self.optional_compound))
        )

    def __repr__(self):
        return f'CompoundOptionPacket(optional_compound={repr(self.optional_compound)})'

    def write_packet(self, writer):
        writer.write_varint(CompoundOptionPacket.packet_id)
        optional_compound_check = self.optional_compound != None
        writer.write_bool(optional_compound_check)
        if optional_compound_check:
            self.optional_compound.write_data(writer)

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound Option Packet', packet.name)
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
