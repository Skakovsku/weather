from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path(
        'author/<str:town>/',
        views.AboutAuthorView.as_view(),
        name='author'),
    path('message/<str:town>/', views.message, name='message'),
    path('sended/<str:town>/', views.message_sended, name='message_sended'),
]
