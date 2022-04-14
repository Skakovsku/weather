import time
import requests
from . import const

weathers_data = {}

def get_weathers_data(data):
    for elem in data:
        if type(data[elem]) is dict:
            get_weathers_data(data[elem])
        elif type(data[elem]) == list:
            get_weathers_data(data[elem][0])
        elif elem in const.WEATHER_DATA:
            if type(data[elem]) == float:
                if data[elem] >= 1 and elem == 'temp':
                    val = '+' + str(int(data[elem]))
                elif data[elem] >= 1 and elem == 'feels_like':
                    val = '+' + str(int(data[elem]))
                else:
                    val = int(data[elem])
                weathers_data[const.WEATHER_DATA[elem]] = val
            else:
                weathers_data[const.WEATHER_DATA[elem]] = data[elem]
    return weathers_data


def get_forecast_5_days(lat, lon):
    coord = str(lat) + '&lon=' + str(lon)
    response = requests.get(const.API_FOR_1 + coord + const.API_FOR_2)
    data_for = response.json()
    forecast = {}
    forecast_param = {}
    for time_for in data_for['list']:
        if (time_for['dt'] + const.HALF_DAY) % const.DAY == 0:
            temp = int(time_for['main']['temp'])
            if temp >= 1:
                temp = '+' + str(temp)
            forecast_param['temp'] = temp
            title = time_for['weather'][0]
            forecast_param['description'] = title['description']
            sign = const.SIGN_BEGIN + title['icon'] + const.SIGN_END
            forecast_param['sign'] = sign
            forecast[time_for['dt_txt']] = forecast_param
        forecast_param = {}
    return forecast


def get_forecast_day(lat, lon, day):
    coord = str(lat) + '&lon=' + str(lon)
    response = requests.get(const.API_FOR_1 + coord + const.API_FOR_2)
    data_request = response.json()
    data = {}
    time_day, temperature = ['Местное время'], ['Температура, °C']
    feels_like, press = ['Ощущается как, °C'], ['Атмосферное давление, Гпа:']
    humidity, clouds = ['Влажность воздуха, %:'], ['Oблачность, %:']
    speed, gust = ['Скорость ветра, м/с:'], ['Порывы до, м/с']
    deg, weather = ['Направление:'], ['Характер погоды:']
    for for_date in data_request['list']:
        if day in for_date['dt_txt']:
            data[for_date['dt_txt']] = for_date
    for time_forecast, param in data.items():
        day_for_struct = time.strptime(time_forecast, "%Y-%m-%d %H:%M:%S")
        time_day.append(time.strftime('%H:%M', day_for_struct))
        data_day = time.strftime('%d.%m.%Y', day_for_struct)
        temp = int(param['main']['temp'])
        if temp >= 1:
            temp = '+' + str(int(param['main']['temp']))
        temperature.append(temp)
        feels = int(param['main']['feels_like'])
        if feels >= 1:
            feels = '+' + str(int(param['main']['temp']))
        feels_like.append(feels)
        press.append(param['main']['pressure'])
        humidity.append(param['main']['humidity'])
        clouds.append(param['clouds']['all'])
        speed.append(int(param['wind']['speed']))
        gust.append(int(param['wind']['gust']))
        if 'deg' in param['wind']:
            deg_param = int(param['wind']['deg'])
            for win in const.WIND_DEG:
                if const.WIND_DEG[win][0] <= deg_param <= const.WIND_DEG[win][1]:
                    deg.append(win)
                    break
        else:
            deg.append('Нет данных')
        sign = const.SIGN_BEGIN + param['weather'][0]['icon'] + const.SIGN_END
        weather.append(sign)
    context = [temperature, feels_like, press, humidity, clouds, speed, gust,
               deg]
    return context, time_day, weather, data_day


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
    time_request = data['dt'] + data['timezone']
    date_request = time.gmtime(time_request)
    date_updated = time.strftime("Обновлено %H:%M %d.%m.%Y", date_request)
    sign = const.SIGN_BEGIN + data['weather'][0]['icon'] + const.SIGN_END
    description = data['weather'][0]['description']
    name = data['name']
    lat, lon = data['coord']['lat'], data['coord']['lon']
    forecast = get_forecast_5_days(lat, lon)
    context = {
        'text_index': const.TEXT_INDEX,
        'lat': lat,
        'lon': lon,
        'text_town': text_town,
        'sign': sign,
        'description': description,
        'name': name,
        'time_update': date_updated,
        'forecast': forecast,
        'weather': {}
    }
    for param, val in weathers_param.items():
        context['weather'][param] = val
    return context
