from .base import Base

class Chat(Base):
    def generate_read_code(self, reader_name, assignment=True):
        if assignment:
            return f'{self.name} = {reader_name}.read_chat()'
        else:
            return f'{reader_name}.read_chat()'

    def generate_write_code(self, writer_name):
        return f'{writer_name}.write_chat(self.{self.name})'

    def generate_len_code(self, len_util_name):
        raise Exception

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Chat'
        name = data['name'] if 'name' in data else None
        return Chat(name)
