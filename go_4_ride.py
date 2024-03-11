#LET'S GO FOR RIDE

from tkinter import *

window = Tk()
window.geometry("500x200") #size of the window

car = PhotoImage(file="ride.png")
label = Label(window, image=car)
label.place(x=0, y=0)

window.mainloop()