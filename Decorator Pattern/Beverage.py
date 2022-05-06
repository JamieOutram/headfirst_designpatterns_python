from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):

    @property
    @abstractmethod
    def description(self) -> str:
        return "Unknown Beverage"

    @abstractmethod
    def cost(self) -> float:
        pass
