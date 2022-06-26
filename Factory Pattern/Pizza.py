from abc import ABCMeta, abstractmethod
from typing import List


class Pizza(metaclass=ABCMeta):

    def __init__(self):
        self.toppings: List[str] = []

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def dough(self) -> str:
        pass

    @property
    @abstractmethod
    def sauce(self) -> str:
        pass

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        print(f"Tossing dough...")
        print(f"Adding sauce...")
        print(f"Adding toppings:")
        for t in self.toppings:
            print(f"   {t}")

    def bake(self) -> None:
        print(f"Bake for 25 minutes at 350")

    def cut(self) -> None:
        print(f"Cutting pizza into 8 triangular slices")

    def box(self) -> None:
        print(f"Place pizza in official PizzaStore box")

    def get_name(self) -> str:
        return self.name
