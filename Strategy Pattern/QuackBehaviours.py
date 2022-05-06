from abc import ABCMeta, abstractmethod


# Quack behaviour interface
class QuackBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def quack(self) -> None:
        raise NotImplementedError


# Fly with wings behaviour
class Quack(QuackBehaviour):
    def quack(self) -> None:
        print("Quack!")


# Fly with wings behaviour
class Squeak(QuackBehaviour):
    def quack(self) -> None:
        print("Squeak!")
