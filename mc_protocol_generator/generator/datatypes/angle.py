from .base import Base

class Angle(Base):
    def generate_read_code(self, reader_name, assignment=True):
        if assignment:
            return f'self.{self.name} = {reader_name}.read_angle()'
        return f'{reader_name}.read_angle()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_angle({self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.angle_size'

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Angle'
        name = data['name'] if 'name' in data else None
        return Angle(name)
