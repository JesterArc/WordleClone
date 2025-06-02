import tkinter as tk
from src.GUI.GameRow import GameRows


class ClassicGameWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.currentText = tk.StringVar()
        self.gray = "#3A3A3C"
        self.black = "#121213"

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=2)

        self.configure(background=self.black)
        self.pack(fill=tk.BOTH, expand=True)

        self.GameRows = GameRows(self, rows=6)
        self.GameRows.grid(column=1)

