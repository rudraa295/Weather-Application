import tkinter as tk
from tkinter import messagebox as ms
from Weather_backend import get_weather as gw

def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        ms.showwarning("Input Error", "Please enter a city name.")
        return

    data = gw(city)

    if data is None:
        result_label.config(text="City not found.")
        return

    result = (
        f"City: {data['city']}, {data['country']}\n"
        f"Temperature: {data['temperature']} °C\n"
        f"Feels Like: {data['feels_like']} °C\n"
        f"Humidity: {data['humidity']}%\n"
        f"Pressure: {data['pressure']} hPa\n"
        f"Wind Speed: {data['wind_speed']} m/s\n"
        f"Condition: {data['condition']}"
    )
    result_label.config(text=result)

root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")

title = tk.Label(root, text="Weather App", font=("Arial", 18))
title.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Get Weather", command=fetch_weather)
search_btn.pack(pady=5)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 11))
result_label.pack(pady=20)

root.mainloop()
