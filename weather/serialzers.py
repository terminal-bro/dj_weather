from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    description = serializers.CharField()
    humidity = serializers.FloatField()
    wind_speed = serializers.FloatField()

    