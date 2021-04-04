# glueather

A simple Python/Qt weather application using the OpenWeather API.

glueather allows you to fetch the current weather as well as hourly and daily forecasts for any given location. The interface is extremely simple to use and multiplatform, working exactly the same across a variety of operating systems like MacOS, Linux or Windows.
w
Instead of showing fancy graphics glueather focuses on the actual meteorological data, neatly presented in a tabular fahsion, particularly useful for the forecasts. The data is provided by the free [OpenWeather API](https://openweathermap.org/), through thousands of distributed home weather stations in addition to standard sources of meteorological data.

## Attention!

The application **requires** you to get an [API key](https://home.openweathermap.org/users/sign_up) from OpenWeather which you should paste into your .glueather.conf file located immediately under your home folder ($HOME/.glueather.conf on MacOS/Linux and %USERPROFILE%\.glueather.conf on Windows). The configuration file is automatically created the first time you run glueather, however the API key field is left empty.

# Screenshots

## Windows

![Windows screenshot 1](https://i.imgur.com/lTc87Yq.png)

## Linux

![Linux screenshot 1](https://i.imgur.com/494m1jA.png)

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

* Python >= 3.7.0
* pyowm >= 3.2.0
* PyQt5 >= 5.15.1 (on Debian Stable use specifically 5.12.1) 

# Install (pip)

```
pip install glueather
```

# Install (source)

## Global

```
git clone https://github.com/vascocosta/glueather.git
pip install pyowm
pip install pyqt5
```

## Venv

### MacOS/Linux

```
git clone https://github.com/vascocosta/glueather.git
cd glueather
pyhton -m venv venv
source venv/bin/activate
pip install pyowm
pip install pyqt5
```

### Windows

```
git clone https://github.com/vascocosta/glueather.git
cd glueather
pyhton -m venv venv
venv\Scripts\activate
pip install pyowm
pip install pyqt5
```

# Run (if installed with pip)

```
glueather
```

# Run (if installed from source)

```
cd glueather/src/
python glueather.py
```
