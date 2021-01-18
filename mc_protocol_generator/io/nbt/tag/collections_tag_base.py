from abc import abstractmethod
from collections.abc import Iterator, Sequence, MutableSequence, Mapping, MutableMapping
from .tag_base import TagBase

class TagNameIterator(Iterator):

    def __init__(self, tag_iter):
        self._iter = tag_iter

    def __next__(self):
        return next(self._iter).name

class TagItemIterator(Iterator):

    def __init__(self, tag_iter):
        self._iter = tag_iter

    def __next__(self):
        n = next(self._iter)
        return n.name, n

class SequenceTagBase(TagBase, Sequence):

    def __getitem__(self, key):
        return self.value[key]
    
    def __len__(self):
        return len(self.value)

class MutableSequenceTagBase(SequenceTagBase, MutableSequence):

    def insert(self, index, object):
        self.value.insert(index, object)

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

class MappingTagBase(TagBase, Mapping):

    def items(self):
        return TagItemIterator(iter(self.value))

    def values(self):
        return iter(self.value)

    def __getitem__(self, key):
        for t in self.value:
            if t.name == key:
                return t
        raise KeyError(key)

    def __iter__(self):
        return TagNameIterator(iter(self.value))

    def __len__(self):
        return len(self.value)


class MutableMappingTagBase(MappingTagBase, MutableMapping):

    def __setitem__(self, key, value):
        if key != value.name:
            raise KeyError('Key must be same as value name')
        if key in self:
            del self[key]
        self.value.append(value)

    def __delitem__(self, key):
        for i, t in enumerate(self.value):
            if t.name == key:
                del self.value[i]
                return
        return KeyError(key)
