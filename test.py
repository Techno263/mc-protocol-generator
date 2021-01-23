import minecraft_data as mcd
import json

if __name__ == '__main__':
    with open('protocol_data.json', 'wt') as fp:
        mc_data = mcd("1.16.4")
        json.dump(mc_data.protocol, fp)
