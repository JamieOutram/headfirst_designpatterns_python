from abc import ABCMeta, abstractmethod
from IObserver import IObserver


class ISubject(metaclass=ABCMeta):  # Here we are using I prefix notation to denote an interface

    @abstractmethod
    def register_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass
