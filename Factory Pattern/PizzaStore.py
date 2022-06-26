from Pizza import Pizza
from abc import ABCMeta, abstractmethod


class PizzaStore(metaclass=ABCMeta):

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def _create_pizza(self, pizza_type) -> Pizza:
        pass
