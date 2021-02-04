from .base import Base

class Short(Base):
    def generate_read_code(self, reader_name):
        return f'{self.name} = {reader_name}.read_short()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_short(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.short_size'

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Short'
        name = data['name'] if 'name' in data else None
        return Short(name)
