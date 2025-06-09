import tkinter as tk
from tkinter import font
import json
from .FrameTraveler import FrameTraveler


class RunHistory(FrameTraveler):
    def __init__(self, master):
        super().__init__(master)

        self.gray = "#3A3A3C"
        self.black = "#121213"
        self.yellow = "#ECFF49"
        self.green = "#28A645"

        self.f = font.Font(size=20, family="Comic Sans MS", weight="bold")

        self.runs = dict()
        self.configure(bg=self.black)
        for i in range(0, 11):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        try:
            self.data = json.load(open("src/Text/history.json"))
        except FileNotFoundError:
            self.data = json.load(open("Text/history.json"))

        self.pack(fill=tk.BOTH, expand=True)

        self.saves = self.create_saves()
        self.saves.grid(row=0, rowspan=11, column=1)

    def create_saves(self):
        try:
            data = json.load(open("src/Text/history.json"))
        except FileNotFoundError:
            data = json.load(open("Text/history.json"))

        frame = tk.Frame(self)
        runs = data["runs"]

        button = tk.Button(frame, width=25, text="Go to Main Menu", bg=self.gray, fg='white',
                           font=self.f, command=lambda: self.go_to_main_menu(), anchor=tk.CENTER,
                           activebackground=self.gray, activeforeground='white')
        button.grid(row=0)

        for pos, run in enumerate(runs):
            if len(run.keys()) == 0:
                text = ""
                command = lambda char="a": self.go_to_run_history()
            else:
                if 'guesses' not in run.keys():
                    attempts = len(run['replay'])
                else:
                    attempts = run['guesses']
                text = f"{run['result']} | {run['word']} | {attempts} / {len(run['replay'])}"
                command = lambda var=run: self.go_to_game_window(rows=len(var['replay']),
                                                                 columns=len(var['word']),
                                                                 history=True, replay=var['replay'])
            if "hardmode" not in run.keys() or not run["hardmode"]:
                color = self.black
            else:
                color = self.yellow
            self.runs[f"run{pos}"] = tk.Button(frame, width=25, text=text, bg=self.gray, fg=color,
                                               font=self.f, command=command, anchor=tk.CENTER,
                                               activebackground=self.gray, activeforeground=color)
            self.runs[f"run{pos}"].grid(row=pos + 2)
        return frame


def add_run(result, word, replay, hardmode=False, guesses=0):
    try:
        data = json.load(open("src/Text/history.json"))
    except FileNotFoundError:
        data = json.load(open("Text/history.json"))
    runs = data["runs"]
    runs[1:] = runs[:-1]
    runs[0] = dict()
    runs[0]["result"] = result
    runs[0]["word"] = word
    runs[0]["replay"] = replay
    runs[0]["hardmode"] = hardmode

    if guesses > 0:
        runs[0]["guesses"] = guesses
    data["runs"] = runs
    data = json.dumps(data, indent=4)
    try:
        with open("src/Text/history.json", "w") as file:
            file.write(data)
    except FileNotFoundError:
        with open("Text/history.json", "w") as file:
            file.write(data)
