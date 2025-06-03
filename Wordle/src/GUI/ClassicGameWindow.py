import tkinter as tk
from src.GUI.GameRow import GameRows

class ClassicGameWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.geometry("620x620")
        self.currentText = tk.StringVar()
        self.gray = "#3A3A3C"
        self.black = "#121213"

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=4)
        self.configure(background=self.black)
        self.pack(fill=tk.BOTH, expand=True)

        self.GameRows = GameRows(self)
        self.GameRows.grid(row=0, column=1, sticky=tk.N)

        self.something = Keyboard(self)
        self.something.grid(row=1, column=0, columnspan=3, sticky=tk.S)

    def updateRow(self, text):
        row = self.GameRows.getCurrentRow()
        for i in range(0, row.columns):
            if row.getCellText(i) == "":
                row.setCellText(i, text)
                return
        return

    def truncRow(self):
        row = self.GameRows.getCurrentRow()
        for i in range(0, row.columns):
            if row.getCellText(row.columns - 1 - i) != "":
                row.setCellText(row.columns - 1 - i, "")
                return
        return

    def subminRow(self):
        row = self.GameRows.getCurrentRow()
        text = row.getText()
        print(text)


class Keyboard(tk.Frame):
    def __init__(self, master: ClassicGameWindow):
        super().__init__(master)
        self.master = master
        self.rows = master.GameRows

        self.keyboardKeys = dict()
        keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Del"],
                ["Enter", "Z", "X", "C", "V", "B", "N", "M"]]
        self.keyCodes = [8, 13] + [i for i in range(65, 91)]
        self.gray = "#3A3A3C"
        self.black = "#121213"
        self.yellow = "#28A645"
        self.green = "#ECFF49"

        def key_handler(event):
            match event.keycode:
                case 8:
                    master.truncRow()
                case 13:
                    master.subminRow()
                case num if num in range(65, 91):
                    master.updateRow(event.char.upper())
                case _:
                    pass

        font = tk.font.Font(family="Comic Sans MS", size=20, weight="bold")

        for i, key_list in enumerate(keys):
            for j, key in enumerate(key_list):
                if key == "Enter":
                    tk.Button(self, height=1, width=10, text=key, font=font, bg=self.gray, fg="white",
                              command=lambda char=key: master.subminRow()).grid(
                        row=i, column=j, columnspan=3)
                elif key == "Del":
                    tk.Button(self, height=1, width=3, text=key, font=font, bg=self.gray, fg="white",
                              command=lambda char=key: master.truncRow()).grid(
                        row=i, column=j)
                else:
                    tk.Button(self, height=1, width=3, text=key, font=font, bg=self.gray, fg="white",
                              command=lambda char=key: master.updateRow(char)).grid(
                        row=i, column=j + (2 if i == 2 else 0))

        self.bind("<Key>", key_handler)
        self.focus()
        self.configure(bg="#121213")
