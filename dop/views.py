from django.shortcuts import render
from django.conf import settings

import requests
from datetime import datetime
from bs4 import BeautifulSoup



URL_BASE_C = "https://myfin.by/currency/minsk"

def currency(request):
    url = URL_BASE_C
    date_html = datetime.now().strftime("%d.%m.%y")
    text = requests.get(url, headers={'User-agent': 'Get the firestarter'}).text
    soup = BeautifulSoup(text, 'html.parser')
    parser_all = soup.find_all('td')
    dollar_buy = parser_all[1].text.replace('\n', '')
    dollar_sale = parser_all[2].text.replace('\n', '')
    dollar_nb = parser_all[3].text.replace('\n', '')
    euro_buy = parser_all[6].text.replace('\n', '')
    euro_sale = parser_all[7].text.replace('\n', '')
    euro_nb =parser_all[8].text.replace('\n', '')
    zloty_buy = parser_all[16].text.replace('\n', '')
    zloty_sale = parser_all[17].text.replace('\n', '')
    zloty_nb = parser_all[18].text.replace('\n', '')
    context = {'title': 'i Creame Currency',
        'dollar_nb': dollar_nb, 'euro_nb': euro_nb,
               'zloty_nb': zloty_nb, 'date_html': date_html,
               'dollar_buy': dollar_buy, 'dollar_sale': dollar_sale,
               'euro_buy': euro_buy, 'euro_sale': euro_sale,
               'zloty_buy': zloty_buy, 'zloty_sale': zloty_sale,
               }
    return render(request, 'dop/currency.html', context)


APPID = settings.WEATHER_API
URL_BASE_W = "http://api.openweathermap.org/data/2.5/weather"

def weather(request):

    APP = APPID
    URL_W =URL_BASE_W

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Amsterdam'

    param = {'q':city, 'appid':APP, 'units':'metric'}
    r = requests.get(url=URL_W, params=param).json()
    description = r['weather'][0]['description']
    icon = r['weather'][0]['icon']
    city = r['name']
    temp = r['main']['temp']
    wind = r['wind']['speed']
    pressure = int((r['main']['pressure']) * 0.75)
    humidity = r['main']['humidity']
    day = datetime.now().strftime("%d-%m-%Y")

    context = { 'title': 'iCreame Weather','icon':icon, 'description': description, 'city': city,
               'temp': temp, 'wind': wind, 'pressure': pressure, 'humidity': humidity, 'day': day}
    return render(request, 'dop/weather.html', context)
