import json

class Packet:
    def __init__(self, name, id, state, bound_to, fields):
        self.name = name
        self.id = id
        self.state = state
        self.bound_to = bound_to
        self.fields = fields

    def __repr__(self):
        return f'Packet(name={repr(self.name)}, id={repr(self.id)}, ' \
            f'bound_to={repr(self.bound_to)}, fields={repr(self.fields)})'

class PacketJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Packet):
            return {
                'name': o.name,
                'id': o.id,
                'state': o.state,
                'bound_to': o.bound_to,
                'fields': o.fields
            }
        return super(PacketJSONEncoder, self).default(o)

class PacketJSONDecoder(json.JSONDecoder):
    _fields = {'name', 'id', 'state', 'bound_to', 'fields'}

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if all(f in obj for f in self._fields):
            return Packet(obj['name'], obj['id'], obj['state'], obj['bound_to'], obj['fields'])
        return obj

if __name__ == '__main__':
    packet = Packet('p1', '0x00', 'play', 'clientbound', [{'name':'field1','type':'varint'},{'name':'field2','type':'varint'}])
    json_output = json.dumps(packet, cls=PacketJSONEncoder)
    packet2 = json.loads(json_output, cls=PacketJSONDecoder)
    print(packet)
    print(json_output)
    print(packet2)
    print(json.dumps({'str':'hello'}, cls=PacketJSONEncoder))
