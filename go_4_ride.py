#LET'S GO FOR A RIDE

from tkinter import *

window = Tk()
window.geometry("1000x250") #size of the window
window.title("BLACK CAR")

car = PhotoImage(file="car.png")
label = Label(window, image=car)
label.place(x=0, y=0)

window.mainloop()