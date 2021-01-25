from mc_protocol_generator.generator.protodef.types import Protodef
import minecraft_data as mcd

if __name__ == '__main__':
    mc_data = mcd("1.16.4")
    pd = Protodef(mc_data.protocol)
    p = pd.get_type('slot', 'login.toClient')
    print(p)
    with open('pd.json', 'wt') as fp:
        import json
        json.dump(pd.protocol, fp, indent=4)
