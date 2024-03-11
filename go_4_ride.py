#LET'S GO FOR A RIDE

from tkinter import *

def go_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+5)


window = Tk()
window.geometry("1000x250") #size of the window
window.title("BLACK CAR")

window.bind("<Down>", go_down)
window.bind()
window.bind()
window.bind()

car = PhotoImage(file="car.png")
label = Label(window, image=car)
label.place(x=0, y=0)

window.mainloop()