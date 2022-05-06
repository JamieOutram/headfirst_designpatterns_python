from all_display_observers import CurrentConditionsDisplay, StatisticsDisplay, HeatIndexDisplay
from WeatherData import WeatherData


def main():
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    heatindex_display = HeatIndexDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(21, 0.65, 30.4)
    weather_data.set_measurements(15, 0.70, 37.2)
    weather_data.set_measurements(10, 0.69, 42.0)


if __name__ == '__main__':
    main()
