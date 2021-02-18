class SimplePacket:
    name = 'Simple Packet'
    id = 0
    state = 'play'
    bound_to = 'server'

    def __init__(self, int1, str1, varint1):
        self.int1 = int1
        self.str1 = str1
        self.varint1 = varint1

    def __len__(self):
        return dl.int_size + dl.string_size(self.str1) + dl.varint_size(self.varint1)

    def __repr__(self):
        return f'SimplePacket(int1={repr(self.int1)}, str1={repr(self.str1)}, varint1={repr(self.varint1)})'

    def write_packet(self, writer):
        writer.write_varint(self.id)
        writer.write_int(self.int1)
        writer.write_string(self.str1)
        writer.write_varint(self.varint1)

    @staticmethod
    def read_packet(reader):
        int1 = reader.read_int()
        str1 = reader.read_string()
        varint1 = reader.read_varint()
        return SimplePacket(int1, str1, varint1)
