"""
Tic_Tac_Toe Game by Jay - 27/03/20
Github: mr-circuit
"""

from tkinter import Tk, ttk, Button, messagebox
from random import randint
import pygame

pygame.mixer.init()

loser_sound = pygame.mixer.Sound("looser.wav")
winner_sound = pygame.mixer.Sound("winner.wav")

playingPawn = 1
player1 = []
player2 = []
move = 0
d = {}


def button_press(symbol):
    global playingPawn
    global player1, player2
    global move

    if playingPawn == 1:
        game_design(symbol, "x")
        player1.append(symbol)
        move += 1
        root.title("Tic Tac Toe : It's Player 2 Turn")
        playingPawn = 2

    elif playingPawn == 2:
        game_design(symbol, "o")
        player2.append(symbol)
        move += 1
        root.title("Tic Tac Toe : It's Player 1 Turn")
        playingPawn = 1
    find_winner()


def game_design(box_id, pawn):
    i = box_id
    if 0 < i < 10:
        d["b" + str(i)].config(text=pawn)
        d["b" + str(i)].state(['disabled'])


def find_winner():
    global move
    winner = -1

    if (1 in player1) and (2 in player1) and (3 in player1):
        winner = 1
    if (1 in player2) and (2 in player2) and (3 in player2):
        winner = 2

    if (4 in player1) and (5 in player1) and (6 in player1):
        winner = 1
    if (4 in player2) and (5 in player2) and (6 in player2):
        winner = 2

    if (7 in player1) and (8 in player1) and (9 in player1):
        winner = 1
    if (7 in player2) and (8 in player2) and (9 in player2):
        winner = 2

    if (1 in player1) and (4 in player1) and (7 in player1):
        winner = 1
    if (1 in player2) and (4 in player2) and (7 in player2):
        winner = 2

    if (2 in player1) and (5 in player1) and (8 in player1):
        winner = 1
    if (2 in player2) and (5 in player2) and (8 in player2):
        winner = 2

    if (3 in player1) and (6 in player1) and (9 in player1):
        winner = 1
    if (3 in player2) and (6 in player2) and (9 in player2):
        winner = 2

    if (1 in player1) and (5 in player1) and (9 in player1):
        winner = 1
    if (1 in player2) and (5 in player2) and (9 in player2):
        winner = 2

    if (3 in player1) and (5 in player1) and (7 in player1):
        winner = 1
    if (3 in player2) and (5 in player2) and (7 in player2):
        winner = 2

    if winner == 1:
        pygame.mixer.Sound.play(winner_sound)
        messagebox.showinfo(title="Winner",
                            message="Hurray!!! Player 1 is the winner")
    elif winner == 2:
        pygame.mixer.Sound.play(winner_sound)
        messagebox.showinfo(title="Winner",
                            message="Hurray!!! Player 2 is the winner")
    elif move == 9:
        pygame.mixer.Sound.play(loser_sound)
        messagebox.showinfo(title="Draw",
                            message="Match Drawn")


def new_game():
    global player1, player2, move, playingPawn
    player1.clear()
    player2.clear()
    move, playingPawn = 0, 1
    root.title("Tic Tac Toe : Start The Game - It's Player 1 Turn")
    activate_blocks()


def activate_blocks():
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        d["b" + str(i)].config(text=" ")
        d["b" + str(i)].state(['!disabled'])


def computer_play():
    global player1
    global player2
    empty_block = []
    for block in range(9):
        if not ((block + 1 in player1) or (block + 1 in player2)):
            empty_block.append(block + 1)
    try:
        random_value = randint(0, len(empty_block) - 1)
        button_press(empty_block[random_value])
    except:
        print("Unidentified Error!")
        pass


root = Tk()
root.title("Tic Tac toe : Start The Game - It's Player 1 Turn")
fontStyle = ttk.Style()
fontStyle.configure("my.TButton", font=('Comic Sans MS', 24, 'bold'))

d["b" + str(1)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(1)].grid(row=1, column=0, ipadx=50, ipady=50)
d["b" + str(1)].config(command=lambda: button_press(1))

d["b" + str(2)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(2)].grid(row=1, column=1, ipadx=50, ipady=50)
d["b" + str(2)].config(command=lambda: button_press(2))

d["b" + str(3)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(3)].grid(row=1, column=2, ipadx=50, ipady=50)
d["b" + str(3)].config(command=lambda: button_press(3))

d["b" + str(4)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(4)].grid(row=2, column=0, ipadx=50, ipady=50)
d["b" + str(4)].config(command=lambda: button_press(4))

d["b" + str(5)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(5)].grid(row=2, column=1, ipadx=50, ipady=50)
d["b" + str(5)].config(command=lambda: button_press(5))

d["b" + str(6)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(6)].grid(row=2, column=2, ipadx=50, ipady=50)
d["b" + str(6)].config(command=lambda: button_press(6))

d["b" + str(7)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(7)].grid(row=3, column=0, ipadx=50, ipady=50)
d["b" + str(7)].config(command=lambda: button_press(7))

d["b" + str(8)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(8)].grid(row=3, column=1, ipadx=50, ipady=50)
d["b" + str(8)].config(command=lambda: button_press(8))

d["b" + str(9)] = ttk.Button(root, text=" ", style="my.TButton")
d["b" + str(9)].grid(row=3, column=2, ipadx=50, ipady=50)
d["b" + str(9)].config(command=lambda: button_press(9))

Button(text="New Game", font=('Comic Sans MS', 22, 'bold'), bg='Purple', fg='white',
       border=4, width=4, command=lambda: new_game()).grid(row=0, column=0, sticky="we")
Button(text="Computer", font=('Comic Sans MS', 22, 'bold'), bg='red', fg='white',
       border=4, width=4, command=lambda: computer_play()).grid(row=0, column=2, sticky="we")
root.resizable(4, 4)
root.mainloop()
