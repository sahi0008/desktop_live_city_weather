import tkinter as tk
from tkinter import messagebox
import requests
import os


# Function to fetch the weather
def get_weather():
    city = city_entry.get().strip()
    
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return
    
    api_key = os.getenv("WEATHER_API_KEY", "df5b9ea81a21a805f4949b1b064ccd8d")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    status_label.config(text="Fetching weather data...", fg="black")
    root.update_idletasks()
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]
            rain = data.get("rain", {})
            
           # Extract weather details
            temperature = main["temp"]
            feels_like = main["feels_like"]
            humidity = main["humidity"]
            description = weather["description"]
            wind_speed = wind["speed"]
            precipitation = rain.get("1h", 0)
            rain_chance = "Likely" if precipitation > 0 else "None"
            

              # Update UI with data
            temperature_label.config(text=f"Temperature🌡: {temperature}°C" , fg="indigo")
            humidity_label.config(text=f"Humidity☁: {humidity}%" , fg="indigo")
            description_label.config(text=f"Description⛅: {description.capitalize()}"  , fg="indigo")
            wind_label.config(text=f"Wind Speed🌪: {wind_speed} m/s" , fg="indigo")
            precipitation_label.config(text=f"Precipitation (last hour)🌬: {precipitation} mm" , fg="indigo")
            rain_chance_label.config(text=f"Chance of Rain☔: {rain_chance}" , fg="indigo")
            
            status_label.config(text="Weather data fetched successfully!", fg="black")
        else:
            messagebox.showerror("Error", data.get("message", "City not found."))
            status_label.config(text="", fg="red")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch data. Check your internet connection.")
        status_label.config(text="", fg="red")


# Create the main window
root = tk.Tk()
root.title(" the Live city Weather ")
root.geometry("500x600")

# Load the background image
try:
    background_image = tk.PhotoImage(file=r"E:\project\background.png")
except Exception as e:
    print(f"Error loading background image: {e}")
    exit()  # Terminate if the image can't be loaded

canvas = tk.Canvas(root, width=500, height=600)
canvas.create_image(0, 0, anchor="nw", image=background_image)
canvas.pack(fill="both", expand=True)

frame = tk.Frame(root, bg="cadetblue", bd=8, relief="ridge")  # Thicker border and ridge style
frame.place(relx=0.5, rely=0.1, anchor="n")

city_label = tk.Label(
    frame, 
    text="Enter City Name🌎:", 
    font=("Comic Sans MS", 16, "bold"),  # Larger and bold font
    bg="#ffffff",  # White background
    fg="#333333"  # Darker text for contrast
)
city_label.grid(row=0, column=0, padx=15, pady=15)

city_entry = tk.Entry(
    frame, 
    width=22, 
    font=("Helvetica", 16, "bold"),  # Bold entry text
    bd=4,  # Border thickness for entry
    relief="sunken"  # Sunken style for input field
)
city_entry.grid(row=0, column=1, padx=15, pady=15)

search_button = tk.Button(
    frame, 
    text="Get Weather", 
    command=get_weather, 
    font=("Helvetica", 14, "bold"),  # Bold and larger button text
    bg="teal",  # teal background
    fg="white",  # White text
    activebackground="teal",  # Darker green on hover
    activeforeground="white"  # White text on hover
)
search_button.grid(row=0, column=2, padx=15, pady=15)



# Weather Data Table Layout
weather_frame = tk.Frame(root, bg="pale green", bd=5)
weather_frame.place(relx=0.5, rely=0.4, anchor="n")

temperature_label = tk.Label(weather_frame, text="Temperature: N/A", font=("Comic Sans MS", 18), bg="thistle")
temperature_label.grid(row=0, column=0, padx=20, pady=10)

humidity_label = tk.Label(weather_frame, text="Humidity: N/A", font=("Comic Sans MS", 18), bg="thistle")
humidity_label.grid(row=1, column=0, padx=20, pady=10)

description_label = tk.Label(weather_frame, text="Description: N/A", font=("Comic Sans MS", 18), bg="thistle")
description_label.grid(row=2, column=0, padx=20, pady=10)

wind_label = tk.Label(weather_frame, text="Wind Speed: N/A", font=("Comic Sans MS",  18), bg="thistle")
wind_label.grid(row=3, column=0, padx=20, pady=10)

precipitation_label = tk.Label(weather_frame, text="Precipitation: N/A", font=("Comic Sans MS", 18), bg="thistle")
precipitation_label.grid(row=4, column=0, padx=20, pady=10)

rain_chance_label = tk.Label(weather_frame, text="Chance of Rain: N/A", font=("Comic Sans MS", 18), bg="thistle")
rain_chance_label.grid(row=5, column=0, padx=20, pady=10)

status_label = tk.Label(root, text="", font=("didot",  14), bg="tan")
status_label.place(relx=0.5, rely=0.9, anchor="center")


root.mainloop()
