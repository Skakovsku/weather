from pprint import pprint
import requests
from . import const

"""weathers_data = {}

def get_weathers_data(data):
    for elem in data:
        print(data[elem])
        if type(data[elem]) is dict:
            get_weathers_data(data[elem])
        elif type(data[elem]) == list:
            for list_elem in data[elem][0]:
                get_weathers_data(list_elem)
        elif elem in const.WEATHER_DATA:
            if type(data[elem]) == float:
                weathers_data[elem] = int(data[elem])
            else:
                weathers_data[elem] = data[elem]
    return weathers_data"""


def get_weather(request, town):
    text_town = ''
    if request == 'index':
        text_town = const.TEXT_TOWN
    response = requests.get(const.API_WEATHER_1 + town + const.API_WEATHER_2)
    data = response.json()
    pprint(data)
    if data['cod'] == '404':
        return {'data': {'cod': '404'}}
    sign = const.SIGN_BEGIN + data['weather'][0]['icon'] + const.SIGN_END
    description = data['weather'][0]['description']
    temp = int(data['main']['temp'])
    feels_like = int(data['main']['feels_like'])
    wind_speed = int(data['wind']['speed'])
    for deg in const.WIND_DEG.items():
        if deg[1][0] <= (int(data['wind']['deg'])+22) <= deg[1][1]:
            wind_deg = deg[0]
            break
    wind_gust = None
    if 'gust' in data['wind']:
        wind_gust = int(data['wind']['gust'])
    wind = {'speed': wind_speed, 'gust': wind_gust, 'deg': wind_deg}
    context = {
        'text_index': 'Погода в Вашем городе',
        'text_town': text_town,
        'data': data,
        'temp': temp,
        'feels_like': feels_like,
        'wind': wind,
        'town': town,
        'sign': sign,
        'description': description,
    }
    return context