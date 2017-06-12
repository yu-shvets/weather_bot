import urllib.request
import json
from cities import city_list

API_KEY = '50227a41393f890c497f3b019385a950'
URL_API = "http://api.openweathermap.org/data/2.5/weather?q="
UNIT = 'metric'


def day_forecast(city):

    if city not in city_list:
        return 'Incorrect name or information unavailable.'

    else:
        url = URL_API + city + '&mode=json&units=' + UNIT + '&APPID=' + API_KEY

        request = urllib.request.Request(url)

        response = urllib.request.urlopen(request)

        data = json.loads(response.read().decode('utf-8'))

        weather = data['weather'][0]['description']
        temp = data['main']['temp']

        current = str(temp) + '°,' + ' ' + weather

        return current
