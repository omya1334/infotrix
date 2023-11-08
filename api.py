import tkinter as tk
from datetime import datetime
from tkinter import *
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
from tkinter import messagebox


geolocator = Nominatim(user_agent="geopyExercises")

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def add_city():
    city = favtext.get()
    if city:
        listbox.insert(tk.END, city)
        favtext.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

def remove_city():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Selection Error", "Please select a city to remove.")


def get_weather():
    city = textfield.get()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=Enter API Key"

    try:
        json_data = requests.get(api).json()

        if json_data.get('weather'):
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            condition_label.config(text=f"Condition: {condition}")
            description_label.config(text=f"Description: {description}")
            temp_label.config(text=f"Temperature: {temp}°C")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind} m/s")
        else:
            print("Error: Weather data not found in JSON response")

    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

    print(json_data)

textfield = tk.Entry(root, justify="center", width=18, font=("popins", 25, "bold"),bg="#404040", border=0, fg="white")
textfield.place(x=20, y=40)
textfield.focus()

search_icon = PhotoImage(file="searchbtn.png")
search_button = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=get_weather)
search_button.place(x=335, y=40)

#favourite city
fav = Label(text="Your Favourite City:", font=("Helvetica", 15, 'bold'),fg="purple")
fav.place(x=375,y=50)

#fav city entry
favtext = tk.Entry(root, justify="center", width=18, font=("popins", 25, "bold"),bg="#404040", border=0, fg="white")
favtext.place(x=570, y=40)
favtext.focus()

# Create a button to add a city
add_button = tk.Button(text="Add City", command=add_city)
add_button.place(x=650,y=100)

# Create a button to remove a city
remove_button = tk.Button(text="Remove City", command=remove_city)
remove_button.place(x=750,y=100)

# Create a listbox to display favorite cities
listbox = tk.Listbox(root, width=50)
listbox.place(x=580,y=150)

#logo
logo_img = PhotoImage(file="android-chrome-192x192.png")
logo = Label(image=logo_img)
logo.place(x=310, y=100)

clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


condition_label = Label(root, font=("Helvetica", 15, 'bold'),bg="#BA55D3")
condition_label.place(x=30, y=160)

description_label = Label(root, font=("Helvetica", 15, 'bold'),bg="#FF0000")
description_label.place(x=30, y=190)

temp_label = Label(root, font=("Helvetica", 15, 'bold'),bg="#3A5FCD")
temp_label.place(x=30, y=220)

pressure_label = Label(root, font=("Helvetica", 15, 'bold'),bg="#54FF9F")
pressure_label.place(x=30, y=250)

humidity_label = Label(root, font=("Helvetica", 15, 'bold'),bg="#836FFF")
humidity_label.place(x=30, y=280)

wind_label = Label(root, font=("Helvetica", 15, 'bold'),bg="#EE3A8C")
wind_label.place(x=30, y=310)

root.mainloop()