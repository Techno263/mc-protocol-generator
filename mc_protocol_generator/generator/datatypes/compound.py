from .base import Base
from mc_protocol_generator.generator.util import replace_string, format_class_name, format_field_name
from ..code_generator_context import CodeGeneratorContext

compound_class_template = '''class {{class_name}}
    def __init__(self{{init_args}}):
        {{init_body}}

    def __len__(self):
        return {{len_body}}

    def __repr__(self):
        return {{repr_body}}

    def write_data(self, {{writer_name}}):
        {{write_data_body}}

    @staticmethod
    def read_data({{reader_name}}):
        {{reader_body}}
'''

class Compound(Base):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields

    def update_class_str(self, class_str, context):
        compound_class_name = format_class_name(self.name + ' Compound')
        compound_field_names = [format_field_name(f.name) for f in self.fields]
        compound_class_str = compound_class_template
        compound_class_str = replace_string(compound_class_str,
            {
                '{{class_name}}': format_class_name(self.name),
                '{{repr_body}}': '({{repr_body}}' % (compound_class_name),
                '{{writer_name}}': writer_name,
                '{{reader_name}}': reader_name
            })
        comp_gen_ctxt = CodeGeneratorContext(context.reader_name,
            context.writer_name, context.sizer_name, 0)
        for field_index, field in enumerate(self.fields):
            comp_gen_ctxt.field_index = field_index
            len_body_str = '{{len_body}}'
            repr_body_str = '{{repr_body}}'
            if field_index != 0:
                len_body_str = ' + {{len_body}}'
                repr_body_str = ', {{repr_body}}'
            compound_class_str = replace_string(compound_class_str,
                {
                    '{{init_args}}': ', {{init_args}}',
                    '{{init_body}}': 'self.{{init_body}}',
                    '{{len_body}}': len_body_str,
                    '{{repr_body}}': repr_body_str
                })
            compound_class_str = field.update_class_str(compound_class_str, comp_gen_ctxt)
        compound_class_str = replace_string(compound_class_str,
            {
                '{{init_args}}': '',
                '{{init_body}}': '',
                '{{len_body}}': '',
                '{{repr_body}}': ')',
                '{{write_packet_body}}': '',
                '{{read_packet_body}}': f'return {compound_class_name}({compound_field_names})'
            })
        field_name = format_field_name(self.name)
        len_body_str = 'len(self.%s){{len_body}}'
        repr_body_str = '%s={self.%s}{{repr_body}}' % (field_name, field_name)
        if field_index != 0:
            len_body_str = ' + ' + len_body_str
            repr_body_str = ', ' + repr_body_str
        return replace_string(class_str,
            {
                '{{init_args}}': ', %s{{init_args}}' % (field_name),
                '{{init_body}}': 'self.%s = %s; {{init_body}}' % (field_name, field_name),
                '{{len_body}}': len_body_str,
                '{{repr_body}}': repr_body_str,
                '{{write_packet_body}}': 'self.'
            })

    @staticmethod
    def from_protocol_data(data):
        from ..packet import parse_field
        assert data['type'] == 'Compound'
        name = data['name'] if 'name' in data else None
        fields = [parse_field(field) for field in data['options']['fields']]
        return Compound(name, fields)
