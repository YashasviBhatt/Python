from tkinter import Tk                      # importing Tk class from tkinter
from tkinter import Label                   # importing Label class from tkinter
from PIL import Image, ImageTk              # importing Image and ImageTk classes from PIL to manage images

root = Tk()                                 # creating a basic GUI i.e GUI Window by creating an object of Tk() class

# GUI Logic Here
# Everything GUI content will be made here

# giving a title to GUI window
root.title('Learning Tkinter')

# setting default, min-size and max-size of GUI window
root.geometry('500x500')                    # setting default size of GUI window {format : ('widthxheight')}
root.minsize(400, 400)                       # setting minimum size of GUI window {format : (width, height)}
root.maxsize(700, 700)                       # setting maximum size of GUI window {format : (width, height)}

# creating label to insert text
label_text = Label(text = 'Hello this is my first program using tkinter').pack()

# creating label to add image as background
img = Image.open('../geeks.jpg')            # opening image
imge = ImageTk.PhotoImage(img)              # displaying the opened image
label_image = Label(image = imge).pack()    # defining the place on which image will be displayed in tkinter GUI

# creating label to apply different attribute of Label
label_text_2 = Label(text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
''', bg = '#FF9933', fg = '#138808', padx = 30, pady = 30, font = 'comicsansms 10 bold', borderwidth = 5, relief = 'sunken').pack()

# creating label to appply different attribute of pack
label_text_3 = Label(text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
''', bg = 'red').pack(side = 'left', fill = 'y', padx = 20, pady = 20)

# GUI Logic Here
# Everything GUI content will be made here

root.mainloop()             # hold the window on infinite loop