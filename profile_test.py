from mc_protocol_generator.io import DataReader
import cProfile
import pstats

if __name__ == '__main__':
    with open(r'./tests/io/nbt/bigtest_raw.nbt', 'rb') as fp:
        reader = DataReader(fp)
        profile = cProfile.Profile()
        profile.enable()
        bigtest = reader.read_nbt()
        profile.disable()
    stats = pstats.Stats(profile)
    stats.dump_stats('read_test.prof')
