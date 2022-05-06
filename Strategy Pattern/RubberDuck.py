from Duck import Duck
from FlyBehaviours import FlyNoWay
from QuackBehaviours import Squeak


class RubberDuck(Duck):

    @property
    def fly_behaviour(self):
        return FlyNoWay()

    @property
    def quack_behaviour(self):
        return Squeak()

    def display(self) -> None:
        print("I am a rubber duck")
