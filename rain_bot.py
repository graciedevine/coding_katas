import os

import requests

WEATHER_API_KEY = os.getenv('5b857f49d7c783ba9e0fce0ab40f14d0')
LATITUDE = os.getenv('37.0871° N')
LONGITUDE = os.getenv('76.4730° W')
BOT_API_KEY = os.getenv('1594150523:AAFeFGHKhuk8IHkpoJ1i9ylf3ExIP9w0D9c')
CHANNEL_NAME = os.getenv('Rain Forecast')

if __name__ == '__main__':
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={37.0871° N}&lon={76.4730° W}&APPID={'5b857f49d7c783ba9e0fce0ab40f14d0'}")
    forecast = resp.json()['daily'][0]
    today_weather = forecast['weather'][0]['description']
    if 'rain' in today_weather:
        requests.get(f'https://api.telegram.org/bot{1594150523:AAFeFGHKhuk8IHkpoJ1i9ylf3ExIP9w0D9c}/sendMessage',
                     params={'chat_id': 'Rain Forecast',
                             'text': 'It\'s going to rain today \U00002614, take your umbrella with you!'})
