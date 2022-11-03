import requests
import json
x = requests.get("https://api.openweathermap.org/data/2.5/weather?q=srinagar&appid=e2b9af1dba1fa3144dbd2a57641c79f2")
data = x.json()
weather = (data["weather"][0]["description"])
air_temp = (data["main"]["temp"])
air_pressure = (data["main"]["pressure"])
air_pressure_updated = "{} bars".format(air_pressure)
humidity = (data["main"]["humidity"])
humidity_updated = "{} %".format(humidity)
visibility = (data["visibility"])
air_speed = (data["wind"]["speed"])
air_speed_update = "{} km/hr".format(air_speed)
air_flow_deg = (data["wind"]["deg"])
air_flow_deg_update = "{}°".format(air_flow_deg)
print()





