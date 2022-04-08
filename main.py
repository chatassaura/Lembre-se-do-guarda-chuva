import requests
from twilio.rest import Client
import datetime as dt

hour_now = int(dt.datetime.now().hour)
account_sid = "ACaee5b120663e1475d2ae1e801ec96118"
auth_token = "6d9ce7719aa1772f2328509f5e0c5c7d"
MY_LNG = -46.5867
MY_LAT = -23.3186
api_key = #SUA API KEY - GERADA NO SITE

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][hour_now:hour_now + 12]

will_rain = False

for hour in weather_slice:
    conditional_code = hour["weather"][0]["id"]
    if conditional_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_="+18647782757",
        to=#YOUR NUMBER PHONE / SEU NUMERO DE TELEFONE
    )
    print(message.status)

