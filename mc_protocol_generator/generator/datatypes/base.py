from abc import ABC, abstractmethod
from mc_protocol_generator.generator.util import format_field_name
from ast import arg, Assign, Attribute, Name, Load, Store

class Base(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def field_name(self):
        return format_field_name(self.name)

    def get_field_name_set(self):
        return {self.field_name}

    def get_class_name_sets(self):
        return [set()]

    @property
    def type(self):
        pass

    def get_init_args(self):
        return (
            [
                arg(
                    arg=self.field_name,
                    annotation=None,
                    type_comment=None
                )
            ],
            []
        )

    def get_init_body_nodes(self):
        return [
            Assign(
                targets=[
                    Attribute(
                        value=Name(
                            id='self',
                            ctx=Load()
                        ),
                        attr=self.field_name,
                        ctx=Store()
                    )
                ],
                value=Name(
                    id=self.field_name,
                    ctx=Load()
                ),
                type_comment=None
            )
        ]

    @abstractmethod
    def get_len_node(self, sizer_name, object_override=None, node_override=None):
        pass

    @abstractmethod
    def get_repr_body_nodes(self, prefix):
        pass

    @abstractmethod
    def get_write_node(self, writer_name):
        pass

    @abstractmethod
    def get_read_node(self, reader_name):
        pass

    def get_module_body_nodes(self):
        pass

    @staticmethod
    @abstractmethod
    def from_protocol_data(data):
        pass
