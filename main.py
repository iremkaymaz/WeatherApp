import requests
import tkinter
from PIL import ImageTk, Image

api_key = 'YOUR_API_KEY'

window = tkinter.Tk()
window.title("Weather App")
window.minsize(450,500)

img = ImageTk.PhotoImage(Image.open("img.png"))
panel = tkinter.Label(window, image = img)
panel.pack(side = "top", fill = "both")

temp_label = tkinter.Label()
desc_label = tkinter.Label()
error_label = tkinter.Label()

def clear_func():
    temp_label.config(text="")
    desc_label.config(text="")
    error_label.config(text="")

# Enter city name label
city_name_label = tkinter.Label(text="Enter city name: ", font=("Arial", 15))
city_name_label.pack()

# City name Entry

city_name_entry = tkinter.Entry(width=50)
city_name_entry.focus()
city_name_entry.pack()

# OK button

def button_func():
    global api_key
    city_name = city_name_entry.get()
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}")
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        clear_func()
        temp_label.config(text=f'Temperature: {(temp - 272):.0f} C', font=("Arial", 18))
        temp_label.pack()
        desc_label.config(text=f'Description: {desc}', font=("Arial", 18))
        desc_label.pack()

    else:
        clear_func()
        error_label.config(text=f"Error {response.status_code}", font=("Arial", 25))
        error_label.pack()

ok_button = tkinter.Button(text="OK", command=button_func,font=("Arial", 12))
ok_button.pack()

window.mainloop()
