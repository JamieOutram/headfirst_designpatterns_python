from Duck import Duck
from FlyBehaviours import FlyWithWings
from QuackBehaviours import Quack


class MallardDuck(Duck):

    @property
    def fly_behaviour(self):
        return FlyWithWings()

    @property
    def quack_behaviour(self):
        return Quack()

    def display(self) -> None:
        print("I am a mallard duck")
