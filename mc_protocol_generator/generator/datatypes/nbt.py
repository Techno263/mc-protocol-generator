from .base import Base
from ast import Call, Attribute, Name, Load, Expr, Assign, Store
from mc_protocol_generator.generator.datatypes.constants import NBT_DATATYPE_NAME

class NBT(Base):
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
                attr='nbt_size',
                ctx=Load()
            ),
            args=[node],
            keywords=[]
        )

    def get_write_nodes(self, writer_name, node_override=None):
        if node_override == None:
            node = Attribute(
                value=Name(id='self', ctx=Load()),
                attr=self.field_name,
                ctx=Load()
            )
        else:
            node = node_override
        return [
            Expr(
                value=Call(
                    func=Attribute(
                        value=Name(id=writer_name, ctx=Load()),
                        attr='write_nbt',
                        ctx=Load(),
                    ),
                    args=[
                        Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr=self.field_name,
                            ctx=Load()
                        )
                    ],
                    keywords=[],
                )
            )
        ]

    def get_read_nodes(self, reader_name, do_assign=True):
        value_op = Call(
            func=Attribute(
                value=Name(id=reader_name, ctx=Load()),
                attr='read_nbt',
                ctx=Load()
            ),
            args=[],
            keywords=[]
        )
        if do_assign:
            return [
                Assign(
                    targets=[Name(id=self.field_name, ctx=Store())],
                    value=value_op
                )
            ]
        return value_op

    @staticmethod
    def from_protocol_data(data):
        assert data['type'] == NBT_DATATYPE_NAME
        name = data['name'] if 'name' in data else None
        return NBT(name)
