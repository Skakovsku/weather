import time
from django.shortcuts import render, redirect

from . import const, get_ip, get_town, get_wether
from .get_user_info import get_user_info
from .forms import TownForm
from pprint import pprint

def index(request):
    user_ip = get_ip.get_client_ip(request)
    town = get_town.get_town(user_ip)
    get_user_info(request, 'index', town)
    template = 'weathers_content/index.html'
    context = get_wether.get_weather('index', town)
    pprint(context)
    return render(request, template, context)

def add_town(request, text, town_current):
    """Setting up the town name."""
    if text == 'main':
        text_town = None
    elif text == 'auxiliary':
        text_town = const.SPEC_CITY
    form = TownForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        town = form.cleaned_data['town']
        return redirect('weather:town', town)
    get_user_info(request, 'add_town', text)
    town_list = []
    file = open('/home/eugenus/dev/weather/weather/weathers_content/db_town.txt', 'r')
    for town_str in range(1363):
        town_current = file.readline().strip()
        if town_current != '':
            town_list.append(town_current)
    file.close()
    template = 'weathers_content/town.html'
    form = TownForm()
    context = {
        'text_index': const.TEXT_INDEX,
        'form': form,
        'text_town': text_town,
        'town_list': town_list,
        'name': town_current,
    }
    return render(request, template, context)

def town(request, town):
    get_user_info(request, 'town', town)
    template = 'weathers_content/index.html'
    context = get_wether.get_weather('town', town)
    if context == {'cod': 'error'}:
        return redirect('weather:add_town', text='auxiliary')
    return render(request, template, context)

def for_day(request, town, day):
    get_user_info(request, 'for_day', town)
    template = 'weathers_content/forecast.html'
    day_for_struct = time.strptime(day, "%Y-%m-%d %H:%M:%S")
    day_for = time.strftime('%Y-%m-%d', day_for_struct)
    other = get_wether.get_forecast_day(
        town, day_for)
    context = {
        'name': town,
        'day': day_for,
        'for_data': other[0],
        'time_day': other[1],
        'weather': other[2],
        'data_day': other[3],
        'day_one': other[4],
        'temp': other[5]
    }
    return render(request, template, context)

def goro(request, town):
    get_user_info(request, 'goro', town)
    template = 'weathers_content/goro.html'
    list_link = const.LIST_LINK_GORO
    context = {
        'list_link': list_link,
        'text_index': 'Гороскоп от ЗэВэЗэ',
        'goro': True,
        'name': town,
    }
    return render(request, template, context)
