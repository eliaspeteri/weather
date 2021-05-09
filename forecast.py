# Import sys for command line arguments
import sys
# Prints weather
from helpers import printWeather
# Loads settings from JSON
from helpers import loadSettings
# Needed to parse the response from the API
import json
# Used to fetch API response
import requests
# Loads settings into a dict
settings = loadSettings()
city = ""
# If no argument is given, use default in the settings
if (len(sys.argv) > 1):
    city = sys.argv[1]
else:
    city = settings['city']
# Here we fetch the forecast from the API
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={settings['key']}"
response = requests.get(url)
forecast = json.loads(response.text)
print(city)
# Prints the response in a human readable format
for forecast_i in range(3):
    date_text = forecast['list'][forecast_i]['dt_txt']
    description = forecast['list'][forecast_i]['weather'][0]['description']
    temperature = forecast['list'][forecast_i]['main']['temp']
    temperature_feels = forecast['list'][forecast_i]['main']['feels_like']
    temperature_min = forecast['list'][forecast_i]['main']['temp_min']
    temperature_max = forecast['list'][forecast_i]['main']['temp_max']
    pressure = forecast['list'][forecast_i]['main']['pressure']
    humidity = forecast['list'][forecast_i]['main']['humidity']
    visibility = forecast['list'][forecast_i]['visibility']
    wind_speed = forecast['list'][forecast_i]['wind']['speed']
    wind_direction = forecast['list'][forecast_i]['wind']['deg']
    # Finally we print the weather onto the command line
    print(f"{date_text}:")
    print(printWeather(description, temperature, temperature_min, temperature_max,
          temperature_feels, pressure, humidity, visibility, wind_speed, wind_direction))
