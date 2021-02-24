from .base import Base
from ast import Attribute, Name, Load, Call

class VarLong(Base):
    @property
    def type(self):
        return int

    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        if object_override == None:
            obj = Name(
                id='self',
                ctx=Load()
            )
        else:
            obj = value_override
        if node_override == None:
            node = Attribute(
                value=obj,
                attr=self.field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return Call(
            func=Attribute(
                value=Name(
                    id=sizer_name,
                    ctx=Load()
                ),
                attr='varlong_size',
                ctx=Load()
            ),
            args=[node],
            keywords=[]
        )

    def get_write_node(self, writer_name):
        pass

    def get_read_node(self, reader_name):
        pass

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == 'VarLong'
        name = data['name'] if 'name' in data else None
        return VarLong(name)
