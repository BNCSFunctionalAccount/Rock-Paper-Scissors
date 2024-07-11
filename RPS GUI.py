# RPS GUI 
# By Praveen Kathirvasan 9C
from tkinter import *
import random

# Initialize variables
win = 0
lose = 0

def rps(user):
    global win, lose
    computer = random.randrange(1, 6)
    
    #Logic for the game
    
    wins.set(f"Wins: {win}")
    losses.set(f"Losses: {lose}")

choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Spock", 5: "Lizard"}



top = Tk()
top.wm_title("RPS Python GUI")
top.minsize(width=600, height=200)  # Adjusted window size
top.maxsize(width=600, height=200)

# Adding padding to buttons and labels
pad_x = 10
pad_y = 10

B1 = Button(top, text="Rock", command=lambda: rps(1))
B1.grid(row=0, column=0, padx=pad_x, pady=pad_y)
B2 = Button(top, text="Paper", command=lambda: rps(2))
B2.grid(row=0, column=1, padx=pad_x, pady=pad_y)
B3 = Button(top, text="Scissors", command=lambda: rps(3))
B3.grid(row=0, column=2, padx=pad_x, pady=pad_y)
B4 = Button(top, text="Spock", command=lambda: rps(4))
B4.grid(row=0, column=3, padx=pad_x, pady=pad_y)
B5 = Button(top, text="Lizard", command=lambda: rps(5))
B5.grid(row=0, column=4, padx=pad_x, pady=pad_y)

space = Label(top, text="")
space.grid(row=1, columnspan=5)

var = StringVar()
var.set('Welcome!')
l = Label(top, textvariable=var)
l.grid(row=2, column=0, columnspan=5, padx=pad_x, pady=pad_y)

wins = StringVar()
wins.set(f"Wins: {win}")
w = Label(top, textvariable=wins)
w.grid(row=3, column=0, columnspan=2, padx=pad_x, pady=pad_y)

losses = StringVar()
losses.set(f"Losses: {lose}")
l = Label(top, textvariable=losses)
l.grid(row=3, column=3, columnspan=2, padx=pad_x, pady=pad_y)

copy = Label(top, text="RPS GUI on Tkinter on Python. By Praveen 2016")
copy.grid(row=4, column=0, columnspan=5, padx=pad_x, pady=pad_y)

top.mainloop()
