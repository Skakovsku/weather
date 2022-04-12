from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('add-town/<str:text>/', views.add_town, name='add_town'),
    path(
        'town/<str:town>/<str:day>/<str:lat>/<str:lon>/',
        views.for_day,
        name='for_day'),
    path('town/<str:town>/', views.town, name='town'),
    path('', views.index, name='index')
]
