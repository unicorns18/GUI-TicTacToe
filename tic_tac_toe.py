import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("550x580")
window.configure(background="black")

# Global Variables
USER_X = True
USER_O = False
USER_X_VAL = 1
USER_O_VAL = 2
CURRENT_PLAYER = USER_X_VAL


def check_winner():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or  # across the top
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or  # across the middle
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or  # across the bottom
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or  # down the left side
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or  # down the middle
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or  # down the right side
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or  # diagonal
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):  # diagonal
        messagebox.showinfo("Winner X", "You have just won a game")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or  # across the top
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or  # across the middle
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or  # across the bottom
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or  # down the left side
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or  # down the middle
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or  # down the right side
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or  # diagonal
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):  # diagonal
        messagebox.showinfo("Winner O", "You have just won a game")


def check_tie():
    pass


def change_player():
    global CURRENT_PLAYER

    if CURRENT_PLAYER == USER_X_VAL:
        CURRENT_PLAYER = USER_O_VAL
    else:
        CURRENT_PLAYER = USER_X_VAL

    return CURRENT_PLAYER


def btn1():
    global CURRENT_PLAYER

    if button1["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button1["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button1["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn2():
    global CURRENT_PLAYER

    if button2["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button2["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button2["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn3():
    global CURRENT_PLAYER

    if button3["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button3["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button3["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn4():
    global CURRENT_PLAYER

    if button4["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button4["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button4["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn5():
    global CURRENT_PLAYER

    if button5["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button5["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button5["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn6():
    global CURRENT_PLAYER

    if button6["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button6["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button6["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn7():
    global CURRENT_PLAYER

    if button7["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button7["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button7["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn8():
    global CURRENT_PLAYER

    if button8["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button8["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button8["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


def btn9():
    global CURRENT_PLAYER

    if button9["text"] == " ":  # If the text is empty, then proceed.
        if CURRENT_PLAYER == USER_X_VAL:  # If the current player is X, then set it to O.
            button9["text"] = "X"
            CURRENT_PLAYER = change_player()
        elif CURRENT_PLAYER == USER_O_VAL:  # If the current player is O, then set it to X.
            button9["text"] = "O"
            CURRENT_PLAYER = change_player()

        check_winner()


# Buttons
button1 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn1)
button1.grid(row=1, column=0)

button2 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn2)
button2.grid(row=1, column=1)

button3 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn3)
button3.grid(row=1, column=2)

button4 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn4)
button4.grid(row=2, column=0)

button5 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn5)
button5.grid(row=2, column=1)

button6 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn6)
button6.grid(row=2, column=2)

button7 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn7)
button7.grid(row=3, column=0)

button8 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn8)
button8.grid(row=3, column=1)

button9 = tk.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=btn9)
button9.grid(row=3, column=2)

window.mainloop()
