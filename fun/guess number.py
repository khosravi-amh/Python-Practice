# Guess Number
from tkinter import *
from tkinter import messagebox
import random

# random number
secret_num = random.randint(1, 100)

round_num = 5
game_over = False


def guess(num):
    global secret_num, round_num, game_over
    if game_over:
        return
    num = int(num)
    if num < secret_num:
        round_num -= 1
        lb_title.config(text=f"Enter a Number, {round_num} of 5 ", font=(20))
        lb_untitle.config(text='the number is bigger')
    elif num > secret_num:
        round_num -= 1
        lb_title.config(text=f"Enter a Number, {round_num} of 5 ", font=(20))
        lb_untitle.config(text='the number is smaller')
    else:
        lb_untitle.config(text=f'you guessed right! ({secret_num})')
        end()

    if round_num == 0:
        lb_untitle.config(
            text=f'You lose! the opportunities are over, ({secret_num}) ')
        end()


def end():
    global game_over
    game_over = True
    num_text.config(state='disabled')
    btn1.config(state='disabled')
    btn2.config(state='disabled')


def help():
    messagebox.showinfo(
        'Help', 'Guess a number between 1 and 100. \n Change your number based on the message, bigger/smaller. \n You only have five chances or you lose. ')


# window
win = Tk()
win.title('Guess Number')
win.geometry('300x200')
win.resizable(0, 0)

# Lable title
lb_title = Label(win, text="Enter a Number, 5 of 5 ", font=(20))
lb_untitle = Label(win, text=' ', font=(15))

num_text = Entry(win, width=30, font=(20), justify='center')

# Button
btn1 = Button(win, text='Check', font=(
    20), command=lambda: guess(num_text.get()))
print('secret number = ', secret_num)
btn2 = Button(win, text='Help', font=(10), command=help)
lb_title.pack()
lb_untitle.pack()
num_text.pack(pady=20)
btn1.pack()
btn2.pack()
win.mainloop()
