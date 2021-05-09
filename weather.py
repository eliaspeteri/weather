# Import sys for command line arguments
import sys
# Used to fetch API response
import requests
# Needed to parse the response from the API
import json
# Prints weather
from helpers import printWeather
# Loads settings from JSON
from helpers import loadSettings
# Loads settings into a dict
settings = loadSettings()
city = ""
# If no argument is given, use default in the settings
if (len(sys.argv) > 1):
    city = sys.argv[1]
else:
    city = settings['city']
# Here we fetch the current weather from the API and store it in variables for reusability
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings['key']}"
response = requests.get(url)
weather = json.loads(response.text)
description = weather['weather'][0]['description']
temperature = weather['main']['temp']
temperature_feels = weather['main']['feels_like']
temperature_min = weather['main']['temp_min']
temperature_max = weather['main']['temp_max']
pressure = weather['main']['pressure']
humidity = weather['main']['humidity']
visibility = weather['visibility']
wind_speed = weather['wind']['speed']
wind_direction = weather['wind']['deg']

print(city)
print(printWeather(description, temperature, temperature_min, temperature_max,
      temperature_feels, pressure, humidity, visibility, wind_speed, wind_direction))
