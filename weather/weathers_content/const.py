import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_WEATHER = os.getenv('token_weather')
API_WEATHER_1 = 'https://api.openweathermap.org/data/2.5/weather?q='
API_WEATHER_2 = '&units=metric&lang=ru&appid=' + TOKEN_WEATHER

API_FOR_1 = 'https://api.openweathermap.org/data/2.5/forecast?lat='
API_FOR_2 = '&units=metric&lang=ru&appid=' + TOKEN_WEATHER

TEXT_TOWN_1 = 'Ваше местоположение определено автоматически. '
TEXT_TOWN_2 = 'Если населенный пункт определён неверно, кликните '
TEXT_TOWN_3 = 'кнопку ниже и настройте местоположение вручную.'
TEXT_TOWN = TEXT_TOWN_1 + TEXT_TOWN_2 + TEXT_TOWN_3

TEXT_INDEX = 'Погода в Вашем городе'

SPEC_CITY_1 = 'К сожалению, такого города нет в базе. '
SPEC_CITY_2 = 'Укажите близлежащий населенный пункт'
SPEC_CITY = SPEC_CITY_1 + SPEC_CITY_2

SIGN_BEGIN = 'http://openweathermap.org/img/wn/'
SIGN_END = '@2x.png'

WIN_DEG = {
    'Сев.': [0, 44],
    'Сев.-Вос.': [45, 90],
    'Вос.': [91, 135],
    'Юго-Вос.': [136, 180],
    'Юж.': [181, 225],
    'Юго-Зап.': [226, 270],
    'Зап': [271, 315],
    'Сев.-Зап.': [316, 360]
}

WEATHER_DATA = {
    'feels_like': 'Ощущается как, °C:',
    'humidity': 'Влажность воздуха, %:',
    'pressure': 'Атмосферное давление, гПа:',
    'temp': 'Температура воздуха, °C:',
    'visibility': 'Видимость, м:',
    'deg': 'Направление:',
    'gust': 'Порывы до, м/с',
    'speed': 'Скорость ветра, м/с:',
    'all': 'Oблачность, %:',
    '1h': 'Уровень осадков за час, мм'
}

HALF_DAY = 43200
DAY = 86400

LIST_LINK_GORO = [
    'ignio-daily-ero',
    'ignio-daily-cook',
    'ignio-daily-lov',
    'ignio-daily-mob',
    'ignio-daily-anti',
    'ignio-weekly-lov'
]
