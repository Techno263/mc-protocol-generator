
def parse_array(protodef):
    protodef['']

def parse_container():
    pass

class PacketStructure:
    
    def __init__(self, name, data):
        self.name = name
        self.data = data

    @staticmethod
    def from_protodef(name, protodef):
        datatype = protodef[0]
