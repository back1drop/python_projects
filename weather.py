import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("api_key")

def get_weather(city):
    baseUrl=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(baseUrl)
    if response.status_code==200:
        data=response.json()
        field=data['main']
        weather={
            "City":city,
            "Temperature":f"{field['temp']} C",
            "Humidity":f"{field['humidity']}%",
            "Condition":data['weather'][0]['description']
        }
        for x in weather:
            print(f"{x}: {weather[x]}")
        
    else:
        print("Error fetching Weather data:", data.get("message"))

city=input("Enter a city: ").strip()
get_weather(city)

