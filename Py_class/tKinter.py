from tkinter import *

def click():
    label.pack()

window = Tk()
window.geometry("420x420")
window.title("Tkinter class")
icon = PhotoImage(file='Py_class/download.png')
window.iconphoto(True,icon)
window.config(background="cyan")
label = Label(window, text="Hello world")
# # label.pack()

# label.place(x=0,y=0)
button = Button(window, text="Hello world")
button.pack()
button.config(command=click)
window.mainloop()

