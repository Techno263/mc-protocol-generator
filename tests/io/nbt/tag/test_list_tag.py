import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import ListTag, IntTag

class TestListTag(unittest.TestCase):
    def test_init(self):
        tag = ListTag('nums', [IntTag(None, -1), IntTag(None, 1)], IntTag)
        self.assertEqual('nums', tag.name)
        self.assertEqual([IntTag(None, -1), IntTag(None, 1)], tag.value)

    def test_type_id(self):
        self.assertEqual(9, ListTag.type_id())

    def test_read(self):
        data = (b'\x09\x00\x04nums\x03\x00\x00\x00\x03'
                b'\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x01')
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = ListTag.read(reader, True, True)
        self.assertEqual('nums', tag.name)
        self.assertEqual([IntTag(None, -1), IntTag(None, 0), IntTag(None, 1)], tag.value)

    def test_write(self):
        tag = ListTag('nums', [IntTag(None, -1), IntTag(None, 0), IntTag(None, 1)], IntTag)
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        true_data = (b'\x09\x00\x04nums\x03\x00\x00\x00\x03'
                     b'\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x01')
        self.assertEqual(true_data, data)
