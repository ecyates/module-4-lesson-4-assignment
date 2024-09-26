from weather_forecast_manager import WeatherForecastManager

def main():
    while True:
        try: 
            # Retrieve the weather forecast manager
            weather_forecast = WeatherForecastManager()
            # Prompt the user for the city 
            city = input("\nEnter the city to get the weather forecast or 'exit' to quit: ")
            # Quit the program if the user asks to
            if city.lower() == 'exit':
                break
            else: 
                # Display the weather of the user's selected city.
                weather_forecast.display_weather(city)
        # Catch any exceptions
        except Exception as e:
            print(f"\nAn error occurred: {e}.")
    print("\nWeather Forecast Manager successful closed. Have a great day, whatever the weather may be!\n")

if __name__ == "__main__":
    main()