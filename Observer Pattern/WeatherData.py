from IObserver import IObserver
from ISubject import ISubject
from typing import List


class WeatherData(ISubject):

    def __init__(self):
        self.observers: List[IObserver] = []
        self._temperature: float = None  # May initialise to initial values, set to none here for demo
        self._humidity: float = None
        self._pressure: float = None

    def register_observer(self, o: IObserver) -> None:
        self.observers.append(o)

    def remove_observer(self, o: IObserver) -> None:
        self.observers.remove(o)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update()

    def measurements_changed(self) -> None:
        # <-----Other local measurement changed updates can go here----->
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        # Trigger observer notification chain
        self.measurements_changed()

    # Encapsulate information with getters
    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure
