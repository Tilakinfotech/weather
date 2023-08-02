import tkinter as tk

def get_weather():
    city = city_entry.get()
    # Replace this with your API call to fetch real weather data
    weather_data = {
        "main": "Cloudy",
        "description": "Overcast clouds",
        "temperature": "25°C",
        "humidity": "70%",
        "wind_speed": "5 m/s"
    }
    display_weather(weather_data)

def display_weather(weather_data):
    weather_label.config(text=f"Weather: {weather_data['main']}")
    description_label.config(text=f"Description: {weather_data['description']}")
    temperature_label.config(text=f"Temperature: {weather_data['temperature']}")
    humidity_label.config(text=f"Humidity: {weather_data['humidity']}")
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind_speed']}")

# GUI setup
root = tk.Tk()
root.title('Weather Forecast')

city_label = tk.Label(root, text='Enter City:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text='Weather: ')
weather_label.pack()

description_label = tk.Label(root, text='Description: ')
description_label.pack()

temperature_label = tk.Label(root, text='Temperature: ')
temperature_label.pack()

humidity_label = tk.Label(root, text='Humidity: ')
humidity_label.pack()

wind_speed_label = tk.Label(root, text='Wind Speed: ')
wind_speed_label.pack()

root.mainloop()
