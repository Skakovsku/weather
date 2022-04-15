from pprint import pprint
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

def for_day(request, town, day):
    template = 'weathers_content/forecast.html'
    day_for_struct = time.strptime(day, "%Y-%m-%d %H:%M:%S")
    day_for = time.strftime('%Y-%m-%d', day_for_struct)
    other = get_wether.get_forecast_day(
        town, day_for)
    context = {
        'town': town,
        'day': day_for,
        'for_data': other[0],
        'time_day': other[1],
        'weather': other[2],
        'data_day': other[3],
        'day_one': other[4]
    }
    pprint(context)
    return render(request, template, context)
