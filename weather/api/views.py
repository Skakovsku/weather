import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from weathers_content import const


@api_view(['GET'])
def weather(request, town):
    response = requests.get(const.API_WEATHER_1 + town + const.API_WEATHER_2)
    data = response.json()
    return Response(data)
