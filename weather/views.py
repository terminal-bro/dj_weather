from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .weather_api import get_weather
from .serialzers import WeatherSerializer


class WeatherView(APIView):
    def get(self, request, city):

        cached_data = cache.get(city)
        if cached_data:
            serializer = WeatherSerializer(data=cached_data)
            if serializer.is_valid():
                return Response(serializer.data)
            
        weather_data = get_weather(city)
        if weather_data:
                
            processed_data = {
                    'temperature': weather_data['currentConditions']['temp'],
                    'description': weather_data['currentConditions']['conditions'],
                    'humidity': weather_data['currentConditions']['humidity'],
                    'wind_speed': weather_data['currentConditions']['windspeed']
                }

            serializer = WeatherSerializer(data=processed_data)
            if serializer.is_valid():
                cache.set(city, processed_data, timeout=43200)
                return Response(serializer.data)
            
        return Response({"error":"Unable to fetch weather data"}, status=status.HTTP_400_BAD_REQUEST)