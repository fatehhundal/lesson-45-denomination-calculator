from tkinter import *
from tkinter import Toplevel
import random

options = ["Rock", "Paper", "Scissors"]

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        return "You win"
    else:
        return "Computer wins"

def show_result_popup(result):
    popup = Toplevel()
    popup.title("Result")
    popup.geometry("200x100")
    Label(popup, text="Result: " + result, font=("Arial", 12)).pack(pady=20)
    Button(popup, text="OK", command=popup.destroy).pack()

def play(player_choice):
    computer_choice = random.choice(options)
    player_label.config(text="Player: " + player_choice)
    computer_label.config(text="Computer: " + computer_choice)
    result = determine_winner(player_choice, computer_choice)
    show_result_popup(result)

def reset_game():
    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")

def start_game():
    game_window = Toplevel(root)
    game_window.title("Rock, Paper, Scissors")
    game_window.geometry("300x300")
    global player_label, computer_label
    Button(game_window, text="Rock", command=lambda: play("Rock"), width=15).pack(pady=5)
    Button(game_window, text="Paper", command=lambda: play("Paper"), width=15).pack(pady=5)
    Button(game_window, text="Scissors", command=lambda: play("Scissors"), width=15).pack(pady=5)
    player_label = Label(game_window, text="Player: ", font=("Arial", 12))
    player_label.pack(pady=5)
    computer_label = Label(game_window, text="Computer: ", font=("Arial", 12))
    computer_label.pack(pady=5)
    Button(game_window, text="Reset", command=reset_game, width=15).pack(pady=10)

root = Tk()
root.title("Game Launcher")
root.geometry("250x100")
Button(root, text="Play Rock, Paper, Scissors", command=start_game, width=30).pack(pady=30)
root.mainloop()