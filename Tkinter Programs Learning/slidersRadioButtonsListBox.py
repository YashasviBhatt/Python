from tkinter import *

root = Tk()

root.geometry('400x768')

scrollbar = Scrollbar()
scrollbar.pack(side = 'right', fill = 'y')

def Upload():
    from time import sleep
    statusvar.set('Busy')
    root.update()
    sleep(2)
    statusvar.set('Ready')

#--------------------------Sliders--------------------------

Label(text = 'Slider', font = 'bold 20').pack()

# Vertical Slider
Label(text = 'Default Slider (Vertical)').pack()
myslider = Scale(from_= 0, to = 100).pack()

# Horizontal Slider
Label(text = 'Default Slider (Horizontal)').pack()
myslider1 = Scale(from_= 0, to = 100, orient = 'horizontal').pack()

# Slider with gap
Label(text = 'Slider with Gap').pack()
myslider2 = Scale(from_= 0, to = 100, orient = 'horizontal', tickinterval = 50).pack()

#--------------------------Sliders--------------------------

#--------------------------RadioButtons--------------------------

Label(text = 'RadioButtons', font = 'bold 20').pack()
var= StringVar()
var.set('Choose')

Label(text = 'Default RadioButton').pack()

radio = Radiobutton(text = 'Radio Button 1', variable = var, value = 'Radio Button 1').pack()
radio3 = Radiobutton(text = 'Radio Button 2', variable = var, value = 'Radio Button 2').pack()
radio2 = Radiobutton(text = 'Radio Button 3', variable = var, value = 'Radio Button 3').pack()
radio3 = Radiobutton(text = 'Radio Button 4', variable = var, value = 'Radio Button 4').pack()

#--------------------------RadioButtons--------------------------

#--------------------------ListBox--------------------------

Label(text = 'ListBox', font = 'bold 20').pack()

listbox = Listbox(yscrollcommand = scrollbar.set, height = 7)
listbox.insert(END, 'First Item')
listbox.insert(END, 'Second Item')
listbox.insert(END, 'Third Item')
listbox.insert(END, 'Fourth Item')
listbox.insert(END, 'Fifth Item')
listbox.insert(END, 'Sixth Item')
for i in range(500):
    listbox.insert(END, f'Item {i}')
listbox.pack()

scrollbar.config(command = listbox.yview)

#--------------------------ListBox--------------------------

#--------------------------StatusBar--------------------------

Button(text = 'Update Status Bar', command = Upload).pack()
statusvar = StringVar()
statusvar.set('Ready')
Label(textvariable = statusvar, relief = 'sunken', anchor = 'w').pack(side = 'bottom', fill = 'x')

#--------------------------StatusBar--------------------------

print(listbox.get(0).index('First Item'))

root.mainloop()