import tkinter as tk
from tkinter import font
from src.GUI.ClassicGameWindow import ClassicGameWindow


class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.yellow = "#ECFF49"
        self.green = "#28A645"

        f = font.Font(size=20, family="Comic Sans MS", weight="bold")

        self.configure(background=self.green)

        for i in range(0, 11):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

        self.pack(fill=tk.BOTH, expand=True)

        titleCard = tk.Label(self, text="Wordle Clone", font=("Comic Sans MS", 50, "bold"), fg=self.yellow,
                             bg=self.green)
        titleCard.grid(column=5, row=1, columnspan=1)
        subtitleCard = tk.Label(self, text="Based on the #1 Word Game of 2021",
                                font=("Comic Sans MS", 15, "bold"), fg="light gray", bg=self.green)
        subtitleCard.grid(column=5, row=2, columnspan=1)
        startButton = tk.Button(self, name="classic_start", width=10, height=1, text="Classic Mode",
                                bg="#34DB66", font=f,
                                fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow, borderwidth=5,
                                relief="ridge", command=lambda: self.setScene(1))
        startButton.grid(column=1, row=4, columnspan=9)
        customStartButton = tk.Button(self, name="custom_start", width=10, height=1, text="Custom Mode",
                                      bg="#34DB66", font=f,
                                      fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                      borderwidth=5, relief="ridge", command=lambda: self.setScene(1))
        customStartButton.grid(column=1, row=6, columnspan=9)
        optionsButton = tk.Button(self, name="options", width=10, height=1, text="Options", bg="#34DB66",
                                  font=f,
                                  fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                  borderwidth=5, relief="ridge", command=lambda: self.setScene(2))
        optionsButton.grid(column=1, row=8, columnspan=9)
        exitButton = tk.Button(self, name="exit", width=10, height=1, text="Exit", bg="#34DB66", font=f,
                               fg=self.yellow,
                               activebackground="#34DB66", activeforeground=self.yellow, borderwidth=5, relief="ridge",
                               command=lambda: self.setScene())
        exitButton.grid(column=1, row=10, columnspan=9)

    def setScene(self, scene=0) -> None:
        match scene:
            case 1:
                for widget in self.winfo_children():
                    widget.destroy()
                self.destroy()
                ClassicGameWindow(master=self.master)
            case 2:
                print("Options")
            case _:
                for widget in self.winfo_children():
                    widget.destroy()
                self.destroy()
                MainMenu2(window=self.master)


class MainMenu2(tk.Frame):
    def __init__(self, window):
        super().__init__(window)

        self.window = window
        self.yellow = "#28A645"
        self.green = "#ECFF49"

        f = font.Font(size=20, family="Comic Sans MS", weight="bold")

        self.configure(background=self.green)
        for i in range(0, 11):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

        self.pack(fill=tk.BOTH, expand=True)

        titleCard = tk.Label(self, text="Wordle Clone", font=("Comic Sans MS", 50, "bold"), fg=self.yellow,
                             bg=self.green)
        titleCard.grid(column=5, row=1, columnspan=1)
        subtitleCard = tk.Label(self, text="Based on the #1 Word Game of 2021",
                                font=("Comic Sans MS", 15, "bold"), fg="light gray", bg=self.green)
        subtitleCard.grid(column=5, row=2, columnspan=1)
        startButton = tk.Button(self, name="classic_start", width=10, height=1, text="Classic Mode",
                                bg="#34DB66", font=f,
                                fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow, borderwidth=5,
                                relief="ridge", command=lambda: self.setScene(1))
        startButton.grid(column=1, row=4, columnspan=9)
        customStartButton = tk.Button(self, name="custom_start", width=10, height=1, text="Custom Mode",
                                      bg="#34DB66", font=f,
                                      fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                      borderwidth=5, relief="ridge", command=lambda: self.setScene(1))
        customStartButton.grid(column=1, row=6, columnspan=9)
        optionsButton = tk.Button(self, name="options", width=10, height=1, text="Options", bg="#34DB66",
                                  font=f,
                                  fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                  borderwidth=5, relief="ridge", command=lambda: self.setScene(2))
        optionsButton.grid(column=1, row=8, columnspan=9)
        exitButton = tk.Button(self, name="exit", width=10, height=1, text="Exit", bg="#34DB66", font=f,
                               fg=self.yellow,
                               activebackground="#34DB66", activeforeground=self.yellow, borderwidth=5, relief="ridge",
                               command=lambda: self.setScene())
        exitButton.grid(column=1, row=10, columnspan=9)

    def setScene(self, scene=0) -> None:
        match scene:
            case 1:
                print("Start")
            case 2:
                print("Options")
            case _:
                for widget in self.winfo_children():
                    widget.destroy()
                self.destroy()
                self.window.destroy()
