from abc import ABC, abstractmethod

class TagBase(ABC):
    @abstractmethod
    def write(self, writer, write_type_id=True):
        pass

    @staticmethod
    def type_id(self):
        pass

    @staticmethod
    def read(reader, has_name=True, has_type_id=False):
        pass

    @abstractmethod
    def __bytes__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value
