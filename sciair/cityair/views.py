from django.shortcuts import render,HttpResponse
from  django.contrib import messages
from cityair.models import City
from datetime import datetime
import requests
import json
def index(request):
    context = {
        "aqi": "N/A",
        "geo_loc": "N/A",
        "loc": "N/A",
        "weather": "N/A",
        "air_temp": "N/A",
        "air_pressure_updated": "N/A",
        "humidity_updated": "N/A",
        "visibility": "N/A",
        "air_speed_updated": "N/A",
        "air_flow_deg_updated": "N/A"
    }
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if request.method == "POST":
        city = request.POST.get("city")
        loc = city
        print(loc)
        if loc == "null":
            context = {
                "aqi": "N/A",
                "geo_loc": "N/A",
                "loc": "N/A",
                "weather": "N/A",
                "air_temp": "N/A",
                "air_pressure_updated": "N/A",
                "humidity_updated": "N/A",
                "visibility": "N/A",
                "air_speed_updated": "N/A",
                "air_flow_deg_updated": "N/A"
            }
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            city = City(ip=ip, city=city, date=datetime.today(), time=current_time)
            city.save()
        else:
            api_key1 = "e2b9af1dba1fa3144dbd2a57641c79f2"
            api_key2 = "0b9c885301f9cf107e53efd85c818ba6af99b23e"
            x = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(loc, api_key1))
            data = x.json()
            y = requests.get("http://api.waqi.info/feed/{}/?token={}".format(loc, api_key2))
            data_aqi = y.json()
            geo_loc = (data_aqi["data"]["city"]["geo"])
            aqi = (data_aqi["data"]["aqi"])
            weather = (data["weather"][0]["description"])
            air_temp = (data["main"]["temp"])
            air_pressure = (data["main"]["pressure"])
            air_pressure_updated = "{} mbars".format(air_pressure)
            humidity = (data["main"]["humidity"])
            humidity_updated = "{}%".format(humidity)
            visibility = (data["visibility"])
            air_speed = (data["wind"]["speed"])
            air_speed_updated = "{} km/hr".format(air_speed)
            air_flow_deg = (data["wind"]["deg"])
            air_flow_deg_updated = "{}°".format(air_flow_deg)
            context = {
                "aqi": aqi,
                "geo_loc": geo_loc,
                "loc": loc,
                "weather": weather,
                "air_temp": air_temp,
                "air_pressure_updated":  air_pressure_updated,
                "humidity_updated":   humidity_updated,
                "visibility":  visibility,
                "air_speed_updated":  air_speed_updated,
                "air_flow_deg_updated":  air_flow_deg_updated
            }
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            city = City(ip=ip, city=city, date=datetime.today(), time=current_time)
            city.save()
            messages.success(request, 'scroll down for your search result !')
    return render(request, "index.html", context)

