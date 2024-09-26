from city_weather import CityWeather

class WeatherForecastManager:
    '''The Weather Forecast Manager hold a dictionary of the cities with their weather forecasts (temperature, humidity, condition). 
    It provides methods to retrieve the weather for a particular city and to display the weather
    for a particular city.'''
    def __init__(self):
        self.forecasts = {
            "New York":CityWeather("New York", 70, 50, "Sunny"),
            "London": CityWeather("London", 60, 65, "Cloudy"),
            "Tokyo": CityWeather("Tokyo", 75, 70, "Rainy")
        }

    def get_weather(self, city):
        '''Method to return the weather forecast for a given city. If the city's forecast is NOT in the dictionary, 
        return "Weather data not available."'''
        return self.forecasts.get(city, f"\nWeather data not available for {city}.")
    
    def display_weather(self, city):
        '''Method to display the weather forecast for a given city. If the city's forecast is NOT in the dictionary,
        display "Weather data not available."'''
        # Retrieve the weather for the city
        forecast = self.get_weather(city)
        # If it exists, display the details of the weather forecast
        if isinstance(forecast, CityWeather):
            print(f"\nWeather for {city}: \n  Temperature: {forecast.temperature}"+u'\u00B0'+f"F\n  Humidity: {forecast.humidity}%\n  Condition: {forecast.condition}")
        # Otherwise display "Weather data not available."
        else: 
            print(forecast)
