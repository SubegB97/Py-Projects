# tkinter is a GUI development toolkit 
import tkinter as tk 
# filedialog will help pick the apps, text will display text
from tkinter import filedialog, Text
# Allow us to run apps for this application
import os 

# root is the html body, this will hold the whole app structure
root = tk.Tk()
# apps is a variable assigned to an empty list that will be appended
apps = []

# if the os.path is save.txt, we open save.txt as f 
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        # tempApps is a variable set to f.read() which returns a string 
        tempApps = f.read()
        # this converts and splits the apps by a comma into an array 
        tempApps = tempApps.split(',')
        # strip out empty spaces 
        apps = [x for x in tempApps if x.strip()]

# This function will open up a file directory where we can select apps to add for opening
# inital directory is the start directory, file types are executable files and all other files 1
def addApp(): 
    # the widget gives us access to everything in the frame
    for widget in frame.winfo_children():
        # Destroys everything before appending the new updated list of apps
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*")))

    # List of files selected are appended to the apps variable
    apps.append(filename)
    # prints file location of app to the console
    print(filename)

    # loop that will create a label for selected app in the frame box
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# function that will run the selected apps when run apps is clicked
def runApps():
    # for loop 
    for app in apps:
        # acts as if its double clicking selected applictions 
        os.startfile(app)

# canvas is used to make the GUI bigger, change background color, takes the root as an parameter
canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
#This attaches the canvas changes to the root 
canvas.pack()

# Creates another frame inside the canvas container 
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Creates an Open File button on the root and it has padding, white foreground and green bg
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

# Creates a Run App button on the root and it has padding, white foreground and green bg
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# Keeps app list on the screen
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
# To make the GUI run 
root.mainloop()

# Whenvever the GUI is closed, saves the text file and that file is written as f
# and with f we can write all the apps saved. 
with open('save.txt', 'w') as f:
    # looping over the apps again
    for app in apps:
        f.write(app + ',')