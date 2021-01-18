import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import FloatTag

class TestDoubleTag(unittest.TestCase):
    def test_init(self):
        tag = FloatTag('name', 0.5)
        self.assertEqual('name', tag.name)
        self.assertEqual(0.5, tag.value)

    def test_type_id(self):
        self.assertEqual(5, FloatTag.type_id())

    def test_read(self):
        data = b'\x05\x00\x05value\x3f\x00\x00\x00'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = FloatTag.read(reader, True, True)
        self.assertEqual('value', tag.name)
        self.assertEqual(0.5, tag.value)

    def test_write(self):
        tag = FloatTag('value', 0.5)
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        self.assertEqual(b'\x05\x00\x05value\x3f\x00\x00\x00', data)
