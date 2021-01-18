import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import IntTag

class TestByteTag(unittest.TestCase):
    def test_init(self):
        tag = IntTag('name', 100)
        self.assertEqual('name', tag.name)
        self.assertEqual(100, tag.value)

    def test_type_id(self):
        self.assertEqual(3, IntTag.type_id())

    def test_read(self):
        data = b'\x03\x00\x03int\xff\xff\xff\xff'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = IntTag.read(reader, True, True)
        self.assertEqual('int', tag.name)
        self.assertEqual(-1, tag.value)

    def test_write(self):
        tag = IntTag('int', -1)
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        self.assertEqual(b'\x03\x00\x03int\xff\xff\xff\xff', data)
