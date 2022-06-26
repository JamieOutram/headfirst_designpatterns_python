from all_pizza_stores import *


def main():
    ny_store = NYPizzaStore()
    pizza_1 = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza_1.get_name()}\n")
    ch_store = ChicagoPizzaStore()
    pizza_2 = ch_store.order_pizza("hawaiian")
    print(f"Joel ordered a {pizza_2.get_name()}")


if __name__ == "__main__":
    main()
