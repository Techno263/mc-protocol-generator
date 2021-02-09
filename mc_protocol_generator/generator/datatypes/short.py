from .base import Base

class Short(Base):
    def len_str(self, sizer_name):
        return '%s.short_size{{len_body}}' % (sizer_name)

    def repr_str(self):
        field_name = format_field_name(self.name)
        return '%s={self.%s}{{repr_body}}' % (field_name, field_name)

    def write_str(self, writer_name):
        field_name = format_field_name(self.name)
        return '%s.write_short(self.%s); {{write_packet_body}}' % (writer_name, field_name)

    def read_str(self, reader_name):
        field_name = format_field_name(self.name)
        return '%s = %s.read_short(); {{read_packet_body}}' % (field_name, reader_name)

    def update_class_str(self, class_str, context):
        field_name = format_field_name(self.name)
        return replace_string(class_str,
            {
                '{{init_args}}': '%s{{init_args}}' % (field_name),
                '{{init_body}}': '%s = %s; {{init_body}}' % (field_name, field_name),
                '{{len_body}}': self.len_str(context.sizer_name),
                '{{repr_body}}': self.repr_str(),
                '{{write_packet_body}}': self.write_str(context.writer_name),
                '{{read_packet_body}}': self.read_str(context.reader_name)
            })

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'Short'
        name = data['name'] if 'name' in data else None
        return Short(name)
