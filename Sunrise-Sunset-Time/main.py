# CONSTANTS 
LAT = 12.971599
LONG = 77.594566


import requests
import datetime

parameters = {
        "lat": LAT,
        "lng": LONG,
        "formatted": 0,
        }

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)

# To fetch sunrise and sunset from the JSON data
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)


time_now = datetime.datetime.now()
print(time_now)

