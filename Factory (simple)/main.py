from PizzaStore import PizzaStore
from SimplePizzaFactory import SimplePizzaFactory


def main():
    factory = SimplePizzaFactory()
    store = PizzaStore(factory)
    store.order_pizza("cheese")
    store.order_pizza("hawaiian")


if __name__ == "__main__":
    main()