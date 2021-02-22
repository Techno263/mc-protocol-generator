import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str

from .util import black_mode

class TestCompound(unittest.TestCase):
    def test_basic_compound(self):
        packet_data = {
            'name': 'Basic Compound Packet',
            'id': 0x04,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Basic Compound',
                    'type': 'Compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Angle Value',
                                'type': 'Angle'
                            },
                            {
                                'name': 'Bool Value',
                                'type': 'Bool'
                            },
                            {
                                'name': 'Byte Value',
                                'type': 'Byte'
                            },
                            {
                                'name': 'Chat Value',
                                'type': 'Chat'
                            },
                            {
                                'name': 'Double Value',
                                'type': 'Double'
                            },
                            {
                                'name': 'Float Value',
                                'type': 'Float'
                            },
                            {
                                'name': 'Identifier Value',
                                'type': 'Identifier'
                            },
                            {
                                'name': 'Int Value',
                                'type': 'Int'
                            },
                            {
                                'name': 'Long Value',
                                'type': 'Long'
                            },
                            {
                                'name': 'NBT Value',
                                'type': 'NBT'
                            },
                            {
                                'name': 'Position Value',
                                'type': 'Position'
                            },
                            {
                                'name': 'Short Value',
                                'type': 'Short'
                            },
                            {
                                'name': 'Slot Value',
                                'type': 'Slot'
                            },
                            {
                                'name': 'String Value',
                                'type': 'String',
                                'options': {
                                    'max_length': 255
                                }
                            },
                            {
                                'name': 'UByte Value',
                                'type': 'UByte'
                            },
                            {
                                'name': 'UShort Value',
                                'type': 'UShort'
                            },
                            {
                                'name': 'UUID Value',
                                'type': 'UUID'
                            },
                            {
                                'name': 'VarInt Value',
                                'type': 'VarInt'
                            },
                            {
                                'name': 'VarLong Value',
                                'type': 'VarLong'
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
class BasicCompound:
    def __init__(self, angle_value, bool_value, byte_value,
                    chat_value, double_value, float_value,
                    identifier_value, int_value, long_value,
                    nbt_value, position_value, short_value,
                    slot_value, string_value, ubyte_value,
                    ushort_value, uuid_value, varint_value,
                    varlong_value):
        self.angle_value = angle_value
        self.bool_value = bool_value
        self.byte_value = byte_value
        self.chat_value = chat_value
        self.double_value = double_value
        self.float_value = float_value
        self.identifier_value = identifier_value
        self.int_value = int_value
        self.long_value = long_value
        self.nbt_value = nbt_value
        self.position_value = position_value
        self.short_value = short_value
        self.slot_value = slot_value
        self.string_value = string_value
        self.ubyte_value = ubyte_value
        self.ushort_value = ushort_value
        self.uuid_value = uuid_value
        self.varint_value = varint_value
        self.varlong_value = varlong_value
    
    def __len__(self):
        return (
            dl.angle_size +
            dl.bool_size +
            dl.byte_size +
            dl.chat_size(self.chat_value) +
            dl.double_size +
            dl.float_size +
            dl.identifier_size(self.identifier_value) +
            dl.int_size +
            dl.long_size +
            dl.nbt_size(self.nbt_value) +
            dl.position_size +
            dl.short_size +
            dl.slot_size(self.slot_value) +
            dl.string_size(self.string_value) +
            dl.ubyte_size +
            dl.ushort_size +
            dl.uuid_size +
            dl.varint_size(self.varint_value) +
            dl.varlong_size(self.varlong_value)
        )

    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class BasicCompoundPacket:
    name = 'Basic Compound Packet'
    id = 4
    state = 'play'
    bound_to = 'client'

    def __init__(self, basic_compound):
        self.basic_compound = basic_compound

    def __len__(self):
        return len(self.basic_compound)
    
    def __repr__(self):
        pass

    def write_packet(self, writer):
        pass

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Basic Compound Packet', packet.name)
        self.assertEqual(4, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_compound_with_array(self):
        packet_data = {
            'name': 'Compound with Array Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Compound',
                    'type': 'Compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Array',
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
                }
            ]
        }
        packet_src_code = '''
class Compound:
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return dl.varint_size(len(self.array)) + sum(
            (dl.string_size(item) for item in self.array)
        )
    
    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class CompoundWithArrayPacket:
    name = 'Compound with Array Packet'
    id = 0
    state = 'play'
    bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return len(self.compound)

    def __repr__(self):
        pass

    def write_packet(self, writer):
        pass

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Array Packet', packet.name)
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

    def test_compound_with_compound(self):
        packet_data = {
            'name': 'Compound with Array Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Compound',
                    'type': 'Compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Nested Compound',
                                'type': 'Compound',
                                'options': {
                                    'fields': [
                                        {
                                            'name': 'Num',
                                            'type': 'Int'
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
class NestedCompound:
    def __init__(self, num):
        self.num = num

    def __len__(self):
        return dl.int_size

    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class Compound:
    def __init__(self, nested_compound):
        self.nested_compound = nested_compound

    def __len__(self):
        return len(self.nested_compound)
    
    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class CompoundWithArrayPacket:
    name = 'Compound with Array Packet'
    id = 0
    state = 'play'
    bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return len(self.compound)

    def __repr__(self):
        pass

    def write_packet(self, writer):
        pass

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Array Packet', packet.name)
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

    def test_compound_with_option(self):
        packet_data = {
            'name': 'Compound with Option Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Compound',
                    'type': 'Compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Int Option',
                                'type': 'Option',
                                'options': {
                                    'optional': {
                                        'type': 'Int'
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
class Compound:
    def __init__(self, int_option):
        self.int_option = int_option

    def __len__(self):
        return 0 if self.int_option == None else dl.int_size
    
    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class CompoundWithOptionPacket:
    name = 'Compound with Option Packet'
    id = 0
    state = 'play'
    bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return len(self.compound)

    def __repr__(self):
        pass

    def write_packet(self, writer):
        pass

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Option Packet', packet.name)
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

    def test_compound_with_switch(self):
        packet_data = {
            'name': 'Compound with Switch Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Compound',
                    'type': 'Compound',
                    'options': {
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
                                                    'type': 'String'
                                                },
                                                {
                                                    'name': 'Field2',
                                                    'type': 'Int'
                                                }
                                            ]
                                        },
                                        {
                                            'value': 1,
                                            'fields': [
                                                {
                                                    'name': 'Field1',
                                                    'type': 'String'
                                                }
                                            ]
                                        },
                                        {
                                            'value': 2,
                                            'fields': [
                                                {
                                                    'name': 'Field2',
                                                    'type': 'Int'
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
class Compound:
    def __init__(self, switch_value, field1=None, field2=None):
        self.switch_value = switch_value
        self.field1 = field1
        self.field2 = field2

    def __len__(self):
        return (
            dl.varint_size(self.switch_value)
            + (
                dl.string_size(self.field1) + dl.int_size
                if self.switch_value == 0
                else dl.string_size(self.field1)
                if self.switch_value == 1
                else dl.int_size
                if self.switch_value == 2
                else 0
            )
        )
    
    def __repr__(self):
        pass

    def write_data(self, writer):
        pass

    @staticmethod
    def read_data(reader):
        pass

class CompoundWithSwitchPacket:
    name = 'Compound with Switch Packet'
    id = 0
    state = 'play'
    bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return len(self.compound)

    def __repr__(self):
        pass

    def write_packet(self, writer):
        pass

    @staticmethod
    def read_packet(reader):
        pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Switch Packet', packet.name)
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
