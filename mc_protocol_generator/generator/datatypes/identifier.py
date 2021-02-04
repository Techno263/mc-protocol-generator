from .base import Base

class Identifier(Base):
    def generate_read_code(self, reader_name, assignment=True):
        if assignment:
            return f'{self.name} = {reader_name}.read_identifier()'
        else:
            return f'{reader_name}.read_identifier()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_identifier(self.{self.name})'

    def generate_len_code(self, len_util_name):
        raise Exception

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Identifier'
        name = data['name'] if 'name' in data else None
        return Identifier(name)
