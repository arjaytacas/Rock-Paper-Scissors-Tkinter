from tkinter import *
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, window):
        self.window = window
        self.window.config(background="white")
        self.window.title("Rock Paper Scissors")
        self.choices = ["Rock", "Paper", "Scissors"]
        self.paper_img = PhotoImage(file='images/1.png')
        self.rock_img = PhotoImage(file='images/3.png')
        self.scissor_img = PhotoImage(file='images/2.png')
        self.create_widgets()

    def create_widgets(self):
        title_label = Label(self.window, text="Rock-Paper-Scissors", background="white", font=("Arial", 40))
        title_label.grid(column=0, row=0, columnspan=3)
        choice = Label(self.window, text="Take your pick!", background="white", font=("Arial", 20))
        choice.grid(column=0, row=1, columnspan=3)
        paper_image = Button(self.window, image=self.paper_img, command=lambda: self.play('paper'))
        rock_image = Button(self.window, image=self.rock_img, command=lambda: self.play('rock'))
        scissor_image = Button(self.window, image=self.scissor_img, command=lambda: self.play('scissors'))
        paper_image.grid(column=0, row=2)
        rock_image.grid(column=1, row=2)
        scissor_image.grid(column=2, row=2)

    def play(self, pick):
        picking = ['rock', 'paper', 'scissors']
        computer = random.choice(picking)
        self.get_result(computer, pick)

    def get_result(self, computer, pick):
        if computer == pick:
            messagebox.showinfo('DRAW', "It's a draw")
        elif computer == 'rock' and pick == 'paper':
            messagebox.showinfo('CONGRATULATIONS', "You Win!")
        elif computer == 'rock' and pick == 'scissors':
            messagebox.showinfo('TOO BAD', "You Lose!")
        elif computer == 'paper' and pick == 'scissors':
            messagebox.showinfo('CONGRATULATIONS', "You Win!")
        elif computer == 'paper' and pick == 'rock':
            messagebox.showinfo('TOO BAD', "You Lose!")
        elif computer == 'scissors' and pick == 'rock':
            messagebox.showinfo('CONGRATULATIONS', "You Win!")
        elif computer == 'scissors' and pick == 'paper':
            messagebox.showinfo('TOO BAD', "You Lose!")
