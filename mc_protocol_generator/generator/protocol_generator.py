import json
import os

def load_protocol_data(version):
    print(os.getcwd())
    print(__file__)
    with open(os.path.join(os.path.dirname(__file__), 'minecraft-protocol', f'{version}.json'), 'rt') as fp:
        return json.load(fp)
