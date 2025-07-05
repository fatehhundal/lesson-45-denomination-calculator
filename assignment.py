from tkinter import *
from PIL import Image, ImageTk
import random

options = ["Rock", "Paper", "Scissors"]

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
        (player == "Paper" and computer == "Rock") or \
        (player == "Scissors" and computer == "Paper"):
            return "Player wins"
    else:
        return "Computer wins"

def play(player_choice):
    computer_choice = random.choice(options)
    player_label.config(text="Player: " + player_choice)
    computer_label.config(text="Computer: " + computer_choice)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text="Result: " + result)

def reset_game():
    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Result: ")

root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("300x300")

rock = Button(root, text="Rock", command=lambda: play("Rock"), width=15).pack(pady=5)
paper = Button(root, text="Paper", command=lambda: play("Paper"), width=15).pack(pady=5)
scissors = Button(root, text="Scissors", command=lambda: play("Scissors"), width=15).pack(pady=5)

player_label = Label(root, text="Player: ", font=("Arial", 12))
player_label.pack(pady=5)

computer_label = Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

Button(root, text="Reset game", command=reset_game, width=15, bg="lightgray").pack(pady=10)

root.mainloop()