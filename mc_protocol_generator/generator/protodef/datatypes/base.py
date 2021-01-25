from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name):
        self.name = name

    def generate_init_code(self):
        return f'self.{self.name} = {self.name}'

    @abstractmethod
    def generate_read_code(self, reader_name):
        pass

    @abstractmethod
    def generate_write_code(self, writer_name):
        pass

    @abstractmethod
    def generate_len_code(self, len_util_name):
        pass