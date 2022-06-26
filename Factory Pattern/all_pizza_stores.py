from PizzaStore import PizzaStore
from all_pizzas import *


class NYPizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            pizza = NYCheesePizza()
        elif pizza_type == "hawaiian":
            pizza = NYHawaiianPizza()
        elif pizza_type == "peperoni":
            pizza = NYPepperoniPizza()
        else:
            raise ValueError(pizza_type)

        return pizza


class ChicagoPizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            pizza = ChicagoCheesePizza()
        elif pizza_type == "hawaiian":
            pizza = ChicagoHawaiianPizza()
        elif pizza_type == "peperoni":
            pizza = ChicagoPepperoniPizza()
        else:
            raise ValueError(pizza_type)

        return pizza


class CaliforniaPizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            pizza = CaliforniaCheesePizza()
        elif pizza_type == "hawaiian":
            pizza = CaliforniaHawaiianPizza()
        elif pizza_type == "peperoni":
            pizza = CaliforniaPepperoniPizza()
        else:
            raise ValueError(pizza_type)

        return pizza
