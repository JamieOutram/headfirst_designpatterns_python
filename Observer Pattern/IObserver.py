from abc import ABCMeta, abstractmethod


class IObserver(metaclass=ABCMeta):  # Here we are using I prefix notation to denote an interface

    @abstractmethod
    def update(self) -> None:
        pass
