from tkinter import *

class GUI(Tk):
    def __init__(self):                             # creating a constructor for GUI setup
        super().__init__()                            # calling super class(Tk) constructor to provide functionality
        self.geometry('400x200')

    # creating function for status var
    def status(self):
        self.statusvar = StringVar()
        self.statusvar.set('Ready')
        self.statusbar = Label(self, textvariable = self.statusvar, relief = 'sunken', anchor = 'w').pack(side = 'bottom', fill = 'x')

    # creating function for Button
    def button(self, inptext, function):
        Button(text = inptext, command = function).pack()

    def updateStatus(self):
        self.statusvar.set('Ready Now')

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.button('Update Status', window.updateStatus)
    window.mainloop()