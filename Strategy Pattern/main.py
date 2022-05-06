from Duck import Duck
from MallardDuck import MallardDuck
from RubberDuck import RubberDuck


def squawk(duck: Duck):
    print(duck.__class__)
    duck.perform_fly()
    duck.perform_quack()


def main():
    mallard = MallardDuck()
    rubber = RubberDuck()
    squawk(mallard)
    squawk(rubber)
    return 0


if __name__=="__main__":
    main()


