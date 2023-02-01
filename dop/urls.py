from django.urls import path
from dop.views import currency, weather

app_name = 'dop'

urlpatterns = [
    path('currency/', currency, name='currency'),
    path('weather/', weather, name='weather'),
]