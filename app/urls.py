from django.urls import path
from .views import DB_Creation,Get_Weather

urlpatterns = [
    path('create_db/',DB_Creation,name='create_db'),
    path('get_weather/<str:city>',Get_Weather,name='get_weather')
]