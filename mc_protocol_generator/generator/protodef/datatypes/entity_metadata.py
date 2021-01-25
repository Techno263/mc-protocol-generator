from .base import Base

class EntityMetadata(Base):
    def generate_read_code(self, reader_name):
        return f'{self.name} = {reader_name}.read_entity_metadata()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_entity_metadata(self.{self.name})'

    def generate_len_code(self, len_util_name):
        return f'{len_util_name}.entity_metadata_size(self.{self.name})'
