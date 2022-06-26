from Pizza import Pizza
from all_pizzas import *


class SimplePizzaFactory:

    def create_pizza(self, pizza_type: str):

        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "hawaiian":
            pizza = HawaiianPizza()
        elif pizza_type == "peperoni":
            pizza = PepperoniPizza()
        else:
            raise ValueError(pizza_type)

        return pizza



