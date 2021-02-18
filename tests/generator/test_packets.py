import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str, Mode

'''
Test Cases:
    Basic types (int, short, byte)
    Dynamic types (string, chat, varint)
    Array of basic types
    Array of dynamic types
    Compound (with basic and dynamic types)
    Array of Compounds (Compound has option type)
    Optional basic type
    Optional dynamic type
    Switch with dynamic and basic types
'''

black_mode = Mode(
    target_versions=set(),
    line_length=79,
    is_pyi=False,
    string_normalization=False,
    experimental_string_processing=False
)

class TestPackets(unittest.TestCase):
    def test_basic_packet(self):
        packet_data = {
            'name': 'Basic Packet',
            'id': 0xff,
            'state': 'play',
            'bound_to': 'server',
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
        packet_src_code = '''
            class BasicPacket:
                name = 'Basic Packet'
                id = 255
                state = 'play'
                bound_to = 'server'

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

                def write_packet(self, writer):
                    pass

                @staticmethod
                def read_packet(reader):
                    pass
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Basic Packet', packet.name)
        self.assertEqual(255, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

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
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

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
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

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
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_switch(self):
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
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

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
                            'type': 'VarInt'
                        }
                    }
                }
            ]
        }
        packet_src_code = '''

        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Array Option Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        generated_src_code = format_str(generated_src_code, mode=black_mode)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
