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


def get_forecast(lat, lon):
    coord = str(lat) + '&lon=' + str(lon)
    response = requests.get(const.API_FOR_1 + coord + const.API_FOR_2)
    data_for = response.json()
    forecast = []
    forecast_param = {}
    for time_for in data_for['list']:
        if (time_for['dt'] + const.HALF_DAY) % const.DAY == 0:
            forecast_param[time_for['dt_txt']] = ''
            forecast_param[int(time_for['main']['temp'])] = ''
            title = time_for['weather'][0]
            forecast_param[title['description']] = ''
            sign = const.SIGN_BEGIN + title['icon'] + const.SIGN_END
            forecast_param[sign] = ''
            forecast.append(forecast_param)
        forecast_param = {}
    """forecast = {}
    forecast_param = {}
    for time_for in data_for['list']:
        if (time_for['dt'] + const.HALF_DAY) % const.DAY == 0:
            forecast_param['Температура, °C:'] = int(time_for['main']['temp'])
            title = time_for['weather'][0]
            forecast_param[title['icon']] = title['description']
            forecast[time_for['dt_txt']] = forecast_param
        forecast_param = {}"""
    pprint(forecast)
    return forecast


def get_weather(request, town):
    text_town = ''
    if request == 'index':
        text_town = const.TEXT_TOWN
    response = requests.get(const.API_WEATHER_1 + town + const.API_WEATHER_2)
    data = response.json()
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
    # Получаем прогноз
    lat, lon = data['coord']['lat'], data['coord']['lon']
    forecast = get_forecast(lat, lon)
    context = {
        'text_index': 'Погода в Вашем городе',
        'text_town': text_town,
        'sign': sign,
        'description': description,
        'name': name,
        'forecast': forecast,
        'weather': {}
    }
    for param, val in weathers_param.items():
        context['weather'][param] = val
    pprint(context)
    return context