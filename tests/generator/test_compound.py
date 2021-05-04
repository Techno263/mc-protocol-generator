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
                    'type': 'compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Angle Value',
                                'type': 'angle'
                            },
                            {
                                'name': 'Bool Value',
                                'type': 'bool'
                            },
                            {
                                'name': 'Byte Value',
                                'type': 'byte'
                            },
                            {
                                'name': 'Chat Value',
                                'type': 'chat'
                            },
                            {
                                'name': 'Double Value',
                                'type': 'double'
                            },
                            {
                                'name': 'Entity Metadata Value',
                                'type': 'entitymetadata'
                            },
                            {
                                'name': 'Float Value',
                                'type': 'float'
                            },
                            {
                                'name': 'Identifier Value',
                                'type': 'identifier'
                            },
                            {
                                'name': 'Int Value',
                                'type': 'int'
                            },
                            {
                                'name': 'Long Value',
                                'type': 'long'
                            },
                            {
                                'name': 'NBT Value',
                                'type': 'nbt'
                            },
                            {
                                'name': 'Position Value',
                                'type': 'position'
                            },
                            {
                                'name': 'Short Value',
                                'type': 'short'
                            },
                            {
                                'name': 'Slot Value',
                                'type': 'slot'
                            },
                            {
                                'name': 'String Value',
                                'type': 'string',
                                'options': {
                                    'max_length': 255
                                }
                            },
                            {
                                'name': 'UByte Value',
                                'type': 'ubyte'
                            },
                            {
                                'name': 'UShort Value',
                                'type': 'ushort'
                            },
                            {
                                'name': 'UUID Value',
                                'type': 'uuid'
                            },
                            {
                                'name': 'VarInt Value',
                                'type': 'varint'
                            },
                            {
                                'name': 'VarLong Value',
                                'type': 'varlong'
                            }
                        ]
                    }
                }
            ]
        }
        packet_src_code = '''
class BasicCompound:
    def __init__(self, angle_value, bool_value, byte_value,
                 chat_value, double_value, entity_metadata_value,
                 float_value, identifier_value, int_value,
                 long_value, nbt_value, position_value,
                 short_value, slot_value, string_value,
                 ubyte_value, ushort_value, uuid_value,
                 varint_value, varlong_value):
        self.angle_value = angle_value
        self.bool_value = bool_value
        self.byte_value = byte_value
        self.chat_value = chat_value
        self.double_value = double_value
        self.entity_metadata_value = entity_metadata_value
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
            dl.entity_metadata_size(self.entity_metadata_value) +
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
        return f'BasicCompound(angle_value={repr(self.angle_value)}, bool_value={repr(self.bool_value)}, byte_value={repr(self.byte_value)}, chat_value={repr(self.chat_value)}, double_value={repr(self.double_value)}, entity_metadata_value={repr(self.entity_metadata_value)}, float_value={repr(self.float_value)}, identifier_value={repr(self.identifier_value)}, int_value={repr(self.int_value)}, long_value={repr(self.long_value)}, nbt_value={repr(self.nbt_value)}, position_value={repr(self.position_value)}, short_value={repr(self.short_value)}, slot_value={repr(self.slot_value)}, string_value={repr(self.string_value)}, ubyte_value={repr(self.ubyte_value)}, ushort_value={repr(self.ushort_value)}, uuid_value={repr(self.uuid_value)}, varint_value={repr(self.varint_value)}, varlong_value={repr(self.varlong_value)})'

    def write_data(self, writer):
        writer.write_angle(self.angle_value)
        writer.write_bool(self.bool_value)
        writer.write_byte(self.byte_value)
        writer.write_chat(self.chat_value)
        writer.write_double(self.double_value)
        writer.write_entity_metadata(self.entity_metadata_value)
        writer.write_float(self.float_value)
        writer.write_identifier(self.identifier_value)
        writer.write_int(self.int_value)
        writer.write_long(self.long_value)
        writer.write_nbt(self.nbt_value)
        writer.write_position(self.position_value)
        writer.write_short(self.short_value)
        writer.write_slot(self.slot_value)
        writer.write_string(self.string_value)
        writer.write_ubyte(self.ubyte_value)
        writer.write_ushort(self.ushort_value)
        writer.write_uuid(self.uuid_value)
        writer.write_varint(self.varint_value)
        writer.write_varlong(self.varlong_value)

    @staticmethod
    def read_data(reader):
        angle_value = reader.read_angle()
        bool_value = reader.read_bool()
        byte_value = reader.read_byte()
        chat_value = reader.read_chat()
        double_value = reader.read_double()
        entity_metadata_value = reader.read_entity_metadata()
        float_value = reader.read_float()
        identifier_value = reader.read_identifier()
        int_value = reader.read_int()
        long_value = reader.read_long()
        nbt_value = reader.read_nbt()
        position_value = reader.read_position()
        short_value = reader.read_short()
        slot_value = reader.read_slot()
        string_value = reader.read_string()
        ubyte_value = reader.read_ubyte()
        ushort_value = reader.read_ushort()
        uuid_value = reader.read_uuid()
        varint_value = reader.read_varint()
        varlong_value = reader.read_varlong()
        return BasicCompound(
            angle_value,
            bool_value,
            byte_value,
            chat_value,
            double_value,
            entity_metadata_value,
            float_value,
            identifier_value,
            int_value,
            long_value,
            nbt_value,
            position_value,
            short_value,
            slot_value,
            string_value,
            ubyte_value,
            ushort_value,
            uuid_value,
            varint_value,
            varlong_value
        )

class BasicCompoundPacket:
    packet_name = 'Basic Compound Packet'
    packet_id = 4
    packet_state = 'play'
    packet_bound_to = 'client'

    def __init__(self, basic_compound):
        self.basic_compound = basic_compound

    def __len__(self):
        return (
            dl.varint_size(BasicCompoundPacket.packet_id)
            + len(self.basic_compound)
        )
    
    def __repr__(self):
        return f'BasicCompoundPacket(basic_compound={repr(self.basic_compound)})'

    def write_packet(self, writer):
        writer.write_varint(BasicCompoundPacket.packet_id)
        self.basic_compound.write_data(writer)

    @staticmethod
    def read_packet(reader):
        basic_compound = BasicCompound.read_data(reader)
        return BasicCompoundPacket(
            basic_compound
        )
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Basic Compound Packet', packet.name)
        self.assertEqual(4, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Array',
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
        return f'Compound(array={repr(self.array)})'

    def write_data(self, writer):
        writer.write_varint(len(self.array))
        for item in self.array:
            writer.write_string(item)

    @staticmethod
    def read_data(reader):
        array = [
            reader.read_string()
            for _ in range(reader.read_varint())
        ]
        return Compound(array)

class CompoundWithArrayPacket:
    packet_name = 'Compound with Array Packet'
    packet_id = 0
    packet_state = 'play'
    packet_bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return (
            dl.varint_size(CompoundWithArrayPacket.packet_id)
            + len(self.compound)
        )

    def __repr__(self):
        return f'CompoundWithArrayPacket(compound={repr(self.compound)})'

    def write_packet(self, writer):
        writer.write_varint(CompoundWithArrayPacket.packet_id)
        self.compound.write_data(writer)

    @staticmethod
    def read_packet(reader):
        compound = Compound.read_data(reader)
        return CompoundWithArrayPacket(compound)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Array Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )

    def test_compound_with_compound(self):
        packet_data = {
            'name': 'Compound with Compound Packet',
            'id': 0x00,
            'state': 'play',
            'bound_to': 'client',
            'fields': [
                {
                    'name': 'Compound',
                    'type': 'compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Nested Compound',
                                'type': 'compound',
                                'options': {
                                    'fields': [
                                        {
                                            'name': 'Num',
                                            'type': 'int'
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
        return f'NestedCompound(num={repr(self.num)})'

    def write_data(self, writer):
        writer.write_int(self.num)

    @staticmethod
    def read_data(reader):
        num = reader.read_int()
        return NestedCompound(num)

class Compound:
    def __init__(self, nested_compound):
        self.nested_compound = nested_compound

    def __len__(self):
        return len(self.nested_compound)
    
    def __repr__(self):
        return f'Compound(nested_compound={repr(self.nested_compound)})'

    def write_data(self, writer):
        self.nested_compound.write_data(writer)

    @staticmethod
    def read_data(reader):
        nested_compound = NestedCompound.read_data(reader)
        return Compound(nested_compound)

class CompoundWithCompoundPacket:
    packet_name = 'Compound with Compound Packet'
    packet_id = 0
    packet_state = 'play'
    packet_bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return (
            dl.varint_size(CompoundWithCompoundPacket.packet_id)
            + len(self.compound)
        )

    def __repr__(self):
        return f'CompoundWithCompoundPacket(compound={repr(self.compound)})'

    def write_packet(self, writer):
        writer.write_varint(CompoundWithCompoundPacket.packet_id)
        self.compound.write_data(writer)

    @staticmethod
    def read_packet(reader):
        compound = Compound.read_data(reader)
        return CompoundWithCompoundPacket(compound)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Compound Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'compound',
                    'options': {
                        'fields': [
                            {
                                'name': 'Int Option',
                                'type': 'option',
                                'options': {
                                    'optional': {
                                        'type': 'int'
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
        return (
            dl.bool_size
            + (0 if self.int_option == None else dl.int_size)
        )
    
    def __repr__(self):
        return f'Compound(int_option={repr(self.int_option)})'

    def write_data(self, writer):
        int_option_check = self.int_option != None
        writer.write_bool(int_option_check)
        if int_option_check:
            writer.write_int(self.int_option)

    @staticmethod
    def read_data(reader):
        int_option = reader.read_int() if reader.read_bool() else None
        return Compound(int_option)

class CompoundWithOptionPacket:
    packet_name = 'Compound with Option Packet'
    packet_id = 0
    packet_state = 'play'
    packet_bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return (
            dl.varint_size(CompoundWithOptionPacket.packet_id)
            + len(self.compound)
        )

    def __repr__(self):
        return f'CompoundWithOptionPacket(compound={repr(self.compound)})'

    def write_packet(self, writer):
        writer.write_varint(CompoundWithOptionPacket.packet_id)
        self.compound.write_data(writer)

    @staticmethod
    def read_packet(reader):
        compound = Compound.read_data(reader)
        return CompoundWithOptionPacket(compound)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Option Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
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
                    'type': 'compound',
                    'options': {
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
                                                    'type': 'string'
                                                },
                                                {
                                                    'name': 'Field2',
                                                    'type': 'int'
                                                }
                                            ]
                                        },
                                        {
                                            'value': 1,
                                            'fields': [
                                                {
                                                    'name': 'Field1',
                                                    'type': 'string'
                                                }
                                            ]
                                        },
                                        {
                                            'value': 2,
                                            'fields': [
                                                {
                                                    'name': 'Field2',
                                                    'type': 'int'
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
    def __init__(self, switch_value, field1, field2):
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
        return f'Compound(switch_value={repr(self.switch_value)}, field1={repr(self.field1)}, field2={repr(self.field2)})'

    def write_data(self, writer):
        writer.write_varint(self.switch_value)
        if self.switch_value == 0:
            writer.write_string(self.field1)
            writer.write_int(self.field2)
        elif self.switch_value == 1:
            writer.write_string(self.field1)
        elif self.switch_value == 2:
            writer.write_int(self.field2)

    @staticmethod
    def read_data(reader):
        switch_value = reader.read_varint()
        if switch_value == 0:
            field1 = reader.read_string()
            field2 = reader.read_int()
        elif switch_value == 1:
            field1 = reader.read_string()
            field2 = None
        elif switch_value == 2:
            field2 = reader.read_int()
            field1 = None
        return Compound(switch_value, field1, field2)

class CompoundWithSwitchPacket:
    packet_name = 'Compound with Switch Packet'
    packet_id = 0
    packet_state = 'play'
    packet_bound_to = 'client'

    def __init__(self, compound):
        self.compound = compound

    def __len__(self):
        return (
            dl.varint_size(CompoundWithSwitchPacket.packet_id)
            + len(self.compound)
        )

    def __repr__(self):
        return f'CompoundWithSwitchPacket(compound={repr(self.compound)})'

    def write_packet(self, writer):
        writer.write_varint(CompoundWithSwitchPacket.packet_id)
        self.compound.write_data(writer)

    @staticmethod
    def read_packet(reader):
        compound = Compound.read_data(reader)
        return CompoundWithSwitchPacket(compound)
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Compound with Switch Packet', packet.name)
        self.assertEqual(0, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('client', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
