import unittest
import io
from mc_protocol_generator.io import DataReader, DataWriter
from mc_protocol_generator.io.nbt.tag import CompoundTag, ByteTag, StringTag, IntTag

class TestCompoundTag(unittest.TestCase):
    def test_init(self):
        tag = CompoundTag('compound', [ByteTag('byte', 100)])
        self.assertEqual('compound', tag.name)
        self.assertListEqual([ByteTag('byte', 100)], tag.value)

    def test_type_id(self):
        self.assertEqual(10, CompoundTag.type_id())

    def test_read(self):
        data = (b'\x0a\x00\x0b\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72'
                b'\x6c\x64\x01\x00\x04\x62\x79\x74\x65\x64\x08\x00'
                b'\x04\x6e\x61\x6d\x65\x00\x09\x42\x61\x6e\x61\x6e'
                b'\x72\x61\x6d\x61\x00')
        buf = io.BytesIO(data)
        reader = DataReader(buf)
        tag = CompoundTag.read(reader, True, True)
        self.assertEqual('hello world', tag.name)
        self.assertEqual(2, len(tag))
        self.assertEqual('byte', tag['byte'].name)
        self.assertEqual(100, tag['byte'].value)
        self.assertEqual('name', tag['name'].name)
        self.assertEqual('Bananrama', tag['name'].value)

    def test_write(self):
        tag = CompoundTag('zombie', [StringTag('name', 'Dave'), IntTag('health', 20)])
        buf = io.BytesIO()
        writer = DataWriter(buf)
        tag.write(writer)
        buf.seek(0, 0)
        data = buf.read()
        true_data = (b'\x0a\x00\x06zombie\x08\x00\x04name\x00\x04Dave'
                     b'\x03\x00\x06health\x00\x00\x00\x14\x00')
        self.assertEqual(true_data, data)
