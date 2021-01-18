import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import DoubleTag

class TestDoubleTag(unittest.TestCase):
    def test_init(self):
        tag = DoubleTag('name', 2.34)
        self.assertEqual('name', tag.name)
        self.assertEqual(2.34, tag.value)

    def test_type_id(self):
        self.assertEqual(6, DoubleTag.type_id())

    def test_read(self):
        data = b'\x06\x00\x05value\x40\x02\xb8\x51\xeb\x85\x1e\xb8'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = DoubleTag.read(reader, True, True)
        self.assertEqual('value', tag.name)
        self.assertEqual(2.34, tag.value)

    def test_write(self):
        tag = DoubleTag('value', 2.34)
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        self.assertEqual(b'\x06\x00\x05value\x40\x02\xb8\x51\xeb\x85\x1e\xb8', data)
