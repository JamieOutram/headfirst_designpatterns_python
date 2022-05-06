from abc import ABCMeta, abstractmethod
from IObserver import IObserver
from WeatherData import WeatherData


class IDisplay(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(IObserver, IDisplay):

    def __init__(self, weather_data: WeatherData):
        self.temperature: float = -99999
        self.humidity: float = -99999
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity*100  # displays humidity as percentage
        self.display()  # Only called here for demo, likely a gui subprocess would make this call

    def display(self):
        print(f"Current conditions: {self.temperature} degrees C "
              f"and {self.humidity}% humidity")


class StatisticsDisplay(IObserver, IDisplay):

    def __init__(self, weather_data: WeatherData):
        self.total_temperature: float = 0
        self.temperature_count: float = 0
        self.total_humidity: float = 0
        self.humidity_count = 0
        self.total_pressure: float = 0
        self.pressure_count = 0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    @property
    def avg_temperature(self):
        return self.total_temperature/self.temperature_count

    @property
    def avg_humidity(self):
        return self.total_humidity / self.humidity_count

    @property
    def avg_pressure(self):
        return self.total_pressure / self.pressure_count

    def update(self) -> None:
        self.total_temperature += self.weather_data.temperature
        self.temperature_count += 1.0
        self.total_humidity += self.weather_data.humidity
        self.humidity_count += 1.0
        self.total_pressure += self.weather_data.pressure
        self.pressure_count += 1.0
        self.display()  # Only called here for demo, likely a gui subprocess would make this call

    def display(self):
        print(f"Statistics: new measurements received\n"
              f"Avg temperature {self.avg_temperature:.1f}\n"
              f"Avg humidity {self.avg_humidity*100:.1f}\n"
              f"Avg pressure {self.avg_pressure:.1f}\n")


class HeatIndexDisplay(IObserver, IDisplay):

    def __init__(self, weather_data):
        self.temperature = 0
        self.humidity = 0
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)

    @property
    def _heat_index(self):
        t = self.temperature
        rh = self.humidity*100
        index = (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
                 (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
                 (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
                 (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                 (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
                 (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
                 0.000000000843296 * (t * t * rh * rh * rh)) - \
                (0.0000000000481975 * (t * t * t * rh * rh * rh))
        return index

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        print(f"Heat Index is {self._heat_index:.3f}")
