from tkinter import Tk                      # importing Tk class from tkinter
from tkinter import Label                   # importing Label class from tkinter
from tkinter import Button
from tkinter import Frame

root = Tk()                                 # creating a basic GUI i.e GUI Window by creating an object of Tk() class

# python logic here

# creating a function to greet user
def hello():
    print('Hello User')

# creating a function to print name
def print_name():
    print('I am a Computer')

# python logic here

# GUI Logic Here
# Everything GUI content will be made here

# giving a title to GUI window
root.title('Frames')

# setting default, min-size and max-size of GUI window
root.geometry('500x500')                    # setting default size of GUI window {format : ('widthxheight')}

# creating a frame to insert all components of GUI
f1 = Frame(root, borderwidth = 10, bg = 'red', relief = 'sunken')
f1.pack()

# creating a label
l1 = Label(f1, text = 'This is a Label', font = 'comicsansms 12 bold', bg='yellow').pack(pady = 10)

# creating a button to greet
button_greet = Button(f1, text = 'Greet Yourselves', bg = '#347284', font = 'comicsansms 12 bold', borderwidth = 5, command = hello).pack(side = 'left', pady = 10, padx = 10)

# creating a button to greet
button_name = Button(f1, text = 'Print Name', bg = '#347284', font = 'comicsansms 12 bold', borderwidth = 5, command = print_name).pack(side = 'left', pady = 10, padx = 10)

# GUI Logic Here
# Everything GUI content will be made here

root.mainloop()             # hold the window on infinite loop