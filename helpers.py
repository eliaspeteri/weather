import json


def parseWind(wind_speed):
    wind_speed_text = ""
    if(wind_speed < 0.5):
        wind_speed_text = "calm"
    elif((wind_speed >= 0.5) & (wind_speed <= 1.5)):
        wind_speed_text = "light air"
    elif((wind_speed >= 1.6) & (wind_speed <= 3.3)):
        wind_speed_text = "light breeze"
    elif((wind_speed >= 3.4) & (wind_speed <= 5.5)):
        wind_speed_text = "gentle breeze"
    elif((wind_speed >= 5.6) & (wind_speed <= 7.9)):
        wind_speed_text = "moderate breeze"
    elif((wind_speed >= 8.0) & (wind_speed <= 10.7)):
        wind_speed_text = "fresh breeze"
    elif((wind_speed >= 10.8) & (wind_speed <= 13.8)):
        wind_speed_text = "strong breeze"
    elif((wind_speed >= 13.9) & (wind_speed <= 17.1)):
        wind_speed_text = "moderate gale"
    elif((wind_speed >= 17.2) & (wind_speed <= 20.7)):
        wind_speed_text = "gale"
    elif((wind_speed >= 20.8) & (wind_speed <= 24.4)):
        wind_speed_text = "strong gale"
    elif((wind_speed >= 24.5) & (wind_speed <= 28.4)):
        wind_speed_text = "storm"
    elif((wind_speed >= 28.5) & (wind_speed <= 32.6)):
        wind_speed_text = "violent storm"
    elif((wind_speed >= 32.7)):
        wind_speed_text = "hurricane force"
    return wind_speed_text


def printWeather(description, temperature, temperature_min, temperature_max, temperature_feels, pressure, humidity, visibility, wind_speed, wind_direction):
    return f"{description}\n\
temperature {temperature}C \
({temperature_min}C...{temperature_max}C), \
feels like {temperature_feels}C\n\
pressure {pressure} hPa\n\
humidity {humidity} %\n\
visibility {visibility} meters or more\n\
{parseWind(wind_speed)} \
({wind_speed} m/s at \
{wind_direction} degrees).\n"


def loadSettings():
    with open("settings.json", "r") as s:
        return json.load(s)
