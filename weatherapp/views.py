from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from .weather_service import WeatherApi
import requests
import os
import json
from .forms import CityForm
from .models import City
from .weather_service import get_wetaher

# Create your views here.
@csrf_exempt
def index(request):
    form=CityForm() 
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    all_cities=get_wetaher()
    context={'all_info':all_cities,'form':form}

    return render(request, 'index.html',context)