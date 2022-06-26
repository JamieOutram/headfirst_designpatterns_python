from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self) -> None:
        pass

    @abstractmethod
    def bake(self) -> None:
        pass

    def cut(self) -> None:
        print("Cutting pizza")

    def box(self) -> None:
        print("Boxing pizza")

    def _bake(self, time) -> None:
        print(f"baking for {time} minutes")
