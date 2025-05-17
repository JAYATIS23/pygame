#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from random import randint

window = Tk()
window.geometry("350x300")
window.title("Rock, Paper, Scissors, Lizard, Spock")
window.configure(background="dark slate gray")

def window2():
    w2 = Toplevel(window)
    w2.title("THE GAME")
    w2.configure(background="dark slate gray")
    
    # Load images using raw strings
    middle_player_img = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\middleplayer.jpeg").resize((70, 70), Image.LANCZOS))
    middle_comp_img = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\middlecomp.jpeg").resize((70, 70), Image.LANCZOS))
    
    rockimg = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\ro.jpeg").resize((70, 70), Image.LANCZOS))
    paperimg = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\paper.jpeg").resize((70, 70), Image.LANCZOS))
    scissorsimg = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\scissors.jpeg").resize((70, 70), Image.LANCZOS))
    lizardimg = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\lizard.jpeg").resize((70, 70), Image.LANCZOS))
    spockimg = ImageTk.PhotoImage(Image.open(r"C:\Users\sjaya\Downloads\spock.jpeg").resize((70, 70), Image.LANCZOS))

    # Keep references to images to prevent garbage collection
    w2.image_refs = [middle_player_img, middle_comp_img, rockimg, paperimg, scissorsimg, lizardimg, spockimg]

    middleplayer = Label(w2, image=middle_player_img)
    middlecomputer = Label(w2, image=middle_comp_img)
    middleplayer.grid(row=4, column=4)
    middlecomputer.grid(row=4, column=11)

    lost = Label(w2, text=0, font=20, bg="pale green", fg="dim gray")
    win = Label(w2, text=0, font=20, bg="pale green", fg="dim gray")
    lost.grid(row=7, column=12)
    win.grid(row=7, column=5)

    def score_of_comp():
        total = int(lost['text']) + 1
        lost['text'] = str(total)
        if total == 3:
            window3()

    def score_of_player():
        total = int(win['text']) + 1
        win['text'] = str(total)

    def results(p, c):
        if p == c:
            return
        outcomes = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }
        if c in outcomes[p]:
            score_of_player()
        else:
            score_of_comp()

    options = ["rock", "paper", "scissors", "lizard", "spock"]

    def selection(x):
        choice_of_computer = options[randint(0, 4)]
        choice_of_player = x

        images = {
            "rock": rockimg,
            "paper": paperimg,
            "scissors": scissorsimg,
            "lizard": lizardimg,
            "spock": spockimg
        }

        middlecomputer.configure(image=images[choice_of_computer])
        middleplayer.configure(image=images[choice_of_player])
        results(choice_of_player, choice_of_computer)

    Label(w2, text=e1.get(), font=20, bg="misty rose", fg="gray29").grid(row=1, column=4)
    Label(w2, text="Computer", font=20, bg="misty rose", fg="gray29").grid(row=1, column=11)

    Button(w2, image=rockimg, command=lambda: selection("rock")).grid(row=2, column=1)
    Button(w2, image=paperimg, command=lambda: selection("paper")).grid(row=3, column=1)
    Button(w2, image=scissorsimg, command=lambda: selection("scissors")).grid(row=4, column=1)
    Button(w2, image=lizardimg, command=lambda: selection("lizard")).grid(row=5, column=1)
    Button(w2, image=spockimg, command=lambda: selection("spock")).grid(row=6, column=1)

    Label(w2, image=rockimg).grid(row=2, column=14)
    Label(w2, image=paperimg).grid(row=3, column=14)
    Label(w2, image=scissorsimg).grid(row=4, column=14)
    Label(w2, image=lizardimg).grid(row=5, column=14)
    Label(w2, image=spockimg).grid(row=6, column=14)

    Label(w2, text="VS", font=30, bg="misty rose", fg="gray29").grid(row=4, column=9)
    Label(w2, text="POINTS", font=30, bg="gray2", fg="snow").grid(row=7, column=1)
    Label(w2, text=f"{e1.get()} 's score=>", font=20, bg="pale green", fg="dim gray").grid(row=7, column=4)
    Label(w2, text="Computer's score=>", font=20, bg="pale green", fg="dim gray").grid(row=7, column=11)

    def window3():
        w3 = Toplevel(w2)
        w3.title("RESULTS")
        w3.geometry("320x300")
        w3.configure(background="dark slate gray")

        def exit_game():
            w3.destroy()
            w2.destroy()
            window.destroy()

        def new_game():
            w3.destroy()
            w2.destroy()
            e1.delete(0, END)

        Label(w3, text=f"{e1.get()} 's score is:-", font=30, bg="misty rose", fg="gray29").place(x=10, y=50)
        Label(w3, text=win.cget("text"), font=30).place(x=190, y=50)
        Button(w3, text="EXIT", command=exit_game, height=4, width=10, bg="pale green", fg="dim gray").place(x=10, y=200)
        Button(w3, text="START NEW GAME", command=new_game, height=4, width=20, bg="pale green", fg="dim gray").place(x=150, y=200)

    w2.mainloop()

# Main window
Label(window, text="THE GAME OF", font=('arial', 20), bd=5, bg="misty rose", fg="gray29").place(x=80, y=40)
Label(window, text="CHANCES", font=('arial', 29, 'bold'), bg="misty rose", fg="gray29").place(x=80, y=80)
Label(window, text="Enter name:", font=('arial'), bg="ivory2", fg="IndianRed1").place(x=50, y=150)

e1 = Entry(window)
e1.place(x=170, y=150)

Button(window, text="START!", font=('bold', 12), height=3, width=10, bg="pale green", fg="dim gray", command=window2).place(x=130, y=220)

window.mainloop()
