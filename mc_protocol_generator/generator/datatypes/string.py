from .base import Base

class String(Base):
    def __init__(self, name, max_length=32767):
        super().__init__(name)
        self.max_length = max_length

    def generate_read_code(self, reader_name):
        return f'{self.name} = {reader_name}.read_string()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_string(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.string_size(self.{self.name})'

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'String'
        name = data['name'] if 'name' in data else None
        if 'options' in data:
            if 'max_length' in data['options']:
                max_length = data['options']['max_length']
            else:
                max_length = 32767
        else:
            max_length = 32767
        return String(name, max_length)
