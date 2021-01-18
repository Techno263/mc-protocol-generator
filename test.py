from mc_protocol_generator.io import DataWriter
import mc_protocol_generator.io.nbt.tag as nbttag
import timeit
import numbers
import io
import cProfile
import pstats

def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = pstats.SortKey.CUMULATIVE  # 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return wrapper

@profile
def get_keys(compound):
    return list(c.keys())

@profile
def get_values(compound):
    return list(c.values())

@profile
def get_items(compound):
    return list(c.items())

@profile
def get_bytes(tag):
    return bytes(tag)

@profile
def get_write(tag, writer):
    tag.write(writer)

if __name__ == '__main__':
    c = nbttag.CompoundTag('compound', [
            nbttag.IntTag('value1', 1), 
            nbttag.IntTag('value2', 2)
        ])
    c = nbttag.CompoundTag(
        'compound',
        [nbttag.IntTag(f'value{i}', i) for i in range(1000)]
    )
    print('keys')
    get_keys(c)
    print('values')
    get_values(c)
    print('items')
    get_items(c)
    print('bytes')
    get_bytes(c)
    print('writer')
    w = DataWriter(io.BytesIO())
    get_write(c, w)
