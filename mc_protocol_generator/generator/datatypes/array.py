from .base import Base

class Array(Base):
    def __init__(self, name, count_type, element_type):
        super().__init__(name)
        self.count_type = count_type
        self.element_type = element_type

    def generate_read_code(self, reader_name, assignment=True):
        read_str = f'[{self.element_type.generate_read_code(reader_name, False)} \
                     for _ in range({self.count_type.generate_read_code(reader_name, False)}]'
        if assignment:
            read_str = f'self.{self.name} = ' + read_str
        return read_str

    def generate_write_code(self, writer_name):
        write_str = f'''{self.count_type.generate_write_code(writer_name)}
                        for value in self.{self.name}:
                            {self.element_type}.
                     '''
    
    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Array'
        name = data['name'] if 'name' in data else None
        count_type = parse_field(data['options']['count'])
        element_type = parse_field(data['options']['element'])
        return Array(name, count_type, element_type)
