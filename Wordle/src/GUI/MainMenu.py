import tkinter as tk
from tkinter import font
from .FrameTraveler import FrameTraveler


class MainMenu(FrameTraveler):
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
                                relief="ridge", command=lambda: self.go_to_game_window())
        startButton.grid(column=1, row=4, columnspan=9)
        customStartButton = tk.Button(self, name="custom_start", width=12, height=1, text="Custom Mode",
                                      bg="#34DB66", font=f,
                                      fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                      borderwidth=5, relief="ridge", command=lambda: self.go_to_customize_window())
        customStartButton.grid(column=1, row=6, columnspan=9)
        historyButton = tk.Button(self, name="runhistory", width=12, height=1, text="Run History", bg="#34DB66",
                                  font=f,
                                  fg=self.yellow, activebackground="#34DB66", activeforeground=self.yellow,
                                  borderwidth=5, relief="ridge", command=lambda: self.go_to_run_history())
        historyButton.grid(column=1, row=8, columnspan=9)
        exitButton = tk.Button(self, name="exit", width=12, height=1, text="Exit", bg="#34DB66", font=f,
                               fg=self.yellow,
                               activebackground="#34DB66", activeforeground=self.yellow, borderwidth=5, relief="ridge",
                               command=lambda: self.exit_game())
        exitButton.grid(column=1, row=10, columnspan=9)
