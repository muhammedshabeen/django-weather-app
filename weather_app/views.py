from django.shortcuts import render
import requests

def index(request):
    weather = None
    api_key = '33e3129c5e20cc50a11b6839ec2100e2'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format('Kozhikode',api_key)
    
    city_weather = requests.get(url).json() #request the API data and convert the JSON to Python data types
    weather = {
        'city' : 'Kozhikode',
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }    
    return render(request, 'weather/index.html',locals()) #returns the index.html template