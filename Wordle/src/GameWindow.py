import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font


def setScene(w: tk, scene=0) -> None:
    match scene:
        case 1:
            print("Start")
        case 2:
            print("Options")
        case _:
            w.destroy()
            print("Exit")


class GameWindow:
    def __init__(self):

        window = tk.Tk()
        window.title("Wordle Clone")
        window.geometry("600x600")
        window.configure(background="#16B865")

        for i in range(0, 11):
            window.rowconfigure(i, weight=1)
        for i in range(0, 11):
            window.columnconfigure(i, weight=1)

        f = font.Font(size=35, family="Comic Sans MS", weight="bold")
        startButton = tk.Button(name="start", width=8, height=1, text="Start", bg="#34DB66", font=f, fg="yellow",
                                activebackground="#34DB66", activeforeground="yellow", borderwidth=5, relief="ridge",
                                command=lambda: setScene(window, 1))
        startButton.grid(column=1, row=2, columnspan=9)
        hardcore = tk.BooleanVar()
        hardcore.set(True)
        hardcoreStartButton = tk.Checkbutton(window, name="hardcore_check", width=8, height=2, text="Hardcore", font=("Comic Sans MS", 15),
                                             fg="yellow", activeforeground="yellow", bg="#16B865", activebackground="#16B865",
                                             variable=hardcore, onvalue=True, offvalue=False)
        hardcoreStartButton.grid(column=5, row=3)
        optionsButton = tk.Button(name="options", width=8, height=1, text="Options", bg="#34DB66", font=f, fg="yellow",
                                  activebackground="#34DB66", activeforeground="yellow", borderwidth=5, relief="ridge",
                                  command=lambda: setScene(window, 2))
        optionsButton.grid(column=1, row=5, columnspan=9)
        exitButton = tk.Button(name="exit", width=8, height=1, text="Exit", bg="#34DB66", font=f, fg="yellow",
                               activebackground="#34DB66", activeforeground="yellow", borderwidth=5, relief="ridge",
                               command=lambda: setScene(window))
        exitButton.grid(column=1, row=8, columnspan=9)

        window.mainloop()
