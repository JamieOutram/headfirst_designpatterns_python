from abc import ABCMeta, abstractmethod
from FlyBehaviours import FlyBehaviour
from QuackBehaviours import QuackBehaviour


# Abstract base class for DUCK
class Duck(metaclass=ABCMeta):

    @property
    @abstractmethod
    def fly_behaviour(self) -> FlyBehaviour:
        pass

    @property
    @abstractmethod
    def quack_behaviour(self) -> QuackBehaviour:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

    # Offload fly logic to flyBehaviour
    def perform_fly(self) -> None:
        self.fly_behaviour.fly()

    # Offload fly logic to flyBehaviour
    def perform_quack(self) -> None:
        self.quack_behaviour.quack()
