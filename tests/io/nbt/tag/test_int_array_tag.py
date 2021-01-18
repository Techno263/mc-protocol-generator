import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import IntArrayTag

class TestIntArrayTag(unittest.TestCase):
    def test_init(self):
        tag = IntArrayTag('name', [10, 11, 255, 0])
        self.assertEqual('name', tag.name)
        self.assertListEqual([10, 11, 255, 0], tag.value)

    def test_type_id(self):
        self.assertEqual(11, IntArrayTag.type_id())

    def test_read(self):
        data = (b'\x0b\x00\x03arr\x00\x00\x00\x04\xff\xff\xff\xff'
                b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02')
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = IntArrayTag.read(buf, True, True)
        self.assertEqual('arr', tag.name)
        self.assertListEqual([-1, 0, 1, 2], tag.value)

    def test_write(self):
        tag = IntArrayTag('arr', [-1, 0, 1, 2])
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        true_data = data = (b'\x0b\x00\x03arr\x00\x00\x00\x04\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02')
        self.assertEqual(true_data, data)
