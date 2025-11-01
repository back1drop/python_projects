import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

load_dotenv()
api_key = os.getenv("api_key")

def get_weather(city):
    try:
        baseUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(baseUrl)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        # Extract weather data
        main = data['main']
        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        condition = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']

        icon_id = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"

        icon_data = requests.get(icon_url).content
        icon_img = Image.open(BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_img)

        weather_icon_label.config(image=icon_photo)
        weather_icon_label.image = icon_photo

        city_label.config(text=f"📍 {city.capitalize()}")
        temp_label.config(text=f"🌡 Temperature: {temperature}°C (Feels like {feels_like}°C)")
        hum_label.config(text=f"💧 Humidity: {humidity}%")
        cond_label.config(text=f"🌥 Condition: {condition}")
        wind_label.config(text=f"🌬 Wind Speed: {wind_speed} m/s")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_weather():
    city = city_entry.get().strip()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city.")
    else:
        get_weather(city)

# --------GUI Section -----------

root = tk.Tk()
root.title("Weather App")
root.geometry("450x450")
root.config(bg="#e3f2fd")

title = tk.Label(root, text="🌦 Weather Checker", font=("Arial", 20, "bold"), bg="#e3f2fd")
title.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Search", font=("Arial", 14), bg="#1565c0", fg="white", command=search_weather)
search_btn.pack(pady=10)

weather_icon_label = tk.Label(root, bg="#e3f2fd")
weather_icon_label.pack()

city_label = tk.Label(root, font=("Arial", 18, "bold"), bg="#e3f2fd")
city_label.pack(pady=5)

temp_label = tk.Label(root, font=("Arial", 14), bg="#e3f2fd")
temp_label.pack()

hum_label = tk.Label(root, font=("Arial", 14), bg="#e3f2fd")
hum_label.pack()

cond_label = tk.Label(root, font=("Arial", 14), bg="#e3f2fd")
cond_label.pack()

wind_label = tk.Label(root, font=("Arial", 14), bg="#e3f2fd")
wind_label.pack()

root.mainloop()
