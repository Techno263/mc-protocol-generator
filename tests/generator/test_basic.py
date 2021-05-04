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
        packet_src_code = '''
            class BasicPacket:
                packet_name = 'Basic Packet'
                packet_id = 255
                packet_state = 'play'
                packet_bound_to = 'server'

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
                        dl.varint_size(BasicPacket.packet_id) +
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
                    writer.write_varint(BasicPacket.packet_id)
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
                def read_packet(reader):
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
                    return BasicPacket(
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
        '''
        packet = Packet.parse_packet_data(packet_data)
        self.assertEqual('Basic Packet', packet.name)
        self.assertEqual(255, packet.id)
        self.assertEqual('play', packet.state)
        self.assertEqual('server', packet.bound_to)
        generated_src_code = packet.get_packet_code()
        exec(generated_src_code)
        self.assertEqual(
            format_str(packet_src_code, mode=black_mode),
            generated_src_code
        )
