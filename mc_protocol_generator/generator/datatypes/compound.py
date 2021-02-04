from .base import Base

class Compound(Base):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields

    def generate_read_code(self, reader_name):
        return f'{self.name}.read_data({reader_name})'

    def generate_write_code(self, writer_name):
        return f'.write_data({writer_name})'

    def generate_len_code(self, len_util_name):
        return f'len()'

    def generate_util_class(self, class_name):
        init_args = []
        f'''return {class_name}:
                def __init__(self, )
         '''

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Compound'
        name = data['name'] if 'name' in data else None
        fields = [parse_field(field) for field in data['options']['fields']]
        return Compound(name, fields)
