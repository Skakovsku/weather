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
        'form': form,
        'text_town': text_town,
    }
    return render(request, template, context)

def town(request, town):
    template = 'weathers_content/index.html'
    context = get_wether.get_weather('town', town)
    if context['data']['cod'] == '404':
        return redirect('weather:add_town', text='auxiliary')
    return render(request, template, context)
