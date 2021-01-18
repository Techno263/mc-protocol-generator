import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import ByteArrayTag

class TestByteArrayTag(unittest.TestCase):
    def test_init(self):
        tag = ByteArrayTag('name', [10, 20])
        self.assertEqual('name', tag.name)
        self.assertListEqual([10, 20], tag.value)

    def test_insert(self):
        tag = ByteArrayTag('name', [10, 20])
        tag.insert(0, 0)
        self.assertListEqual([0, 10, 20], tag.value)
        tag.insert(3, 30)
        self.assertListEqual([0, 10, 20, 30], tag.value)
        tag.insert(1, 5)
        self.assertListEqual([0, 5, 10, 20, 30], tag.value)

    def test_type_id(self):
        self.assertEqual(7, ByteArrayTag.type_id())

    def test_read(self):
        data = b'\x07\x00\x03\x61\x72\x72\x00\x00\x00\x04\x01\x02\x03\xff'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = ByteArrayTag.read(reader, has_name=True, has_type_id=True)
        self.assertEqual('arr', tag.name)
        self.assertEqual(4, len(tag))
        self.assertEqual(1, tag[0])
        self.assertEqual(2, tag[1])
        self.assertEqual(3, tag[2])
        self.assertEqual(-1, tag[3])

    def test_write(self):
        tag = ByteArrayTag('arr', [1, 2, 3, -1])
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        self.assertEqual(b'\x07\x00\x03\x61\x72\x72\x00\x00\x00\x04\x01\x02\x03\xff', data)

    def test_mixed(self):
        data = b'\x07\x00\x03\x61\x72\x72\x00\x00\x00\x04\x01\x02\x03\xff'
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = ByteArrayTag.read(reader, has_name=True, has_type_id=True)
        tag.append(5)
        tag.insert(0, -2)
        self.assertEqual('arr', tag.name)
        self.assertEqual(6, len(tag))
        self.assertEqual(-2, tag[0])
        self.assertEqual(1, tag[1])
        self.assertEqual(2, tag[2])
        self.assertEqual(3, tag[3])
        self.assertEqual(-1, tag[4])
        self.assertEqual(5, tag[5])
