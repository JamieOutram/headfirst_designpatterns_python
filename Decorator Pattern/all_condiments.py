from CondimentDecorator import CondimentDecorator


class Mocha(CondimentDecorator):

    @property
    def description(self) -> str:
        return self.beverage.description + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + .20


class SteamedMilk(CondimentDecorator):

    @property
    def description(self) -> str:
        return self.beverage.description + ", Steamed milk"

    def cost(self) -> float:
        return self.beverage.cost() + .10


class Soy(CondimentDecorator):

    @property
    def description(self) -> str:
        return self.beverage.description + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + .15


class Whip(CondimentDecorator):

    @property
    def description(self) -> str:
        return self.beverage.description + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + .10
