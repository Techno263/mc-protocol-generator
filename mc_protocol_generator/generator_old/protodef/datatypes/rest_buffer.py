from .buffer import Buffer

class RestBuffer(Buffer):
    def generate_read_code(self, reader_name):
        return f'{self.name} = {reader_name}.read()'
