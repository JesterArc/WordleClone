import tkinter as tk
from tkinter import messagebox
from ..GUI.GameRows import GameRows
from ..Logic import Wordle, Rating, Validation


class GameWindow(tk.Frame):
    def __init__(self, master: tk.Tk, hardmode=False, rows=6, columns=5):
        super().__init__(master)
        self.master = master

        self.gray = "#3A3A3C"
        self.black = "#121213"
        self.yellow = "#ECFF49"
        self.green = "#28A645"

        self.hardmode = hardmode
        self.rows = rows
        self.columns = columns

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=4)
        self.configure(background=self.black)
        self.pack(fill=tk.BOTH, expand=True)

        self.GameRows = GameRows(self, columns=columns, rows=rows)
        self.GameRows.grid(row=0, column=1, sticky=tk.N)

        self.Keys = dict()
        self.keyboard = self.create_keyboard()
        self.keyboard.grid(row=1, column=0, columnspan=3, sticky=tk.S)

        self.buttons = self.create_menu_button()
        self.buttons.grid(row=0, column=2, sticky=tk.NE)

        self.buttons2 = self.create_restart_button()
        self.buttons2.grid(row=0, column=0, sticky=tk.NW)

        self.game = Wordle(hardmode=hardmode, length=columns)

    def update_row(self, text):
        row = self.GameRows.getRow(self.game.guessCounter)
        if row is None:
            return
        for i in range(0, row.columns):
            if row.getCellText(i) == "":
                row.setCellText(i, text)
                return
        return

    def trunc_row(self):
        row = self.GameRows.getRow(self.game.guessCounter)
        if row is None:
            return
        for i in range(0, row.columns):
            if row.getCellText(row.columns - 1 - i) != "":
                row.setCellText(row.columns - 1 - i, "")
                return
        return

    def submit_row(self):
        row = self.GameRows.getRow(self.game.guessCounter)
        text = row.getText()
        match self.game.verifyWord(text):
            case Validation.TOO_SHORT:
                messagebox.showerror("Too Short", message=f"Too Short: {text}")
                return
            case Validation.NOT_A_WORD:
                messagebox.showerror("Not a Word", message=f"Not a Word: {text}")
                return
            case Validation.NOT_ALLOWED:
                messagebox.showerror("Not Allowed", message=f"{text} doesn't contain required letters")
                return
        self.apply_colors(row, self.game.rateAnswer(text))
        self.check_win(text)

    def check_win(self, text):
        print(self.game.guessCounter, self.GameRows.rowCount)
        if text == self.game.secretWord:
            messagebox.showinfo(message=f"You Win!\nYou guessed correctly in {self.game.guessCounter} guess" +
                                        ("es!" if self.game.guessCounter > 1 else "!"), title="Game Over")
            for key, value in self.Keys.items():
                value.configure(state=tk.DISABLED)
            self.focus()
        elif self.game.guessCounter == self.GameRows.rowCount:
            messagebox.showinfo(message=f"You Lose!\nThe word was {self.game.secretWord}", title="Game Over")
            for key, value in self.Keys.items():
                value.configure(state=tk.DISABLED)
            self.focus()

    def apply_colors(self, row, ratingArray):
        for cell, (rating, letter) in enumerate(ratingArray):
            match rating:
                case Rating.WRONG | Rating.EXISTS:
                    if row.getCell(cell).cget("background") != self.green:
                        row.setColor(cell, self.gray if rating == Rating.WRONG else self.yellow)
                    if self.Keys[letter].cget("background") != self.green:
                        self.Keys[letter].configure(background=self.black if rating == Rating.WRONG else self.yellow)
                case Rating.CORRECT:
                    row.setColor(cell, self.green)
                    self.Keys[letter].configure(background=self.green)

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

    def create_menu_button(self):
        buttons = tk.Frame(self)
        buttons.configure(bg=self.black)
        font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        button = tk.Button(buttons, text="Main Menu", font=font, width=10, height=2,
                           fg='white', bg=self.gray, activebackground=self.gray, activeforeground='white',
                           command=lambda: self.back_to_main_menu())
        button.grid()

        return buttons

    def create_restart_button(self):
        buttons = tk.Frame(self)
        buttons.configure(bg=self.black)
        font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        button = tk.Button(buttons, text="Restart", font=font, width=10, height=2,
                           fg='white', bg=self.gray, activebackground=self.gray, activeforeground='white',
                           command=lambda: self.restart())
        button.grid()

        return buttons

    def back_to_main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        from src.GUI.MainMenu import MainMenu
        MainMenu(self.master)

    def restart(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        GameWindow(self.master, hardmode=self.hardmode, rows=self.rows, columns=self.columns)
