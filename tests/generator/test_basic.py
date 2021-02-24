import unittest
from mc_protocol_generator.generator.packet import Packet
from black import format_str

from .util import black_mode

class TestBasic(unittest.TestCase):
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
                    'name': 'Entity Metadata Value',
                    'type': 'EntityMetadata'
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
                    return f'BasicPacket(angle_value={repr(self.angle_value)}, bool_value={repr(self.bool_value)}, byte_value={repr(self.byte_value)}, chat_value={repr(self.chat_value)}, double_value={repr(self.double_value)}, entity_metadata_value={repr(self.entity_metadata_value)}, float_value={repr(self.float_value)}, identifier_value={repr(self.identifier_value)}, int_value={repr(self.int_value)}, long_value={repr(self.long_value)}, nbt_value={repr(self.nbt_value)}, position_value={repr(self.position_value)}, short_value={repr(self.short_value)}, slot_value={repr(self.slot_value)}, string_value={repr(self.string_value)}, ubyte_value={repr(self.ubyte_value)}, ushort_value={repr(self.ushort_value)}, uuid_value={repr(self.uuid_value)}, varint_value={repr(self.varint_value)}, varlong_value={repr(self.varlong_value)})'

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
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
