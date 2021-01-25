from .base import Base

class Buffer(Base):
    def generate_read_code(self, reader_name):
        return f'{self.name}_len = {reader_name}.read_varint()\n'
               f'{self.name} = {reader_name}.read_byte_array({self.name}_len)'
    
    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_byte_array(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.byte_array_size(self.{self.name})'
