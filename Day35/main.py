import requests

lat = 36.779411168
lon = -76.535579828
api_key = "GETAPIKEYFROMOPENWEATHERMAP"
url = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    'lat': lat,
    'lon': lon,
    'exclude': "current,minutely,daily",
    'appid': api_key
}

response = requests.get(url, params=parameters)
response.raise_for_status()

weather_data = response.json()

#print(weather_data['hourly'][0]['weather'][0]['id'])

need_umbrella = False

weather_slice = weather_data['hourly'][:12]

for hour_data in weather_slice:
    # if weather id is < 700 you will likely need an umbrella
    if int(hour_data['weather'][0]['id']) < 700:
        need_umbrella = True

if need_umbrella:
    print("You will need an umbrella")
else:
    print("No umbrella needed.")




