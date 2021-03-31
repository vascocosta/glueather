# glueather

**A simple Python/Qt weather application using the OpenWeather API.**

glueather allows you to fetch the current weather as well as hourly and daily forecasts for any given location. The interface is extremely simple to use and multiplatform, working exactly the same across a variety of operating systems like MacOS, Linux or Windows.

Instead of showing fancy graphics glueather focuses on the actual meteorological data, neatly presented in a tabular fahsion, particularly useful for the forecasts. The data is provided by the free [OpenWeather API](https://openweathermap.org/), through thousands of distributed home weather stations in addition to standard sources of meteorological data.

In order to use the application you **need** to get an [API key](https://home.openweathermap.org/users/sign_up) from OpenWeather which you should paste into your conf.json file.

## Screenshots

![Windows screenshot 1](https://i.imgur.com/lTc87Yq.png)

# Features

* Simple interface
* Multiplatform (MacOS/Linux/Windows)
* Current weather
* Hourly forecast
* Daily forecast
* Units (Celsius/Fahrenheit)
* Persistent settings
* Advanced weather API (OpenWeather)

# Dependencies

* pyowm >= 3.2.0
* PyQt5 >= 5.15.1 or newer (on Debian Stable use 5.15.1) 

## Install

```
pip3 install pyowm
pip3 install pyqt5
```
