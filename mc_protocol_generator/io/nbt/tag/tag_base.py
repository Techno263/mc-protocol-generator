from abc import ABC, abstractmethod

class TagBase(ABC):
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
