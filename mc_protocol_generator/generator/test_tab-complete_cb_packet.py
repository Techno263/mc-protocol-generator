class MatchesElement:
    def __init__(self, match, tooltip):
        self.match = match
        self.tooltip = tooltip

    def __len__(self):
        return dl.string_size(self.match) + \
            0 if self.tooltip == None else dl.chat_size(self.tooltip)

    def __repr__(self):
        pass

    def write_data(self, writer):
        writer.write_string(self.match)
        writer.write_bool(self.tooltip != None)
        if self.tooltip != None:
            writer.write_chat(self.tooltip)

    @staticmethod
    def read_data(reader):
        match = reader.read_string()
        if reader.read_bool():
            tooltip = reader.read_chat()
        else:
            tooltip = None
        return MatchesElement(match, tooltip)

class TabComplete:
    def __init__(self, id, start, length, matches):
        self.id = id
        self.start = start
        self.length = length
        self.matches = matches

    def __len__(self):
        return dl.varint_size(self.id) + \
            dl.varint_size(self.start) + \
            dl.varint_size(self.length) + \
            sum(len(match) for match in matches)

    def __repr__(self):
        pass

    def write_packet(self, writer):
        writer.write_varint(packet_id)
        writer.write_varint(self.id)
        writer.write_varint(self.start)
        writer.write_varint(self.length)
        for match in self.matches:
            match.write_data(writer)
        
    @staticmethod
    def read_packet(reader):
        id = reader.read_varint()
        start = reader.read_varint()
        length = reader.read_varint()
        matches = [MatchesElement.read_data(reader)
                   for _ in range(reader.read_varint())]
        return TabComplete(id, start, length, matches)
