import json
import os

def format_label(label):
    if label != None:
        return label.lower().replace(' ', '_')

def build_packet(packet_data):
    pass

def preprocess_packet_data(protocol_data):
    for packet in protocol_data:
        packet['name'] = format_label(packet['name'])
        packet['id'] = int(packet['id'], 16)
        packet['state'] = format_label(packet['state'])
        packet['bound_to'] = format_label(packet['bound_to'])
        for field in packet['fields']:
            field['name'] = format_label(field['name'])
            field['type']['type'] = format_label(field['type']['type'])
    #output_data []

def load_protocol_data(version):
    file_path = os.path.join(os.path.dirname(__file__), 'minecraft-protocol', f'{version}.json')
    with open(file_path, 'rt', encoding='utf8') as fp:
        protocol_data = json.load(fp)
        preprocess_packet_data(protocol_data)
        return protocol_data

def generate_init_args(fields):
    return ', '.join(field['name'] for field in fields if field['name'] != None)

def generate_reader_code(field, reader_name):
    if field['type'] == 'bool':
        return f'{reader_name}.read_bool()'
    elif field['type'] == 'byte':
        pass

def generate_init_body(fields):
    pass

def generate_packet(packet_data):
    pass
