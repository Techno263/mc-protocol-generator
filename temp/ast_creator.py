import ast
import os
from black import Mode, format_str

def create_ast_dump_file(filename):
    current_dir = os.path.dirname(__file__)
    simple_packet_filename = os.path.join(current_dir, filename)
    with open(simple_packet_filename, 'rt') as fp:
        src_code = fp.read()
    node = ast.parse(src_code)
    black_mode = Mode(
        target_versions=set(),
        line_length=100,
        is_pyi=False,
        string_normalization=False,
        experimental_string_processing=False
    )
    filename = filename.replace('.py', '')
    with open(os.path.join(current_dir, f'{filename}_ast_dump.py'), 'wt') as fp:
        fp.write(format_str(ast.dump(node), mode=black_mode))
    with open(os.path.join(current_dir, f'{filename}_generated.py'), 'wt') as fp:
        fp.write(format_str(ast.unparse(node), mode=black_mode))

if __name__ == '__main__':
    create_ast_dump_file('simple_packet.py')
    create_ast_dump_file('complex_packet.py')
    create_ast_dump_file('all_types_packet.py')
