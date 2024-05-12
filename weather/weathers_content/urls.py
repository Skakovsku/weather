from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
    path(
        '.well-known/acme-challenge/KtVZ8CVDOM8OxBC2kPOg-raizbLmV-H0C05cmR6zYhg/',
        views.cert,
        name='cert'),
    path(
        'add-town/<str:text>/<str:town_current>/',
        views.add_town,
        name='add_town'),
    path(
        'town/<str:town>/<str:day>/',
        views.for_day,
        name='for_day'),
    path('town/<str:town>/', views.town, name='town'),
    path('goro/<str:town>/', views.goro, name='goro'),
    path('', views.index, name='index')
]
