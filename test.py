from mc_protocol_generator.generator.protocol_generator import load_protocol_data

if __name__ == '__main__':
    protocol = load_protocol_data('1.16.5')
    import json
    print(json.dumps(protocol, indent=4))
