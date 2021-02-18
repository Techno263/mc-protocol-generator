import datatype_length as dl

class ArrayCompItem:
    def __init__(self, string, int_val):
        self.string = string
        self.int_val = int_val

    def __len__(self):
        return (
            dl.string_size(self.string) +
            dl.int_size
        )
    
    def __repr__(self):
        return f'ArrayCompItem(string={repr(self.string)}, int_val={repr(self.int_val)})'

    def write_data(self, writer):
        writer.write_string(self.string)
        writer.write_int(self.int_val)
    
    @staticmethod
    def read_data(reader):
        string = reader.read_string()
        int_val = reader.read_int()
        return ArrayCompItem(string, int_val)

class CompoundVar:
    def __init__(self, string, varlong, short):
        self.string = string
        self.varlong = varlong
        self.short = short
    
    def __len__(self):
        return (
            dl.string_size(self.string) +
            dl.varlong(self.varlong) +
            dl.short_size
        )

    def write_data(self, writer):
        writer.write_string(self.string)
        writer.write_varlong(self.varlong)
        writer.write_short(self.short)

    @staticmethod
    def read_data(reader):
        string = reader.read_string()
        varlong = reader.read_varlong()
        short = reader.read_short()
        return CompoundVar(string, varlong, short)

class ComplexPacket:
    name = 'Complex Packet'
    id = 0x01
    state = 'play'
    bound_to = 'server'

    def __init__(self, array_comp, array_int, array_varint, compound_var):
        self.array_comp = array_comp
        self.array_int = array_int
        self.array_varint = array_varint
        self.compound_var = compound_var

    def __len__(self):
        return (
            sum(len(item) for item in self.array_comp) +
            sum(dl.int_size for item in self.array_int) +
            sum(dl.varint_size(item) for item in self.array_varint) +
            len(self.compound_var)
        )

    def __repr__(self):
        return f'ComplexPacket(array_comp={repr(self.array_comp)}, array_int={repr(self.array_int)}, array_varint={repr(self.array_varint)}, compound={repr(self.compound)})'

    def write_packet(self, writer):
        for item in self.array_comp:
            item.write_data(writer)
        for item in self.array_int:
            writer.write_int(item)
        for item in self.array_varint:
            writer.write_varint(item)
        self.compound_var.write_data(writer)

    @staticmethod
    def read_packet(reader):
        array_comp = [ArrayCompItem.read_data(reader)
                      for _ in range(reader.read_varint())]
        array_int = [reader.read_int()
                     for _ in range(reader.read_varint())]
        array_varint = [reader.read_varint()
                        for _ in range(reader.read_varint())]
        compound_var = CompoundVar.read_data(reader)
        return ComplexPacket(array_comp, array_int, array_varint, compound_var)
