class CityWeather:
    '''Each CityWeather object will have a city, temperature (in degrees Fahrenheit), humidity (%), and 
    condition (Sunny, Partly Sunny, Partly Cloudy, Cloudy, Rainy, Snowy, Hail, Tornado, Hurricane).'''
    def __init__(self, city, temperature, humidity, condition):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition