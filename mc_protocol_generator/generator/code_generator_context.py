class CodeGeneratorContext:
    def __init__(self, reader_name, writer_name, sizer_name, field_index):
        self.reader_name = reader_name
        self.writer_name = writer_name
        self.sizer_name = sizer_name
        self.field_index = field_index
