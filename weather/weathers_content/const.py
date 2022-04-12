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
TEXT_TOWN_3 = 'кнопку ниже и настройте местоположение в ручную.'
TEXT_TOWN = TEXT_TOWN_1 + TEXT_TOWN_2 + TEXT_TOWN_3

TEXT_INDEX = 'Погода в Вашем городе'

SPEC_CITY_1 = 'К сожалению, такого города нет в базе. '
SPEC_CITY_2 = 'Укажите близлежащий населенный пункт'
SPEC_CITY = SPEC_CITY_1 + SPEC_CITY_2

SIGN_BEGIN = 'http://openweathermap.org/img/wn/'
SIGN_END = '@2x.png'

WIND_DEG = {
    'северный': [0, 44],
    'северо-восточный': [45, 90],
    'восточный': [91, 135],
    'юго-восточный': [136, 180],
    'южный': [181, 225],
    'юго-западный': [226, 270],
    'западный': [271, 315],
    'северо-западный': [316, 360]
}

WEATHER_DATA = {
    'feels_like': 'Ощущается как, °C:',
    'humidity': 'Влажность воздуха, %:',
    'pressure': 'Атмосферное давление, Гпа:',
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
