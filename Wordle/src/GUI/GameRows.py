import tkinter as tk
from tkinter import font


class GameRows(tk.Frame):
    def __init__(self, master, rows=6, columns=5):
        super().__init__(master)
        self.master = master
        self.rows = rows
        self.columns = columns

        for i in range(0, columns):
            self.columnconfigure(i, weight=1)
        for i in range(0, rows):
            self.rowconfigure(i, weight=1)

        self.rows = dict()

        for i in range(0, rows):
            self.rows[f"row{i}"] = GameRow(self, column=columns, row=i)

    def getRow(self, row):
        return self.rows[f"row{row}"]


class GameRow(tk.Frame):
    def __init__(self, master, row, column=1):
        super().__init__(master)
        self.gray = "#3A3A3C"
        self.master = master
        self.columns = column
        f = font.Font(size=25, family="Comic Sans MS", weight="bold")
        self.cells = dict()
        for r in range(0, column):
            self.cells[f"text{r}"] = tk.StringVar()
            self.cells[f"text{r}"].set("")
            self.cells[f"cell{r}"] = tk.Label(self.master, width=2, textvariable=self.cells[f"text{r}"], font=f,
                                              background=self.gray, foreground='white', justify='center',
                                              padx=5, pady=5, highlightcolor="white", highlightthickness=1)
            self.cells[f"cell{r}"].grid(row=row, column=r)

    def getCell(self, count):
        return self.cells[f"cell{count}"]

    def setCellText(self, cell, value):
        return self.cells[f"text{cell}"].set(value)

    def getCellText(self, cell):
        return self.cells[f"text{cell}"].get()

    def getText(self):
        return ''.join([self.cells[f"text{i}"].get() for i in range(0, self.columns)])

    def setText(self, value):
        for i in range(0, self.columns):
            self.cells[f"text{i}"].set(value[i])

    def setColor(self, cell, color):
        self.cells[f"cell{cell}"].configure(background=color)
