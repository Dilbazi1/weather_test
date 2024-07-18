from django.test import TestCase
import requests
class TestProject(TestCase):
    def test_get_city(self):
        url='http://api.weatherapi.com/v1/current.json?key=6cb5546d877f4cb3955144028241807&q=london&aqi=no'
        response = requests.get(url)
        response=response.json()
        city=response['location']['name']
        self.assertEqual(city, 'London')
    
