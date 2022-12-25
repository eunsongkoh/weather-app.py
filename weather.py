from tkinter import *
import json as j
import requests as r 

# ---------------- Initializing Window and Setup ------------------------------ 
window = Tk()
window.geometry("500x500")
window.title('Weather App 1.0')
background = PhotoImage(file = "<background_photo>.png")
bg = Label(window, image=background)
bg.pack()
window.resizable(0,0)

# City value 
city = StringVar()

def theWeather():
    city_name = city.get()
    # ---------------- Setting up the API ---------------
    apiKey = "<api_key>"
    url = "https://api.openweathermap.org/data/2.5/weather?" + 'appid=' + apiKey + "&q=" + city_name

    # Returns the response 
    response = r.get(url)

    # Clears the output in the text box for each entry 
    tInsert.delete("1.0", "end")

    # converts data 
    converted = response.json()

    # if the city is found 
    if converted["cod"] == 200:
        kelvin = 273

        # temperature 
        temperature = int(converted['main']['temp'] - kelvin)

        # feels like temperature
        feels = int(converted["main"]["feels_like"] - kelvin)

        # description of the weather 
        descrip = converted["weather"][0]["description"]

        weather = f"The Current Weather of {city_name}\n\nTemperature: {temperature}°C\nFeels Like: {feels}°C\nDescription: {descrip}"
    else: 
        weather = f"\nCity Not Found!"
    
    tInsert.insert(INSERT, weather)
        
# ---------------- UI ------------------------------ 
# default font 
fontDefault = ("lucida", 10, "bold italic")
fontWeather = ("lucida", 10, "italic")
placeFont = ("lucida", 8, "italic")

place = Label(text="Enter Your Location", font = fontDefault).place(x=198,y=10)
place_entry = Entry(width=30, textvariable=city, font = placeFont).place(x=170, y=40)

place_submit = Button(text="Go", width=8, command=theWeather, font = fontDefault).place(x=223, y=80)
weather = Label(text="Current Weather", font = fontDefault).place(x=205, y=170)

tInsert = Text(font = fontWeather, width=38, height=10)
tInsert.place(x=130, y=200)

	
# Executing the Window 
window.mainloop()
