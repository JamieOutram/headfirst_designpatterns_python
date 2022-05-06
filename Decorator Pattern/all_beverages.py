from Beverage import Beverage


class Espresso(Beverage):

    @property
    def description(self) -> str:
        return "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):

    @property
    def description(self) -> str:
        return "House blend coffee"

    def cost(self) -> float:
        return .89


class DarkRoast(Beverage):

    @property
    def description(self) -> str:
        return "Dark roast coffee"

    def cost(self) -> float:
        return .99


class Decaf(Beverage):

    @property
    def description(self) -> str:
        return "Decaf coffee"

    def cost(self) -> float:
        return 1.05