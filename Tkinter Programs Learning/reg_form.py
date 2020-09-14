# Program for a Simple Registration Page (no data element)

# importing required classed from tkinter
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Button
from tkinter import Checkbutton

root = Tk()                     # creating object of Tk Class

# python logic here

# creating a function to print user inputted data
def Details():
    if user_name.get() != '' and user_city.get() != '' and user_reg_num.get() != 0:
        print('\nDetails Entered by User are')
        print(f'The Name Entered by User is {user_name.get()}')
        print(f'The City Entered by User is {user_city.get()}')
        print(f'The Registration Number Entered by User is {user_reg_num.get()}')
        if user_feedback.get() == 1:
            print('You Liked the Design')
        else:
            print('You didn\'t liked the Design')

    else:
        print('Details Not Entered Completely')

# creating a function to clear the entry fields of GUI
def Clear():
    if user_name.get() != '' or user_city.get() != '' or user_reg_num.get() != 0 or user_feedback.get() != 0:
        user_name.set('')
        user_city.set('')
        user_reg_num.set(0)
        user_feedback.set(0)
        print('\nCleared!')
    else:
        print('Nothing to Clear')

# python logic here

# GUI Logic here

# window setting
root.title('Registration')      # giving title to GUI Window
root.geometry('310x232')        # setting deafult size of GUI Window
root.minsize(310, 232)          # setting min-size of GUI Window
root.maxsize(310, 232)          # setting max-size of GUI Window

# component setting

# creating frame
frame = Frame(root, borderwidth = 10, bg = '#ff9933')            # creating a frame
frame.grid()

# creating labels to tell user what type of data to be insert
label_name = Label(frame, text = 'Enter Name', bg = '#138808', fg = '#ffffff').grid(row = 0, column = 0, pady = 10)
label_city = Label(frame, text = 'Enter City', bg = '#138808', fg = '#ffffff').grid(row = 1, column = 0, pady = 10)
label_registration_number = Label(frame, text = 'Enter Registration Number', bg = '#138808', fg = '#ffffff').grid(row = 2, column = 0, pady = 10)
label_interested = Label(frame, text = 'Tick to give good feedback', bg = '#138808', fg = '#ffffff').grid(row = 3, column = 0, pady = 10)

# creating entry fields to take input from user
# creating input variables to store user input data
user_name = StringVar()
user_city = StringVar()
user_reg_num = IntVar()
user_feedback = IntVar()
# adding the variables to entry fields
input_name = Entry(frame, textvariable = user_name).grid(row = 0, column = 1, pady = 10)
input_city = Entry(frame, textvariable = user_city).grid(row = 1, column = 1, pady = 10)
input_reg_num = Entry(frame, textvariable = user_reg_num).grid(row = 2, column = 1, padx = 10, pady = 10)
# adding the variable to checkbox
input_feedback = Checkbutton(frame, text = 'Looking Good ?', variable = user_feedback).grid(row = 3, column = 1, pady = 10)

# creating control buttons
button_submit = Button(frame, text = 'Submit', bg = '#000080', fg = '#ffffff', command = Details).grid(row = 4, column = 0, pady = 10)
button_clear = Button(frame, text = 'Clear', bg = '#000080', fg = '#ffffff', command = Clear).grid(row = 4, column = 1, pady = 10)

# GUI Logic here

root.mainloop()             # holding the GUI window in a loop

print('\nThanks!')          # program complete counter