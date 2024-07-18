from django.urls import path
from .views import index
from weatherapp.apps import WeatherappConfig
app_name = WeatherappConfig.name
urlpatterns = [

 path('', index,name='index'),
 

]