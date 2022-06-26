from Pizza import Pizza


class NYCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Grated Reggiano Cheese")

    @property
    def name(self) -> str:
        return "NY Style Sauce and Cheese Pizza"

    @property
    def dough(self) -> str:
        return "Thin Crust Dough"

    @property
    def sauce(self) -> str:
        return "Marinara Sauce"


class ChicagoCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Shredded Mozzarella Cheese")

    @property
    def name(self) -> str:
        return "Chicago Style Deep Dish Cheese Pizza"

    @property
    def dough(self) -> str:
        return "Extra Thick Crust Dough"

    @property
    def sauce(self) -> str:
        return "Plum Tomato Sauce"

    def cut(self) -> None:
        print("Cutting Pizza into 4 Square Slices")


class CaliforniaCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Shredded Cheddar Cheese")

    @property
    def name(self) -> str:
        return "California Style Crispy Cheese Pizza"

    @property
    def dough(self) -> str:
        return "Extra Thin Crust Dough"

    @property
    def sauce(self) -> str:
        return "Tomato Sauce"


class NYHawaiianPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Pineapple")
        self.toppings.append("Ham")

    @property
    def name(self) -> str:
        return "NY Style Sauce and Hawaiian Pizza"

    @property
    def dough(self) -> str:
        return "Thin Crust Dough"

    @property
    def sauce(self) -> str:
        return "Marinara Sauce"


class ChicagoHawaiianPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Pineapple")
        self.toppings.append("Ham")

    @property
    def name(self) -> str:
        return "Chicago Style Deep Dish Hawaiian Pizza"

    @property
    def dough(self) -> str:
        return "Extra Thick Crust Dough"

    @property
    def sauce(self) -> str:
        return "Plum Tomato Sauce"

    def cut(self) -> None:
        print("Cutting Pizza into 4 Square Slices")


class CaliforniaHawaiianPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Shredded Cheddar Cheese")
        self.toppings.append("Pineapple")
        self.toppings.append("Ham")

    @property
    def name(self) -> str:
        return "California Style Crispy Hawaiian Pizza"

    @property
    def dough(self) -> str:
        return "Extra Thin Crust Dough"

    @property
    def sauce(self) -> str:
        return "Tomato Sauce"


class NYPepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Pepperoni")

    @property
    def name(self) -> str:
        return "NY Style Sauce and Pepperoni Pizza"

    @property
    def dough(self) -> str:
        return "Thin Crust Dough"

    @property
    def sauce(self) -> str:
        return "Marinara Sauce"


class ChicagoPepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Pepperoni")

    @property
    def name(self) -> str:
        return "Chicago Style Deep Dish Pepperoni Pizza"

    @property
    def dough(self) -> str:
        return "Extra Thick Crust Dough"

    @property
    def sauce(self) -> str:
        return "Plum Tomato Sauce"

    def cut(self) -> None:
        print("Cutting Pizza into 4 Square Slices")


class CaliforniaPepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.toppings.append("Shredded Cheddar Cheese")
        self.toppings.append("Pepperoni")

    @property
    def name(self) -> str:
        return "California Style Crispy Pepperoni Pizza"

    @property
    def dough(self) -> str:
        return "Extra Thin Crust Dough"

    @property
    def sauce(self) -> str:
        return "Tomato Sauce"
