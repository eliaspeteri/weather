# Description

This is my command line interface for fetching weather and forecast from OpenWeatherMap API. Currently it has two scripts with one parameter each for the city. Python 3+ is required, though it can be easily converted to Python 2.

For ease of use, it is recommended to install or make a symbolic link in the C:/Users/{User}-folder or whatever your default folder is when opening up a new terminal. You also need an API key from OpenWeatherMap. Finally, you need to setup the settings.json-file with your key and preferred location.

## Folder structure

The folder structure after installation should be:

/weather

-> .gitignore

-> example_settings.json

-> forecast.py

-> helpers.py

-> README.MD

-> weather.py

# Usage

## Fetching current weather

Current weather can be called by command

```
python weather.py
```

or for a specific location

```
python weather.py {location}
```

without the brackets.

## Fetching the forecast

Similarly to the weather.py script, forecast can be fetched with

```
python forecast.py
```

or for a specific location

```
python forecast.py {location}
```

without the brackets.

# Uninstallation

Simply remove the project folder.

# Final notes

This project was made for personal use and may or may not match your expectations. YMMV.
