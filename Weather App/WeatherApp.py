import tkinter as tk 
from tkinter import font
import requests

# Global Variables
HEIGHT = 500
WIDTH = 600

# Function that prints entry in console when a city is entered 
def test_function(entry):
    print("This is the entry:", entry)

def format_response(weather):
    # try to find the properties that were passed in
    try:
        # In the JSON, name is not nested, so its just a Key 
        name = (weather['name'])
        # Key into weather since its a dictionary, get the first entry which is 0th, then description
        desc = (weather['weather'][0]['description'])
        # Key into main and then temp, not a list so just add the name temp in brackets 
        temp = (weather['main']['temp'])
        # Final string in notation of %s is place holder for string, \n is newline and then pass in string value with % with the actual variables
        final_str = 'City: %s \nConidtions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str
# Function that gets the weather using OPEN WEATHER MAP API
def get_weather(city):
    # API KEY
    weather_key = 'bca68f5db046d2e61c34df460d6b198b'
    # URL FOR OPENWEATHERMAP
    url = 'http://api.openweathermap.org/data/2.5/weather'  
    # PARAMETERS required in a dictionary                                                                                                                                                                                                                                                                                              
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    # response returns the url and the params dictionary 
    response = requests.get(url, params=params)
    # weather variable assigned to the json response file retrieved by API
    weather = response.json()

    # label and text property of label, allows the text to show up in the label 
    label['text'] = format_response(weather)


# API KEY bca68f5db046d2e61c34df460d6b198b
# API LINK api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# This is the root window to tkinter (Root is the parent)
root = tk.Tk()

# This is another window that will be inside the root window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Variable that is assigned to the tkinter photo image which lets us use images 
background_image = tk.PhotoImage(file='landscape.png')
# background label is set to a label where the root is the parent and the image is put on the root
background_label = tk.Label(root, image=background_image)
# image is placed on the root 
background_label.place(relwidth=1, relheight=1)
# This is will organize the widgets on the screen
frame = tk.Frame(root, bg='#80C1FF', bd=5)
# This sets the frame up on the screen along with the relative width/ height and relx/y which centers the frame
# Great to resize the screen without messing it up
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Entry box where you can type into it
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

# First button and its placed in the frame window (Text, bg are keyword argument or kwarg)
# lambda is an inline function used temporarily in memory
button = tk.Button(frame, text="Show Weather", font=('Times New Roman', 12), command=lambda: get_weather(entry.get()))
# Makes the actual button show up in the window
# Side can move button left, right or center
# Fill fills the parent (frame) with the entire button 
# Expand makes the button bigger and fill more of the screen
# Grid makes alignment easier for the buttons, labels or entry boxes
# Place is more flexible and put things exactly where you want
button.place(relx=0.7, relwidth=.30, relheight=1)

# Lower Frame which will display the weather results for city 
lower_frame = tk.Frame(root, bg='#80C1FF', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Label that is inside the lower frame
label = tk.Label(lower_frame, font=('Arial', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

print(tk.font.families())

# This runs the application 
root.mainloop()