import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city="Little Elm"):
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"

    # print(request_url)
    weather_data = requests.get(request_url).json()

    return weather_data
    # pprint(weather_data)
    print(f"\nCurrent Weather for {weather_data["name"]}")
    print(f"\nThe temp is {weather_data["main"]["temp"]}")
    print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.")

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***")
    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Little Elm"

    weather_data = get_current_weather(city)

    print("/n")
    pprint(weather_data)