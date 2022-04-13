import time
from django.shortcuts import render, redirect

from . import const, get_ip, get_town, get_wether
from .forms import TownForm

def index(request):
    user_ip = get_ip.get_client_ip(request)
    town = get_town.get_town(user_ip)
    template = 'weathers_content/index.html'
    context = get_wether.get_weather('index', town)
    return render(request, template, context)

def add_town(request, text):
    if text == 'main':
        text_town = None
    elif text == 'auxiliary':
        text_town = const.SPEC_CITY
    form = TownForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        town = form.cleaned_data['town']
        return redirect('weather:town', town)
    template = 'weathers_content/town.html'
    form = TownForm()
    context = {
        'text_index': const.TEXT_INDEX,
        'form': form,
        'text_town': text_town,
    }
    return render(request, template, context)

def town(request, town):
    template = 'weathers_content/index.html'
    context = get_wether.get_weather('town', town)
    if context == {'cod': 'error'}:
        return redirect('weather:add_town', text='auxiliary')
    return render(request, template, context)

def for_day(request, town, day, lat, lon):
    template = 'weathers_content/forecast.html'
    day_for_struct = time.strptime(day, "%Y-%m-%d %H:%M:%S")
    day_for = time.strftime('%Y-%m-%d', day_for_struct)
    data_day_for, time_day, weather, data_day = get_wether.get_forecast_day(
        lat, lon, day_for)
    context = {
        'town': town,
        'day': day_for,
        'for_data': data_day_for,
        'time_day': time_day,
        'weather': weather,
        'data_day': data_day
    }
    return render(request, template, context)
