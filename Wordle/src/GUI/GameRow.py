import tkinter as tk
from tkinter import font


class GameRow(tk.Frame):
    def __init__(self, master, row, columnspan=1):
        super().__init__(master)
        self.gray = "#3A3A3C"
        self.master = master
        self.columns = columnspan
        f = font.Font(size=30, family="Comic Sans MS", weight="bold")
        self.cells = dict()
        self.isCurrentRow = False
        for r in range(0, columnspan):
            self.cells[f"text{r}"] = tk.StringVar()
            self.cells[f"cell{r}"] = tk.Label(self.master, width=2, textvariable=self.cells[f"text{r}"], font=f, background=self.gray, foreground='white', justify='center', padx=5, pady=5, highlightcolor="white", highlightthickness=1)
            self.cells[f"cell{r}"].grid(row=row, column=r + 1)

    def getCell(self, count):
        return self.cells[f"cell{count}"]

    def setText(self, cell_count, value):
        return self.cells[f"text{cell_count}"].set(value)

    def getText(self, cell_count):
        return self.cells[f"text{cell_count}"]

    def setCells(self, text):
        for i in range(0, self.columns):
            self.setText(i, text[i])


class GameRows(tk.Frame):
    def __init__(self, master, rows, columnspan=5):
        super().__init__(master)
        self.master = master

        for i in range(0, 5):
            self.columnconfigure(0, weight=1)
        for i in range(0, 6):
            self.rowconfigure(0, weight=1)

        self.rows = dict()

        for i in range(0, rows):
            self.rows[f"row{i}"] = GameRow(self, columnspan=columnspan, row=i)

        self.rows["row0"].isCurrentRow = True

    def getRow(self, row):
        return self.rows[f"row{row}"]

    def getCurrentRow(self):
        for key, value in self.rows.items():
            if value.isCurrentRow:
                return value
