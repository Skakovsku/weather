import requests
from . import const
from pprint import pprint

weathers_data = {}

def get_weathers_data(data):
    for elem in data:
        if type(data[elem]) is dict:
            get_weathers_data(data[elem])
        elif type(data[elem]) == list:
            get_weathers_data(data[elem][0])
        elif elem in const.WEATHER_DATA:
            if type(data[elem]) == float:
                weathers_data[const.WEATHER_DATA[elem]] = int(data[elem])
            else:
                weathers_data[const.WEATHER_DATA[elem]] = data[elem]
    return weathers_data


def get_weather(request, town):
    text_town = ''
    if request == 'index':
        text_town = const.TEXT_TOWN
    response = requests.get(const.API_WEATHER_1 + town + const.API_WEATHER_2)
    data = response.json()
    pprint(data)
    if data['cod'] == '404':
        return {'cod': 'error'}
    weathers_param = get_weathers_data(data)
    if 'Направление:' in weathers_param:
        deg_wing = weathers_param['Направление:']
        for deg in const.WIND_DEG:
            if const.WIND_DEG[deg][0] <= deg_wing < const.WIND_DEG[deg][1]:
                weathers_param['Направление:'] = deg
                break
    sign = const.SIGN_BEGIN + data['weather'][0]['icon'] + const.SIGN_END
    description = data['weather'][0]['description']
    name = data['name']
    context = {
        'text_index': 'Погода в Вашем городе',
        'text_town': text_town,
        'sign': sign,
        'description': description,
        'name': name,
        'weather': {}
    }
    for param, val in weathers_param.items():
        context['weather'][param] = val
    pprint(context)
    return context