import requests
import os


API_KEY = os.environ.get('WEATHER_API_KEY')
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"


def get_weather(city):
    url = f"{BASE_URL}/{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None