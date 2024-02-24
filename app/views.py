from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CityWeather
import pandas as pd

@api_view(['GET'])
def DB_Creation(request):
    df = pd.read_csv("IndianWeatherRepository.csv")

    region = df[df['region'] == "Tamil Nadu" ]
    for i in range (0, len(region)):
        city = region.iloc[i]

        data = CityWeather(location_name = city.loc['location_name'],
                           temperature_celsius = city.loc['temperature_celsius'],
                           condition_text = city.loc['condition_text'],
                           humidity = int(city.loc['humidity']),
                           feels_like_celsius = city.loc['feels_like_celsius']
                           )
        data.save()

    return  Response({'message': 'Data added to the database'})

@api_view(['GET'])
def Get_Weather(request,city):
    try:
        city = city.capitalize()
        data = CityWeather.objects.filter(location_name = city).first()
        response = {
            "location_name":data.location_name,
            "temperature_celsius":data.temperature_celsius,
            "condition_text":data.condition_text,
            "humidity":data.humidity,
            "feels_like_celsius" : data.feels_like_celsius
        }
        return Response(response)
    except Exception as e:
        print(e)








