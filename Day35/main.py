import requests
api_key = "YOUR_API_KEY"
latitude = "YOUR_LATITUDE(INT)"
longitude = "YOUR_LONGITUDE(INT)"
OWM = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4
}
response =requests.get(OWM, params=weather_params)
response.raise_for_status()

waether_data = response.json()
will_rain = False
for hour_data in waether_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        
if will_rain:
    print("Bring an Umbrella")