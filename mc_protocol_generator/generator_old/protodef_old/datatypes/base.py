from abc import ABC, abstractmethod

class DatatypeBase(ABC):

    @staticmethod
    def parse(options):
        print(options)