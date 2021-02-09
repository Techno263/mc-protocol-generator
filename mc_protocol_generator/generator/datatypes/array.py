from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string

class Array(Base):
    def __init__(self, name, count_type, element_type):
        super().__init__(name)
        self.count_type = count_type
        self.element_type = element_type
    
    def len_str(self):
        pass

    def repr_str(self):
        pass

    def write_str(self):
        pass

    def read_str(self):
        pass

    def update_class_str(self, class_str, context):
        field_name = format_field_name(self.name)
        return replace_string(class_str,
            {
                '{{init_args}}': '%s{{init_args}}' % (field_name),
                '{{init_body}}': '%s = %s; {{init_body}}' % (field_name, field_name),
                '{{len_body}}': 'sum({' % (context.sizer_name),
            })

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Array'
        name = data['name'] if 'name' in data else None
        count_type = parse_field(data['options']['count'])
        element_type = parse_field(data['options']['element'])
        return Array(name, count_type, element_type)
