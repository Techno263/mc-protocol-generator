from . import TagBase
from .. import NBTTag

class EndTag(TagBase):
    def __init__(self):
        pass

    @staticmethod
    def type_id():
        return NBTTag.End

    @staticmethod
    def read(reader, has_type_id=False):
        if has_type_id:
            type_id = reader.read_ubyte()
            if type_id != NBTTag.End:
                raise Exception()
        return EndTag()

    def __bytes__(self):
        return bytes(NBTTag.End)

    def __repr__(self):
        return f'EndTag()'
