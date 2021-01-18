import unittest
import mc_protocol_generator.io.nbt.tag as nbttag
from mc_protocol_generator.io import DataReader
import os.path as path

class TestParseNBT(unittest.TestCase):
    def test_bigtest(self):
        filepath = path.join(path.dirname(__file__), 'bigtest_raw.nbt')
        with open(filepath, 'rb') as fp:
            reader = DataReader(fp)
            bigtest = reader.read_nbt()
        self.assertIsInstance(bigtest, nbttag.CompoundTag)
        self.assertEqual('Level', bigtest.name)
        self.assertEqual(11, len(bigtest))
        nested_compound = bigtest['nested compound test']
        self.assertIsInstance(nested_compound, nbttag.CompoundTag)
        self.assertEqual(2, len(nested_compound))
        egg = nested_compound['egg']
        self.assertIsInstance(egg, nbttag.CompoundTag)
        self.assertEqual(2, len(egg))
        self.assertEqual('Eggbert', egg['name'].value)
        self.assertEqual(0.5, egg['value'].value)
        ham = nested_compound['ham']
        self.assertIsInstance(ham, nbttag.CompoundTag)
        self.assertEqual(2, len(ham))
        self.assertEqual('Hampus', ham['name'].value)
        self.assertEqual(0.75, ham['value'].value)
        int_test = bigtest['intTest']
        self.assertIsInstance(int_test, nbttag.IntTag)
        self.assertEqual(2147483647, int_test.value)
        byte_test = bigtest['byteTest']
        self.assertIsInstance(byte_test, nbttag.ByteTag)
        self.assertEqual(127, byte_test.value)
        string_test = bigtest['stringTest']
        self.assertIsInstance(string_test, nbttag.StringTag)
        self.assertEqual(b'HELLO WORLD THIS IS A TEST STRING \xc3\x85\xc3\x84\xc3\x96!'.decode('utf8'), string_test.value)
        list_test_long = bigtest['listTest (long)']
        self.assertIsInstance(list_test_long, nbttag.ListTag)
        self.assertEqual(5, len(list_test_long))
        self.assertEqual(nbttag.LongTag, list_test_long.list_type)
        self.assertListEqual([
                nbttag.LongTag(None, 11),
                nbttag.LongTag(None, 12),
                nbttag.LongTag(None, 13),
                nbttag.LongTag(None, 14),
                nbttag.LongTag(None, 15),
            ],
            list_test_long.value)
        double_test = bigtest['doubleTest']
        self.assertIsInstance(double_test, nbttag.DoubleTag)
        self.assertEqual(0.49312871321823148, double_test.value)
        float_test = bigtest['floatTest']
        self.assertIsInstance(float_test, nbttag.FloatTag)
        self.assertEqual(0.49823147058486938, float_test.value)
        long_test = bigtest['longTest']
        self.assertIsInstance(long_test, nbttag.LongTag)
        self.assertEqual(9223372036854775807, long_test.value)
        list_test_compound = bigtest['listTest (compound)']
        self.assertIsInstance(list_test_compound, nbttag.ListTag)
        self.assertEqual(nbttag.CompoundTag, list_test_compound.list_type)
        self.assertListEqual([
                nbttag.CompoundTag(None, [
                    nbttag.StringTag('name', 'Compound tag #0'),
                    nbttag.LongTag('created-on', 1264099775885)
                ]),
                nbttag.CompoundTag(None, [
                    nbttag.StringTag('name', 'Compound tag #1'),
                    nbttag.LongTag('created-on', 1264099775885)
                ])
            ],
            list_test_compound.value)
        byte_arr_test = bigtest['byteArrayTest (the first 1000 values of (n*n*255+n*7)%100, starting with n=0 (0, 62, 34, 16, 8, ...))']
        self.assertIsInstance(byte_arr_test, nbttag.ByteArrayTag)
        self.assertListEqual([(i * i * 255 + i * 7) % 100 for i in range(1000)],
                             byte_arr_test.value)
        short_test = bigtest['shortTest']
        self.assertIsInstance(short_test, nbttag.ShortTag)
        self.assertEqual(short_test.value, 32767)
