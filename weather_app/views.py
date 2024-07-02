from django.shortcuts import render,redirect
import requests
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    api_key = '33e3129c5e20cc50a11b6839ec2100e2'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request,"{} added succesfully".format(instance.name))
            return redirect('index')
    
    
    cities = City.objects.all()
    weather_list = []
    form = CityForm()
    for i in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={i.name}&units=imperial&appid={api_key}'
        
        response = requests.get(url)
        city_weather = response.json()

        # Debugging: Print the raw response
        print("///////////////", city_weather)

        if response.status_code == 200 and 'main' in city_weather:
            weather = {
                'city': i.name,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon'],
                'id':i.id,
            }
            weather_list.append(weather)
        else:
            print(f"Error fetching data for {i.name}: {city_weather.get('message', 'Unknown error')}")

    # Debugging: Print the final weather list
    print("wwwwwwwwwwwww", weather_list)
    context = {
        "weather_list":weather_list,
        "form":CityForm
    }
    return render(request, 'weather/index.html', locals())



def delete(request,pk):
    try:
        city = City.objects.get(id=pk)
        city.delete()
        messages.error(request,'{} deleted successfully'.format(city.name))
    except City.DoesNotExist:
        messages.warning("City doesnot exist!!")
    return redirect(index)

