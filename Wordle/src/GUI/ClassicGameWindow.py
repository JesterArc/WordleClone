import tkinter as tk
from src.Logic.WordProvider import chooseRandomWord, rateAnswer, Rating
from src.GUI.GameRow import GameRows
from tkinter import messagebox


class ClassicGameWindow(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        master.geometry("620x620")

        self.gray = "#3A3A3C"
        self.black = "#121213"
        self.yellow = "#ECFF49"
        self.green = "#28A645"

        self.wordlist = chooseRandomWord()

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=4)
        self.configure(background=self.black)
        self.pack(fill=tk.BOTH, expand=True)

        self.GameRows = GameRows(self)
        self.GameRows.grid(row=0, column=1, sticky=tk.N)

        self.Keys = dict()
        self.keyboard = self.create_keyboard()
        self.keyboard.grid(row=1, column=0, columnspan=3, sticky=tk.S)

        self.guessCounter = 0
        self.secretWord = chooseRandomWord()

    def update_row(self, text):
        row = self.GameRows.getRow(self.guessCounter)
        if row is None:
            return
        for i in range(0, row.columns):
            if row.getCellText(i) == "":
                row.setCellText(i, text)
                return
        return

    def trunc_row(self):
        row = self.GameRows.getRow(self.guessCounter)
        if row is None:
            return
        for i in range(0, row.columns):
            if row.getCellText(row.columns - 1 - i) != "":
                row.setCellText(row.columns - 1 - i, "")
                return
        return

    def submit_row(self):
        row = self.GameRows.getRow(self.guessCounter)
        if row is None:
            return
        text = row.getText()
        if len(text) != self.GameRows.columns:
            return
        rating = rateAnswer(text, self.secretWord)
        self.guessCounter += 1
        self.apply_colors(row, rating)
        if text == self.secretWord:
            messagebox.showinfo(message=f"You Win!\nYou guessed correctly in {self.guessCounter} guess" +
                                        ("es!" if self.guessCounter > 1 else "!"), title="Game Over")
            for key, value in self.Keys.items():
                value.configure(state=tk.DISABLED)
            self.focus()
        elif self.guessCounter > self.GameRows.columns:
            messagebox.showinfo(message=f"You Lose!\nThe word was {self.secretWord}", title="Game Over")
            for key, value in self.Keys.items():
                value.configure(state=tk.DISABLED)
            self.focus()

    def apply_colors(self, row, rating):
        for i in range(row.columns):
            match rating[i][0]:
                case Rating.WRONG:
                    row.setColor(i, self.gray)
                    self.Keys[rating[i][1]].configure(background=self.black)
                case Rating.EXISTS:
                    current = row.getCell(i).cget("background")
                    if current != self.green:
                        row.setColor(i, self.yellow)
                        self.Keys[rating[i][1]].configure(background=self.yellow)
                case Rating.CORRECT:
                    row.setColor(i, self.green)
                    self.Keys[rating[i][1]].configure(background=self.green)

    def key_handler(self, event):
        match event.keycode:
            case 8:
                self.trunc_row()
            case 13:
                self.submit_row()
            case num if num in range(65, 91):
                self.update_row(chr(num).upper())
            case _:
                pass

    def create_keyboard(self):
        keyboard = tk.Frame(self)

        keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Del"],
                ["Enter", "Z", "X", "C", "V", "B", "N", "M"]]

        font = tk.font.Font(family="Comic Sans MS", size=20, weight="bold")

        for i, key_list in enumerate(keys):
            for j, key in enumerate(key_list):
                if key == "Enter":
                    self.Keys[key] = tk.Button(keyboard, height=1, width=10, text=key, font=font, bg=self.gray,
                                               fg="white", command=lambda char=key: self.submit_row())
                    self.Keys[key].grid(row=i, column=j, columnspan=3)
                elif key == "Del":
                    self.Keys[key] = tk.Button(keyboard, height=1, width=3, text=key, font=font, bg=self.gray,
                                               fg="white", command=lambda char=key: self.trunc_row())
                    self.Keys[key].grid(row=i, column=j)
                else:
                    self.Keys[key] = tk.Button(keyboard, height=1, width=3, text=key, font=font, bg=self.gray,
                                               fg="white", command=lambda char=key: self.update_row(char))
                    self.Keys[key].grid(row=i, column=j + (2 if i == 2 else 0))

        keyboard.bind("<Key>", self.key_handler)
        keyboard.focus()
        keyboard.configure(bg=self.black)

        return keyboard
