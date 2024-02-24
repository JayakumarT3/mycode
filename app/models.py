from django.db import models

class CityWeather(models.Model):
    location_name = models.CharField(max_length=100)
    temperature_celsius = models.FloatField()
    humidity = models.IntegerField()
    condition_text = models.CharField(max_length=100)
    feels_like_celsius = models.FloatField()





