from .base import Base
from mc_protocol_generator.generator.util import format_field_name, replace_string

class String(Base):
    def __init__(self, name, max_length=32767):
        super().__init__(name)
        self.max_length = max_length

    def len_str(self, sizer_name):
        field_name = format_field_name(self.name)
        return '%s.string_size(self.%s){{len_body}}' % (sizer_name, field_name)

    def repr_str(self):
        field_name = format_field_name(self.name)
        return '%s={self.%s}{{repr_body}}' % (field_name, field_name)

    def write_str(self, writer_name):
        field_name = format_field_name(self.name)
        return '%s.write_string(self.%s); {{write_packet_body}}' % (writer_name, field_name)

    def read_str(self. reader_name):
        field_name = format_field_name(self.name)
        return '%s = %s.read_string(); {{read_packet_body}}' % (field_name, reader_name)

    def update_class_str(self, class_str, context):
        field_name = format_field_name(self.name)
        return replace_string(class_str,
            {
                '{{init_args}}': '%s{{init_args}}' % (field_name),
                '{{init_body}}': '%s = %s;{{init_body}}' % (field_name, field_name),
                '{{len_body}}': self.len_str(context.sizer_name),
                '{{repr_body}}': self.repr_str(),
                '{{write_packet_body}}': self.write_str(context.writer_name),
                '{{read_packet_body}}': self.read_str(context.reader_name)
            })

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'String'
        name = data['name'] if 'name' in data else None
        if 'options' in data:
            if 'max_length' in data['options']:
                max_length = data['options']['max_length']
            else:
                max_length = 32767
        else:
            max_length = 32767
        return String(name, max_length)
