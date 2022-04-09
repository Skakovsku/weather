API_WEATHER_1 = 'https://api.openweathermap.org/data/2.5/weather?q='
API_WEATHER_2 = '&units=metric&lang=ru&appid=092e16bc85bd3596b7c24349e1623625'

TEXT_TOWN_1 = 'Ваше местоположение определено автоматически. '
TEXT_TOWN_2 = 'Если населенный пункт определён неверно, кликните '
TEXT_TOWN_3 = 'кнопку ниже и настройте местоположение в ручную.'
TEXT_TOWN = TEXT_TOWN_1 + TEXT_TOWN_2 + TEXT_TOWN_3

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
    'feels_like': 3.71,
    'grnd_level': 981,
    'humidity': 84,
    'pressure': 1003,
    'temp': 6.55,
    'name': 'Ступино',
    'sys': {'country': 'RU', 'sunrise': 1649471994, 'sunset': 1649521103},
    'timezone': 10800,
    'visibility': 10000,
    'description': 'облачно с прояснениями',
    'icon': '04d',
    'main': 'Clouds',
    'deg': 222,
    'gust': 6.89,
    'speed': 4.1
}
