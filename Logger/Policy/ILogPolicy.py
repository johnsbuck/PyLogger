from abc import ABCMeta, abstractmethod

from Logger.Log import Log


class ILogPolicy(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name: str):
        raise NotImplementedError()

    @abstractmethod
    def open(self, name: str):
        raise NotImplementedError()

    @abstractmethod
    def write(self, log: Log):
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        raise NotImplementedError()
