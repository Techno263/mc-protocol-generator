from .base import Base

class Bool(Base):
    def generate_read_code(self, reader_name, assignment=True):
        if assignment:
            return f'{self.name} = {reader_name}.read_boolean()'
        else:
            return f'{reader_name}.read_boolean()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_boolean(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.boolean_size'

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Bool'
        name = data['name'] if 'name' in data else None
        return Bool(name)
