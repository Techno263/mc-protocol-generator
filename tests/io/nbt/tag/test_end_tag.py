import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import EndTag

class TestEndTag(unittest.TestCase):
    def test_init(self):
        tag = EndTag()
        self.assertIsNone(tag.name)
        self.assertIsNone(tag.value)

    def test_type_id(self):
        self.assertEqual(0, EndTag.type_id())

    def test_read(self):
        data = b'\x00'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = EndTag.read(reader, True)
        self.assertIsNone(tag.name)
        self.assertIsNone(tag.value)

    def test_write(self):
        tag = EndTag()
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        self.assertEqual(b'\x00', data)
