from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
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
