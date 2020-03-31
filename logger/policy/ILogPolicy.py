from abc import ABCMeta, abstractmethod

from logger.Log import Log


class ILogPolicy(metaclass=ABCMeta):

    @abstractmethod
    def write(self, log: Log):
        raise NotImplementedError()
