import requests
from datetime import datetime
import smtplib
import time
MY_LAT = "YOUR LATITUDE"
MY_LNG = "YOUR LONGITUDE"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
def is_iss_overhead():
    response = requests.get("https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LNG -5 <= iss_longitude <= MY_LNG +5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
        
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
 
while True:  
    time.sleep(60)  
    if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: Look UP\n\nISS is overhead, look up.")