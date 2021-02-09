from mc_protocol_generator.generator.packet import Packet
import json

packet_str = '''
{
    "name": "Array Test",
    "id": "0x00",
    "state": "Handshaking",
    "bound_to": "Server",
    "fields": [
        {
            "name": "Array Field",
            "type": "Array",
            "options": {
                "count": {
                    "type": "VarInt"
                },
                "element": {
                    "type": "UByte"
                }
            }
        }
    ]
}
'''

target_str = '''
class ArrayTest:
    def __init__(self, array_fields):
        self.array_fields = array_fields

    @staticproperty
    def name():
        return 'Array Test'

    @staticproperty
    def packet_id():
        return 0x00

    @staticproperty
    def state():
        return 'handshaking'

    @staticproperty
    def bound_to():
        return 'server'

    def __len__(self):
        return sum(dl.int_size for _ in range(len(self.array_fields)))

    def __repr__(self):
        return f'ArrayTest(array_fields={repr(self.array_fields)})'

    def __bytes__(self):
        buffer = io.BytesIO()
        self.write_packet(buffer)
        buffer.seek(0, 0)
        return buffer.read()

    def write_packet(self, writer):
        for element in self.array_fields: writer.write_int(element);print('a');print('b')

    @staticmethod
    def read_packet(reader):
        array_fields = [reader.read_int() for _ in range(reader.read_varint())];return ArrayTest(array_fields)
'''

if __name__ == '__main__':
    from black import Mode, format_str
    black_mode = Mode(
        target_versions=set(),
        line_length=88,
        is_pyi=False,
        string_normalization=False,
        experimental_string_processing=False
    )
    print(format_str(target_str, mode=black_mode))
    array_test_data = json.loads(packet_str)
    #array_test_packet = Packet.parse_packet_data(array_test_data)
    #print(array_test_packet.get_code_str())