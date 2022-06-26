from Pizza import Pizza


class CheesePizza(Pizza):

    def prepare(self) -> None:
        print("Preparing Cheese Pizza")
        print("adding cheese")

    def bake(self) -> None:
        self._bake(12)


class HawaiianPizza(Pizza):

    def prepare(self) -> None:
        print("Preparing Hawaiian Pizza")
        print("adding cheese")
        print("adding ham")
        print("adding pineapple")

    def bake(self) -> None:
        self._bake(10)


class PepperoniPizza(Pizza):

    def prepare(self) -> None:
        print("Preparing Pepperoni Pizza")
        print("adding cheese")
        print("adding pepperoni")

    def bake(self) -> None:
        self._bake(10)