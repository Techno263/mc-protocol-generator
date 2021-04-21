import datatype_length as dl


class Compound:
    def __init__(self, string, int):
        self.string = string
        self.int = int

    def __len__(self):
        return dl.string_size(self.string) + dl.int_size

    def __repr__(self):
        return f'Compound(string={repr(self.string)}, int={repr(self.string)})'

    def write_data(self, writer):
        writer.write_string(self.string)
        writer.write_int(self.int)

    @staticmethod
    def read_data(reader):
        string = reader.read_string()
        int = reader.read_int()
        return Compound(string, int)


class AllTypesPacket:
    name = 'All Types Packet'
    id = 1
    state = 'play'
    bound_to = 'client'

    def __init__(
        self,
        angle,
        array,
        bool,
        byte,
        chat,
        compound,
        double,
        entity_metadata,
        float,
        identifier,
        int,
        long,
        nbt,
        option,
        position,
        short,
        slot,
        string,
        switch_value,
        ubyte,
        ushort,
        uuid,
        varint,
        varlong,
        switch_short=None,
        switch_long=None,
        switch_int=None,
    ):
        self.angle = angle
        self.array = array
        self.bool = bool
        self.byte = byte
        self.chat = chat
        self.compound = compound
        self.double = double
        self.entity_metadata = entity_metadata
        self.float = float
        self.identifier = identifier
        self.int = int
        self.long = long
        self.nbt = nbt
        self.option = option
        self.position = position
        self.short = short
        self.slot = slot
        self.string = string
        self.switch_value = switch_value
        self.switch_short = switch_short
        self.switch_long = switch_long
        self.switch_int = switch_int
        self.ubyte = ubyte
        self.ushort = ushort
        self.uuid = uuid
        self.varint = varint
        self.varlong = varlong

    def __len__(self):
        return (
            dl.angle_size
            + (dl.varint_size(len(self.array)) + sum((dl.string_size(item) for item in self.array)))
            + dl.bool_size
            + dl.byte_size
            + dl.chat_size(self.chat)
            + len(self.compound)
            + dl.double_size
            + dl.entity_metadata_size(self.entity_metadata)
            + dl.float_size
            + dl.identifier_size(self.identifier)
            + dl.int_size
            + dl.long_size
            + dl.nbt_size(self.nbt)
            + (0 if self.option == None else dl.int_size)
            + dl.position_size
            + dl.short_size
            + dl.slot_size(self.slot)
            + dl.string_size(self.string)
            + dl.varint_size(self.switch_value)
            + (
                dl.short_size
                if self.switch_value == 0
                else dl.long_size + dl.int_size
                if self.switch_value == 1
                else 0
            )
            + dl.ubyte_size
            + dl.ushort_size
            + dl.uuid_size
            + dl.varint_size(self.varint)
            + dl.varlong_size(self.varlong)
        )

    def __repr__(self):
        return f'ComplexPacket(angle={repr(self.angle)}, array={repr(self.array)}, bool={repr(self.bool)}, byte={repr(self.byte)}, chat={repr(self.chat)}, compound={repr(self.compound)}, double={repr(self.double)}, entity_metadata={repr(self.entity_metadata)}, float={repr(self.float)}, identifier={repr(self.identifier)}, int={repr(self.int)}, long={repr(self.long)}, nbt={repr(self.nbt)}, option={repr(self.option)}, position={repr(self.position)}, short={repr(self.short)}, slot={repr(self.slot)}, string={repr(self.string)}, switch_value={repr(self.switch_value)}, switch_short={repr(self.switch_short)}, switch_long={repr(self.switch_long)}, switch_int={repr(self.switch_int)}, ubyte={repr(self.ubyte)}, ushort={repr(self.ushort)}, uuid={repr(self.uuid)}, varint={repr(self.varint)}, varlong={repr(self.varlong)})'

    def write_packet(self, writer):
        writer.write_varint(AllTypesPacket.id)
        writer.write_angle(self.angle)
        writer.write_varint(len(self.array))
        for item in self.array:
            writer.write_string(item)
        writer.write_bool(self.bool)
        writer.write_byte(self.byte)
        writer.write_chat(self.chat)
        self.compound.write_data(writer)
        writer.write_double(self.double)
        writer.write_entity_metadata(self.entity_metadata)
        writer.write_float(self.float)
        writer.write_identifier(self.identifier)
        writer.write_int(self.int)
        writer.write_long(self.long)
        writer.write_nbt(self.nbt)
        writer.write_position(self.position)
        writer.write_short(self.short)
        writer.write_slot(self.slot)
        writer.write_string(self.string)
        writer.write_varint(self.switch_value)
        if self.switch_value == 0:
            writer.write_short(self.switch_short)
        elif self.switch_value == 1:
            writer.write_long(self.switch_long)
            writer.write_int(self.switch_int)
        writer.write_ubyte(self.ubyte)
        writer.write_ushort(self.ushort)
        writer.write_uuid(self.uuid)
        writer.write_varint(self.varint)
        writer.write_varlong(self.varlong)

    @staticmethod
    def read_packet(reader):
        angle = reader.read_angle()
        array = [reader.read_string() for _ in range(reader.read_varint())]
        bool = reader.read_bool()
        byte = reader.read_byte()
        chat = reader.read_chat()
        compound = Compound.read_data(reader)
        double = reader.read_double()
        entity_metadata = reader.read_entity_metadata()
        float = reader.read_float()
        identifier = reader.read_identifier()
        int = reader.read_int()
        long = reader.read_long()
        nbt = reader.read_nbt()
        option = reader.read_int() if reader.read_bool() else None
        position = reader.read_position()
        short = reader.read_short()
        slot = reader.read_slot()
        string = reader.read_string()
        switch_value = reader.read_varint()
        if switch_value == 0:
            _switch_values = {'switch_short': reader.read_short()}
        elif switch_value == 1:
            _switch_values = {'switch_long': reader.read_long(), 'switch_int': reader.read_int()}
        ubyte = reader.read_ubyte()
        ushort = reader.read_ushort()
        uuid = reader.read_uuid()
        varint = reader.read_varint()
        varlong = reader.read_varlong()
        return AllTypesPacket(
            angle=angle,
            array=array,
            bool=bool,
            byte=byte,
            chat=chat,
            compound=compound,
            double=double,
            entity_metadata=entity_metadata,
            float=float,
            identifier=identifier,
            int=int,
            long=long,
            nbt=nbt,
            option=option,
            position=position,
            short=short,
            slot=slot,
            string=string,
            switch_value=switch_value,
            ubyte=ubyte,
            ushort=ushort,
            uuid=uuid,
            varint=varint,
            varlong=varlong,
            **_switch_values,
        )
