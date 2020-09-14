from tkinter import *

root = Tk()

root.geometry('500x300')
root.title('Hello Guys')
root.wm_iconbitmap('1.ico')                     # setting the icon of GUI Window

# function to close the output window
Button(text = 'Close', command = root.destroy).pack()

root.mainloop()