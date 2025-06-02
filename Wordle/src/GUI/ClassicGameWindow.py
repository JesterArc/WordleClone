import tkinter as tk
from tkinter import ttk, font
from src.GUI.GameRow import GameRow


class ClassicGameWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.currentText = tk.StringVar()
        self.gray = "#3A3A3C"
        self.black = "#121213"

        for i in range(0, 13):
            self.rowconfigure(i, weight=1)
        for i in range(0, 14):
            self.columnconfigure(i, weight=1)

        self.configure(background=self.black)
        self.pack(fill=tk.BOTH, expand=True)

        self.guessRow = GameRow(self, columnspan=5, row=0, column=4)
        self.guessRow.setText(0, "W")
        self.guessRow.setText(1, "O")
        self.guessRow.setText(2, "R")
        self.guessRow.setText(3, "K")
        self.guessRow.setText(4, "S")
        self.guessRow.getCell(2).configure(background="#B59F3B")
        self.guessRow.getCell(3).configure(background="#538D4E")

        self.guessRow2 = GameRow(self, columnspan=5, row=1, column=4)
        self.guessRow2.setText(0, "W")
        self.guessRow2.setText(1, "O")
        self.guessRow2.setText(2, "R")
        self.guessRow2.setText(3, "K")
        self.guessRow2.setText(4, "S")
        self.guessRow2.getCell(2).configure(background="#538D4E")
        self.guessRow2.getCell(3).configure(background="#B59F3B")

        self.guessRow3 = GameRow(self, columnspan=5, row=2, column=4)
        self.guessRow3.setText(0, "W")
        self.guessRow3.setText(1, "O")
        self.guessRow3.setText(2, "R")
        self.guessRow3.setText(3, "K")
        self.guessRow3.setText(4, "S")
        self.guessRow3.getCell(2).configure(background="#B59F3B")
        self.guessRow3.getCell(3).configure(background="#538D4E")

        self.guessRow4 = GameRow(self, columnspan=5, row=3, column=4)
        self.guessRow4.setText(0, "W")
        self.guessRow4.setText(1, "O")
        self.guessRow4.setText(2, "R")
        self.guessRow4.setText(3, "K")
        self.guessRow4.setText(4, "S")
        self.guessRow4.getCell(2).configure(background="#B59F3B")
        self.guessRow4.getCell(3).configure(background="#538D4E")

        self.guessRow5 = GameRow(self, columnspan=5, row=4, column=4)
        self.guessRow5.setText(0, "W")
        self.guessRow5.setText(1, "O")
        self.guessRow5.setText(2, "R")
        self.guessRow5.setText(3, "K")
        self.guessRow5.setText(4, "S")
        self.guessRow5.getCell(2).configure(background="#B59F3B")
        self.guessRow5.getCell(3).configure(background="#538D4E")

        self.guessRow6 = GameRow(self, columnspan=5, row=5, column=4)
        self.guessRow6.setText(0, "W")
        self.guessRow6.setText(1, "O")
        self.guessRow6.setText(2, "R")
        self.guessRow6.setText(3, "K")
        self.guessRow6.setText(4, "S")
        self.guessRow6.getCell(2).configure(background="#B59F3B")
        self.guessRow6.getCell(3).configure(background="#538D4E")
