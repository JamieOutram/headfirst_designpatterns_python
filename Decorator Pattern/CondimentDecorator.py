from Beverage import Beverage
from abc import abstractmethod


class CondimentDecorator(Beverage):

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def beverage(self) -> Beverage:
        return self._beverage

    @property
    @abstractmethod
    def description(self):
        return "Unknown Condiment"
