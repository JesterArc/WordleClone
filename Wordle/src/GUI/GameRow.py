import tkinter as tk
from tkinter import font


class GameRow(tk.Frame):
    def __init__(self, master, row, column, columnspan=1):
        super().__init__(master)
        self.gray = "#3A3A3C"
        self.master = master
        f = font.Font(size=25, family="Comic Sans MS", weight="bold")
        self.cells = dict()
        for r in range(0, columnspan):
            self.cells[f"text{r}"] = tk.StringVar()
            self.cells[f"text{r}"].set(chr(ord("A") + r))
            self.cells[f"cell{r}"] = tk.Label(self.master, width=2, textvariable=self.cells[f"text{r}"], font=f, background=self.gray, foreground='white', justify='center')
            self.cells[f"cell{r}"].grid(row=row, column=column + r)

    def getCell(self, count):
        return self.cells[f"cell{count}"]

    def setText(self, cell_count, value):
        return self.cells[f"text{cell_count}"].set(value)

    def getText(self, cell_count):
        return self.cells[f"text{cell_count}"]

