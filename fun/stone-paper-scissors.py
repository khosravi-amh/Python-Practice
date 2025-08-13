# Stone Paper Scissors
import tkinter as tk
from tkinter import messagebox
import random

choices = ["stone", "paper", "scissors"]
round_number = 1
your_score = 0
system_score = 0


def play(your_choice):
    global round_number, your_score, system_score

    if round_number > 3:
        return

    system_choice = random.choice(choices)

    # The winner of this round
    if your_choice == system_choice:
        result = "tie game"
    elif (your_choice == "stone" and system_choice == "scissors") or \
         (your_choice == "paper" and system_choice == "stone") or \
         (your_choice == "scissors" and system_choice == "paper"):
        result = "you win "
        your_score += 1
    else:
        result = " computer win"
        system_score += 1

    # Show results
    lb1_title.config(text=f"round {round_number} of 1 \n"
                     f"you: {your_choice} | computer: {system_choice}\n"
                     f"{result}")

    round_number += 1

    # if game is over
    if round_number > 3:
        if your_score > system_score:
            final_result = "you win! 🏆"
        elif your_score < system_score:
            final_result = " computer win! 💻"
        else:
            final_result = "game was tied! 🤝"
        messagebox.showinfo("End Of Game", f"Final Result  \n"
                            f"you: {your_score} | computer: {system_score}\n"
                            f"{final_result}")


# window
win = tk.Tk()
win.title("stone - paper - scissors (3 rounds)")
win.geometry("400x250")
win.resizable(0, 0)

# Label
lb1_title = tk.Label(
    win, text="Game has started! Select:", font=("Arial", 15))
lb1_title.pack(pady=30)

# Frame buttons
frame = tk.Frame(win)
frame.pack(pady=10)

# buttons
rock_btn = tk.Button(frame, text="stone", width=12,
                     height=3, command=lambda: play("stone"))
paper_btn = tk.Button(frame, text="paper", width=12,
                      height=3, command=lambda: play("paper"))
scissors_btn = tk.Button(frame, text="scissors", width=12,
                         height=3, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

win.mainloop()
