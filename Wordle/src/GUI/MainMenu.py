import tkinter as tk
from tkinter import font


class MainMenu(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master

        self.yellow = "#ECFF49"
        self.green = "#28A645"

        f = font.Font(size=30, family="Comic Sans MS", weight="bold")

        self.configure(background=self.green)

        for i in range(0, 11):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

        self.pack(fill=tk.BOTH, expand=True)

        titleCard = tk.Label(self, text="Wordle Clone", font=("Comic Sans MS", 75, "bold"), fg=self.yellow,
                             bg=self.green)
        titleCard.grid(column=5, row=1, columnspan=1)
        subtitleCard = tk.Label(self, text="Based on the #1 Word Game of 2021",
                                font=("Comic Sans MS", 25, "bold"), fg="light gray", bg=self.green)
        subtitleCard.grid(column=5, row=2, columnspan=1)
        startButton = tk.Button(self, name="classic_start", width=12, height=1, text="Classic Mode",
                                bg="#34DB66", font=f,
                                fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow, borderwidth=5,
                                relief="ridge", command=lambda: self.setScene(1))
        startButton.grid(column=1, row=4, columnspan=9)
        customStartButton = tk.Button(self, name="custom_start", width=12, height=1, text="Custom Mode",
                                      bg="#34DB66", font=f,
                                      fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                      borderwidth=5, relief="ridge", command=lambda: self.setScene(2))
        customStartButton.grid(column=1, row=6, columnspan=9)
        historyButton = tk.Button(self, name="runhistory", width=12, height=1, text="Run History", bg="#34DB66",
                                  font=f,
                                  fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                  borderwidth=5, relief="ridge", command=lambda: self.setScene(3))
        historyButton.grid(column=1, row=8, columnspan=9)
        exitButton = tk.Button(self, name="exit", width=12, height=1, text="Exit", bg="#34DB66", font=f,
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
                from src.GUI.GameWindow import GameWindow
                GameWindow(master=self.master)
            case 2:
                for widget in self.winfo_children():
                    widget.destroy()
                self.destroy()
                # from src.GUI.GameWindow import GameWindow
                # GameWindow(master=self.master, hardmode=True, rows=10, columns=10)
                from src.GUI.CustomizeGame import CustomizeGame
                CustomizeGame(master=self.master)
            case _:
                for widget in self.winfo_children():
                    widget.destroy()
                self.destroy()
                self.master.destroy()
