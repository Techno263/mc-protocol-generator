from .base import Base

class NBT(Base):
    def generate_read_code(self, reader_name):
        return f'{self.name} = {reader_name}.read_nbt()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_nbt(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.nbt_size(self.{self.name})'
