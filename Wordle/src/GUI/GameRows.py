import tkinter as tk
from tkinter import font


class GameRows(tk.Frame):
    def __init__(self, master, rows=6, columns=5):
        super().__init__(master)
        self.master = master
        self.rowCount = rows
        self.columnCount = columns

        for i in range(0, self.columnCount):
            self.columnconfigure(i, weight=1)
        for i in range(0, self.rowCount):
            self.rowconfigure(i, weight=1)

        self.rows = dict()

        for i in range(0, rows):
            self.rows[f"row{i}"] = GameRow(self, column=columns, row=i)

    def getRow(self, row):
        return self.rows[f"row{row}"]

    def pack(self):
        text = list("" for _ in range(self.rowCount))
        for i in range(self.rowCount):
            row = self.getRow(i)
            for j in range(self.columnCount):
                text[i] += f"{row.getCell(j)['background']}_{row.getCell(j)['text']} "
            text[i] = text[i][:-1]
        return text

    def unpack(self, preset):
        for pos, row in enumerate(preset):
            text = row.split(" ")
            for val in range(len(text)):
                text[val] = text[val].split("_")
            for i in range(0, self.columnCount):
                self.getRow(pos).setCellText(i, text[i][1])
                self.getRow(pos).getCell(i).configure(background=text[i][0])


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

    def setText(self, text):
        for i in range(0, self.columns):
            self.cells[f"text{i}"].set(text[i])

    def setColor(self, cell, color):
        self.cells[f"cell{cell}"].configure(background=color)