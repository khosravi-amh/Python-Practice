import tkinter as tk
from tkinter import ttk, messagebox
import random

c1 = {
    "Fruits": ["apple", "banana", "grape", "peach", "melon", "lemon", "orange", "cherry"],
    "Foods": ["rice", "pizza", "barbecue", "soup", "sandwich", "noodle", "chicken", "hamburger"],
    "Drinks": ["tea", "water", "lemonade", "soda", "coffee", "milk", "juice"],
    "Snaks": ["chips", "cookies", "candy", "popcorn", "smarties", "gummy", "lollipop"]
}

chosen_word = ""
mas_word = ""


def choose_category(event):
    global chosen_word, mas_word
    category = combo.get()
    if category in c1:
        chosen_word = random.choice(c1[category])
        print("chosen word =", chosen_word)
        mas_word = chosen_word[0] + " _ " * (len(chosen_word) - 1)
        word_label.config(text=mas_word)
        res_label.config(text="")
        entry.delete(0, "end")


def check_guess():
    guess = entry.get().strip()
    if not chosen_word:
        res_label.config(text="Choose a category", fg="orange")
        return
    if guess == chosen_word:
        res_label.config(text="Well Done! You guessed right 🎉", fg="green")
        word_label.config(text=chosen_word)
    else:
        res_label.config(text="Error! Try again ❌", fg="red")


def help():
    if word_label.cget("text") == chosen_word:
        return
    mas_word = chosen_word[0] + chosen_word[1] + " _ " * (len(chosen_word) - 2)
    word_label.config(text=mas_word)


# window
win = tk.Tk()
win.title("Guess Word")
win.geometry("500x380")
win.resizable(0, 0)

# ComboBox
combo = ttk.Combobox(win, values=list(c1.keys()),
                     state="readonly", font=("tahoma", 15))
combo.set("Choose a Category")
combo.pack(pady=20)
combo.bind("<<ComboboxSelected>>", choose_category)

# Show incomplete word
word_label = tk.Label(win, text="", font=("tahoma", 25))
word_label.pack(pady=10)

# User input
entry = tk.Entry(win, font=("tahoma", 17), justify="center")
entry.pack(pady=10)

# Check Guess
btn = tk.Button(win, text="Check Guess",
                command=check_guess, font=("tahoma", 15))
btn.pack(pady=10)

# Help
btn_help = tk.Button(win, text="Help", command=help, font=("tahoma", 15))
btn_help.pack(pady=10)

# result
res_label = tk.Label(win, text="", font=("tahoma", 17))
res_label.pack(pady=10)

win.mainloop()
