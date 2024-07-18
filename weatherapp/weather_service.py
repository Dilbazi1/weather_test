import requests
from .models import City

def get_wetaher():
    weather_icon = {
        "Sunny": "\U00002600",
        "Clear":"\U00002600",
        "Clouds": "\U00002601",
        'Partly Cloudy':"\U00002601",
        'Partly cloudy':"\U00002601",
        "Rain": "\U00002614",
        "Drizzle": "\U00002614",
        "Thunderstorm": "\U000026A1",
        "Snow": "\U0001F328",
        "Mist": "\U0001F32B",
        "Fog": "",
        "Haze": "",
    }
    cities=City.objects.all()
    all_cities=[]
    for city in cities:
        url=f'http://api.weatherapi.com/v1/current.json?key=6cb5546d877f4cb3955144028241807&q={city.name}&aqi=no'
        res = requests.get(url)
        res=res.json()
        print(res)
        city_info={
            'city':city.name,
            'temp':res["current"]["temp_c"],
            'icon':res['current']['condition']['icon'],
        
            'icon':weather_icon[res['current']['condition']['text']]
        } 
        all_cities.append(city_info)
        
    return all_cities
