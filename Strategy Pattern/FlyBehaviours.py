from abc import ABCMeta, abstractmethod


# Fly behaviour interface, an interface may only contain methods and all must be abstract
# There is no specific interface descriptor in python. This code will throw a type error
# if a subclass does not implement fly() when attempting to instantiate the subclass.
class FlyBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError  # This should never be called


# Fly with wings behaviour
class FlyWithWings(FlyBehaviour):
    def fly(self) -> None:
        print("I'm flying with wings")


# Fly with wings behaviour
class FlyNoWay(FlyBehaviour):

    def fly(self) -> None:
        print("I cant fly! :(")
