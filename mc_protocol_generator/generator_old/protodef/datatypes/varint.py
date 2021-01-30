from .base import Base

class Varint(Base):
    def generate_read_code(self, reader_name):
        return f'{self.name} = {reader_name}.read_varint()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_varint(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.varint_size(self.{self.name})'