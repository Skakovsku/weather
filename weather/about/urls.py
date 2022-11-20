from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path(
        'author/<str:town>/',
        views.AboutAuthorView.as_view(),
        name='author'),
]