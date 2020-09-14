from tkinter import Tk                      # importing Tk class from tkinter
from tkinter import Label                   # importing Label class from tkinter
from tkinter import Frame                   # importing Frame class from tkinter

root = Tk()                                 # creating a basic GUI i.e GUI Window by creating an object of Tk() class

# GUI Logic Here
# Everything GUI content will be made here

# giving a title to GUI window
root.title('Frames')

# setting default, min-size and max-size of GUI window
root.geometry('500x500')                    # setting default size of GUI window {format : ('widthxheight')}

# creating a frame for left window of GUI
f_left = Frame(root, borderwidth = 10, bg = 'red', relief = 'sunken')
f_left.pack(side = 'left', fill = 'y')
label_1 = Label(f_left, text = 'This is the left window', font = 'comicsansms 12 bold', bg='yellow').pack(pady = 325)

# creating a frame for top window of GUI
f_top = Frame(root, borderwidth = 10, bg = 'green', relief = 'sunken')
f_top.pack(side = 'top', fill = 'x')
label_2 = Label(f_top, text = 'This is the top window', font = 'comicsansms 12 bold', bg='yellow').pack(padx = 450)

# creating a frame for center window of GUI
f_mid_1 = Frame(root, borderwidth = 10, bg = 'blue', relief = 'sunken')
f_mid_1.pack(side = 'left', fill = 'y')
label_3 = Label(f_mid_1, text = 'This is the centre window', font = 'comicsansms 12 bold', bg='yellow').pack(padx = 190, pady = 280)

# creating a frame for right window of GUI
f_mid_2 = Frame(root, borderwidth = 10, bg = 'black', relief = 'sunken')
f_mid_2.pack(side = 'left', fill = 'y')
label_4 = Label(f_mid_2, text = 'This is the right window', font = 'comicsansms 12 bold', bg='yellow').pack(padx = 190, pady = 280)

# GUI Logic Here
# Everything GUI content will be made here

root.mainloop()             # hold the window on infinite loop