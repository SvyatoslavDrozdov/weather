import requests
import geocoder
from datetime import datetime, timezone, timedelta
from weather.config import key, url


def get_weather(city) -> list:
    """
    Эта функция возвращает список в котором содержится вся необходимая информация о погоде.

    Returns:
        list: [Current time, City name, Weather, Current temperature, Feels like, Wind speed]
    """
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    time_shift = weather.get("timezone")
    time_zone = timezone(timedelta(seconds=time_shift))
    current_time = datetime.now(time_zone).strftime("%Y-%m-%d %H:%M:%S")
    if str(time_zone) == "UTC":
        time_zone = "UTC+00:00"

    information = [
        f"Current time: {current_time + " " + str(time_zone)}",
        f"City name: {city}",
        f"Weather: {weather["weather"][0]["description"]}",
        f"Current temperature: {weather["main"]["temp"]} degrees Celsius",
        f"Feels like: {weather["main"]["feels_like"]} degrees Celsius",
        f"Wind speed: {weather["wind"]["speed"]} m/s"
    ]

    return information


def get_current_city() -> str:
    """
    Эта функция возвращает название города по текущему местоположению пользователя.

    Returns:
        str: название города
    """
    return geocoder.ip('me').city
