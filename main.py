from tkinter import *

window = Tk()
window.config(background="white")
window.title("Rock-Paper-Scissors")

title_label = Label(window, text="Rock-Paper-Scissors", background="white", font=("Arial", 40))
title_label.grid(column=0, row=0, columnspan=3)

choice = Label(window, text="Take your pick!", background="white", font=("Arial", 20))
choice.grid(column=0, row=1, columnspan=3)

paper = PhotoImage(file='images/1.png')
rock = PhotoImage(file='images/3.png')
scissor = PhotoImage(file='images/2.png')
paper_image = Button(window, image=paper)
rock_image = Button(window, image=rock)
scissor_image = Button(window, image=scissor)
paper_image.grid(column=0, row=2)
rock_image.grid(column=1, row=2)
scissor_image.grid(column=2, row=2)

window.mainloop()