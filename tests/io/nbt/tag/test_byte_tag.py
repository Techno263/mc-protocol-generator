import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import ByteTag

class TestByteTag(unittest.TestCase):
    def test_init(self):
        tag = ByteTag('name', 100)
        self.assertEqual('name', tag.name)
        self.assertEqual(100, tag.value)

    def test_type_id(self):
        self.assertEqual(1, ByteTag.type_id())

    def test_read(self):
        data = b'\x01\x00\x04\x62\x79\x74\x65\x64'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = ByteTag.read(reader, True, True)
        self.assertEqual('byte', tag.name)
        self.assertEqual(100, tag.value)

    def test_write(self):
        tag = ByteTag('byte', 100)
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        self.assertEqual(b'\x01\x00\x04\x62\x79\x74\x65\x64', data)
