from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name):
        self.name = name

    def imports(self):
        return ''

    def len_str(self, sizer_name):
        return ''

    def repr_str(self):
        return ''

    def write_str(self, writer_name):
        return ''

    def read_str(self, reader_name):
        return ''

    @abstractmethod
    def update_class_str(self, class_str, context):
        pass

    @staticmethod
    @abstractmethod
    def from_protocol_data(data):
        pass
