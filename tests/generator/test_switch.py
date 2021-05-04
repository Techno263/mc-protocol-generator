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
                    'type': 'varint'
                },
                {
                    'type': 'switch',
                    'options': {
                        'switch': {
                            'field': 'Switch Value'
                        },
                        'cases': [
                            {
                                'value': 0,
                                'fields': [
                                    {
                                        'name': 'Field1',
                                        'type': 'varint'
                                    },
                                    {
                                        'name': 'Field2',
                                        'type': 'ubyte'
                                    },
                                    {
                                        'name': 'Field3',
                                        'type': 'short'
                                    }
                                ]
                            },
                            {
                                'value': 1,
                                'fields': [
                                    {
                                        'name': 'Field4',
                                        'type': 'string'
                                    }
                                ]
                            },
                            {
                                'value': 2,
                                'fields': []
                            }
                        ]
                    }
                },
                {
                    'name': 'field5',
                    'type': 'varint'
                }
            ]
        }
        packet_src_code = '''
class SwitchPacket:
    packet_name = 'Switch Packet'
    packet_id = 17
    packet_state = 'play'
    packet_bound_to = 'server'

    def __init__(self, switch_value, field1, field2, field3, field4, field5):
        self.switch_value = switch_value
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4
        self.field5 = field5

    def __len__(self):
        return (
            dl.varint_size(SwitchPacket.packet_id)
            + dl.varint_size(self.switch_value) + (
                dl.varint_size(self.field1) + dl.ubyte_size + dl.short_size if self.switch_value == 0 else 
                dl.string_size(self.field4) if self.switch_value == 1 else
                0 if self.switch_value == 2 else 0
            )
            + dl.varint_size(self.field5)
        )
    
    def __repr__(self):
        return f'SwitchPacket(switch_value={repr(self.switch_value)}, field1={repr(self.field1)}, field2={repr(self.field2)}, field3={repr(self.field3)}, field4={repr(self.field4)}, field5={repr(self.field5)})'

    def write_packet(self, writer):
        writer.write_varint(SwitchPacket.packet_id)
        writer.write_varint(self.switch_value)
        if self.switch_value == 0:
            writer.write_varint(self.field1)
            writer.write_ubyte(self.field2)
            writer.write_short(self.field3)
        elif self.switch_value == 1:
            writer.write_string(self.field4)
        elif self.switch_value == 2:
            pass
        writer.write_varint(self.field5)

    @staticmethod
    def read_packet(reader):
        switch_value = reader.read_varint()
        if switch_value == 0:
            field1 = reader.read_varint()
            field2 = reader.read_ubyte()
            field3 = reader.read_short()
            field4 = None
        elif switch_value == 1:
            field4 = reader.read_string()
            field1 = None
            field2 = None
            field3 = None
        elif switch_value == 2:
            field1 = None
            field2 = None
            field3 = None
            field4 = None
        field5 = reader.read_varint()
        return SwitchPacket(
            switch_value, field1, field2, field3, field4, field5
        )
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Switch Packet', packet.name)
        self.assertEqual(17, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_array_switch(self):
        packet_data = {
            'name': 'Switch Packet',
            'id': 0x11,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    "name": "Switch Value",
                    "type": "varint"
                },
                {
                    'type': 'switch',
                    'options': {
                        'switch': {
                            'field': "Switch Value"
                        },
                        'cases': [
                            {
                                'value': 0,
                                'fields': [
                                    {
                                        'name': 'Array1',
                                        'type': 'array',
                                        'options': {
                                            'count': {
                                                'type': 'varint'
                                            },
                                            'element': {
                                                'type': 'string'
                                            }
                                        }
                                    },
                                    {
                                        'name': 'Array2',
                                        'type': 'array',
                                        'options': {
                                            'count': {
                                                'type': 'int'
                                            },
                                            'element': {
                                                'type': 'short'
                                            }
                                        }
                                    },
                                    {
                                        'name': 'Field1',
                                        'type': 'short'
                                    }
                                ]
                            },
                            {
                                'value': 1,
                                'fields': [
                                    {
                                        'name': 'Array3',
                                        'type': 'array',
                                        'options': {
                                            'count': {
                                                'type': 'ushort'
                                            },
                                            'element': {
                                                'type': 'chat'
                                            }
                                        }
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
    packet_name = 'Switch Packet'
    packet_id = 17
    packet_state = 'play'
    packet_bound_to = 'server'

    def __init__(self, switch_value, array1, array2, field1, array3):
        self.switch_value = switch_value
        self.array1 = array1
        self.array2 = array2
        self.field1 = field1
        self.array3 = array3

    def __len__(self):
        return (
            dl.varint_size(SwitchPacket.packet_id)
            + dl.varint_size(self.switch_value) + (
                dl.varint_size(len(self.array1)) 
                + sum((dl.string_size(item) for item in self.array1))
                + (dl.int_size + sum((dl.short_size for item in self.array2)))
                + dl.short_size
                if self.switch_value == 0
                else dl.ushort_size
                + sum((dl.chat_size(item) for item in self.array3))
                if self.switch_value == 1 
                else 0
                if self.switch_value == 2
                else 0
            )
        )
    
    def __repr__(self):
        return f'SwitchPacket(switch_value={repr(self.switch_value)}, array1={repr(self.array1)}, array2={repr(self.array2)}, field1={repr(self.field1)}, array3={repr(self.array3)})'

    def write_packet(self, writer):
        writer.write_varint(SwitchPacket.packet_id)
        writer.write_varint(self.switch_value)
        if self.switch_value == 0:
            writer.write_varint(len(self.array1))
            for item in self.array1:
                writer.write_string(item)
            writer.write_int(len(self.array2))
            for item in self.array2:
                writer.write_short(item)
            writer.write_short(self.field1)
        elif self.switch_value == 1:
            writer.write_ushort(len(self.array3))
            for item in self.array3:
                writer.write_chat(item)
        elif self.switch_value == 2:
            pass

    @staticmethod
    def read_packet(reader):
        switch_value = reader.read_varint()
        if switch_value == 0:
            array1 = [reader.read_string() for _ in range(reader.read_varint())]
            array2 = [reader.read_short() for _ in range(reader.read_int())]
            field1 = reader.read_short()
            array3 = None
        elif switch_value == 1:
            array3 = [reader.read_chat() for _ in range(reader.read_ushort())]
            array1 = None
            array2 = None
            field1 = None
        elif switch_value == 2:
            array1 = None
            array2 = None
            field1 = None
            array3 = None
        return SwitchPacket(switch_value, array1, array2, field1, array3)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Switch Packet', packet.name)
        self.assertEqual(17, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_compound_switch(self):
        packet_data = {
            'name': 'Switch Packet',
            'id': 0x11,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'Switch Value',
                    'type': 'varint'
                },
                {
                    'type': 'switch',
                    'options': {
                        'switch': {
                            'field': 'Switch Value'
                        },
                        'cases': [
                            {
                                'value': 0,
                                'fields': [
                                    {
                                        'name': 'Field1',
                                        'type': 'compound',
                                        'options': {
                                            'fields': [
                                                {
                                                    'name': 'Field1',
                                                    'type': 'int'
                                                },
                                                {
                                                    'name': 'Field2',
                                                    'type': 'string'
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        'name': 'Field2',
                                        'type': 'compound',
                                        'options': {
                                            'fields': [
                                                {
                                                    'name': 'Field1',
                                                    'type': 'int'
                                                },
                                                {
                                                    'name': 'Field2',
                                                    'type': 'string'
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        'name': 'Field3',
                                        'type': 'short'
                                    }
                                ]
                            },
                            {
                                'value': 1,
                                'fields': [
                                    {
                                        'name': 'Field4',
                                        'type': 'compound',
                                        'options': {
                                            'fields': [
                                                {
                                                    'name': 'Field1',
                                                    'type': 'int'
                                                },
                                                {
                                                    'name': 'Field2',
                                                    'type': 'string'
                                                }
                                            ]
                                        }
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
class Field1:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __len__(self):
        return dl.int_size + dl.string_size(self.field2)

    def __repr__(self):
        return f'Field1(field1={repr(self.field1)}, field2={repr(self.field2)})'

    def write_data(self, writer):
        writer.write_int(self.field1)
        writer.write_string(self.field2)

    @staticmethod
    def read_data(reader):
        field1 = reader.read_int()
        field2 = reader.read_string()
        return Field1(field1, field2)

class Field2:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __len__(self):
        return dl.int_size + dl.string_size(self.field2)

    def __repr__(self):
        return f'Field2(field1={repr(self.field1)}, field2={repr(self.field2)})'

    def write_data(self, writer):
        writer.write_int(self.field1)
        writer.write_string(self.field2)

    @staticmethod
    def read_data(reader):
        field1 = reader.read_int()
        field2 = reader.read_string()
        return Field2(field1, field2)

class Field4:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __len__(self):
        return dl.int_size + dl.string_size(self.field2)

    def __repr__(self):
        return f'Field4(field1={repr(self.field1)}, field2={repr(self.field2)})'

    def write_data(self, writer):
        writer.write_int(self.field1)
        writer.write_string(self.field2)

    @staticmethod
    def read_data(reader):
        field1 = reader.read_int()
        field2 = reader.read_string()
        return Field4(field1, field2)

class SwitchPacket:
    packet_name = 'Switch Packet'
    packet_id = 17
    packet_state = 'play'
    packet_bound_to = 'server'

    def __init__(self, switch_value, field1, field2, field3, field4):
        self.switch_value = switch_value
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4

    def __len__(self):
        return (
            dl.varint_size(SwitchPacket.packet_id)
            + dl.varint_size(self.switch_value) + (
                len(self.field1) + len(self.field2) + dl.short_size
                if self.switch_value == 0
                else len(self.field4)
                if self.switch_value == 1
                else 0
                if self.switch_value == 2
                else 0
            )
        )
    
    def __repr__(self):
        return f'SwitchPacket(switch_value={repr(self.switch_value)}, field1={repr(self.field1)}, field2={repr(self.field2)}, field3={repr(self.field3)}, field4={repr(self.field4)})'

    def write_packet(self, writer):
        writer.write_varint(SwitchPacket.packet_id)
        writer.write_varint(self.switch_value)
        if self.switch_value == 0:
            self.field1.write_data(writer)
            self.field2.write_data(writer)
            writer.write_short(self.field3)
        elif self.switch_value == 1:
            self.field4.write_data(writer)
        elif self.switch_value == 2:
            pass

    @staticmethod
    def read_packet(reader):
        switch_value = reader.read_varint()
        if switch_value == 0:
            field1 = Field1.read_data(reader)
            field2 = Field2.read_data(reader)
            field3 = reader.read_short()
            field4 = None
        elif switch_value == 1:
            field4 = Field4.read_data(reader)
            field1 = None
            field2 = None
            field3 = None
        elif switch_value == 2:
            field1 = None
            field2 = None
            field3 = None
            field4 = None
        return SwitchPacket(switch_value, field1, field2, field3, field4)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Switch Packet', packet.name)
        self.assertEqual(17, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_option_switch(self):
        packet_data = {
            'name': 'Switch Packet',
            'id': 0x11,
            'state': 'play',
            'bound_to': 'server',
            'fields': [
                {
                    'name': 'Switch Value',
                    'type': 'varint'
                },
                {
                    'type': 'switch',
                    'options': {
                        'switch': {
                            'field': 'Switch Value'
                        },
                        'cases': [
                            {
                                'value': 0,
                                'fields': [
                                    {
                                        'name': 'Field1',
                                        'type': 'option',
                                        'options': {
                                            'optional': {
                                                'type': 'varint'
                                            }
                                        }
                                    },
                                    {
                                        'name': 'Field2',
                                        'type': 'option',
                                        'options': {
                                            'optional': {
                                                'type': 'ubyte'
                                            }
                                        }
                                    },
                                    {
                                        'name': 'Field3',
                                        'type': 'option',
                                        'options': {
                                            'optional': {
                                                'type': 'short'
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                'value': 1,
                                'fields': [
                                    {
                                        'name': 'Field4',
                                        'type': 'option',
                                        'options': {
                                            'optional': {
                                                'type': 'string'
                                            }
                                        }
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
    packet_name = 'Switch Packet'
    packet_id = 17
    packet_state = 'play'
    packet_bound_to = 'server'

    def __init__(self, switch_value, field1, field2, field3, field4):
        self.switch_value = switch_value
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4

    def __len__(self):
        return (
            dl.varint_size(SwitchPacket.packet_id)
            + dl.varint_size(self.switch_value) + (
                dl.bool_size
                + (0 if self.field1 == None else dl.varint_size(self.field1))
                + (
                    dl.bool_size
                    + (0 if self.field2 == None else dl.ubyte_size)
                )
                + (
                    dl.bool_size
                    + (0 if self.field3 == None else dl.short_size)
                )
                if self.switch_value == 0
                else dl.bool_size + (0 if self.field4 == None else dl.string_size(self.field4))
                if self.switch_value == 1
                else 0
                if self.switch_value == 2
                else 0
            )
        )
    
    def __repr__(self):
        return f'SwitchPacket(switch_value={repr(self.switch_value)}, field1={repr(self.field1)}, field2={repr(self.field2)}, field3={repr(self.field3)}, field4={repr(self.field4)})'

    def write_packet(self, writer):
        writer.write_varint(SwitchPacket.packet_id)
        writer.write_varint(self.switch_value)
        if self.switch_value == 0:
            field1_check = self.field1 != None
            writer.write_bool(field1_check)
            if field1_check:
                writer.write_varint(self.field1)
            field2_check = self.field2 != None
            writer.write_bool(field2_check)
            if field2_check:
                writer.write_ubyte(self.field2)
            field3_check = self.field3 != None
            writer.write_bool(field3_check)
            if field3_check:
                writer.write_short(self.field3)
        elif self.switch_value == 1:
            field4_check = self.field4 != None
            writer.write_bool(field4_check)
            if field4_check:
                writer.write_string(self.field4)
        elif self.switch_value == 2:
            pass

    @staticmethod
    def read_packet(reader):
        switch_value = reader.read_varint()
        if switch_value == 0:
            field1 = reader.read_varint() if reader.read_bool() else None
            field2 = reader.read_ubyte() if reader.read_bool() else None
            field3 = reader.read_short() if reader.read_bool() else None
            field4 = None
        elif switch_value == 1:
            field4 = reader.read_string() if reader.read_bool() else None
            field1 = None
            field2 = None
            field3 = None
        elif switch_value == 2:
            field1 = None
            field2 = None
            field3 = None
            field4 = None
        return SwitchPacket(switch_value, field1, field2, field3, field4)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Switch Packet', packet.name)
        self.assertEqual(17, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
