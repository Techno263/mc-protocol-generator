from .base import Base

class Int(Base):
    def generate_read_code(self, reader_name, assignment=True):
        if assignment:
            return f'self.{self.name} = {reader_name}.read_int()'
        return f'{reader_name}.read_int()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_int(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.int_size'

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Int'
        name = data['name'] if 'name' in data else None
        return Int(name)
