from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox

root = Tk()

root.geometry('544x244')

# Programming Logic Here

def help():
    messagebox.showinfo('Help', 'Sorry I can\'t Help! you')

def askquestion():
    ans = messagebox.askquestion('Simple Question', 'Is this GUI good')
    print(ans)

def exit_func():
    ans = messagebox.askyesno('Exit?', 'Are you sure want to leave?')
    if ans:
        quit()

# Programming Logic Here

# GUI Logic Here

# creating original Menu Bar
menubar = Menu(root)

# -------------------- File Menu --------------------

# creating Menus of File Menu
m1 = Menu(menubar, tearoff = 0)
# adding Sub Menus
m1.add_command(label = 'New')
m1.add_command(label = 'Open')
m1.add_separator()
m1.add_command(label = 'Save')
m1.add_command(label = 'Save As')

# adding the Menu to Menu Bar
root.config(menu = menubar)

# adding Sub Menus to File Menu
menubar.add_cascade(label = 'File', menu = m1)

# -------------------- File Menu --------------------

# -------------------- Edit Menu --------------------

# creating Menu of File Menu
m2 = Menu(menubar, tearoff = 0)
# adding sub menus
m2.add_command(label = 'Undo')
m2.add_command(label = 'Redo')
m2.add_separator()
m2.add_command(label = 'Copy')
m2.add_command(label = 'Cut')
m2.add_command(label = 'Paste')

# adding the Menu to Menu Bar
root.config(menu = menubar)

# adding Sub Menus to File Menu
menubar.add_cascade(label = 'Edit', menu = m2)

# -------------------- Edit Menu --------------------

# -------------------- Help Menu --------------------

# creating Menu of File Menu
m3 = Menu(menubar, tearoff = 0)
# adding sub menus
m3.add_command(label = 'Contact Us')
m3.add_command(label = 'Mail Us')
m3.add_separator()
m3.add_command(label = 'Visit Our Site')
m3.add_command(label = 'Forums')
m3.add_separator()
m3.add_command(label = 'Help!', command = help)
m3.add_command(label = 'Feedback!', command = askquestion)

# adding the Menu to Menu Bar
root.config(menu = menubar)

# adding Sub Menus to File Menu
menubar.add_cascade(label = 'Help!', menu = m3)

# -------------------- Help Menu --------------------

# -------------------- Help Menu --------------------
menubar.add_command(label = 'Exit', command = exit_func)
root.config(menu = menubar)
# -------------------- Help Menu --------------------

# GUI Logic Here

root.mainloop()