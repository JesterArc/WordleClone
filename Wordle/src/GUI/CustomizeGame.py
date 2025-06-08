import tkinter as tk
from tkinter import ttk, font


# 3 - 10
class CustomizeGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.yellow = "#ECFF49"
        self.green = "#28A645"
        self.light_green = "#34DB66"

        self.f = font.Font(size=30, family="Comic Sans MS", weight="bold")
        for i in range(0, 11):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

        self.pack(fill=tk.BOTH, expand=True)
        self.rows = tk.StringVar()
        self.columns = tk.StringVar()
        self.hardMode = tk.StringVar()
        self.Buttons = self.create_buttons()
        self.Buttons.grid(column=0, row=0, columnspan=12, rowspan=12, sticky=tk.NSEW)

    def create_buttons(self):
        frame = tk.Frame(self)
        frame.configure(background=self.green)

        sizes = [f"{i}" for i in range(3, 11)]
        attempts = [f"{i}" for i in range(3, 11)]
        enableHardMode = ["True", "False"]

        comboStyle = ttk.Style()
        comboStyle.theme_use('clam')
        # noinspection DuplicatedCode
        comboStyle.map('TCombobox',
                       selectforeground=[('readonly', self.yellow), ('active', self.yellow)])
        comboStyle.map('TCombobox', foreground=[('readonly', self.yellow), ('active', self.yellow)])
        comboStyle.map('TCombobox', fieldforeground=[('readonly', self.yellow), ('active', self.yellow)])
        comboStyle.map('TCombobox', activeforeground=[('readonly', self.yellow), ('active', self.yellow)])
        # noinspection DuplicatedCode
        comboStyle.map('TCombobox',
                       selectbackground=[('readonly', self.light_green), ('active', self.light_green)])
        comboStyle.map('TCombobox', background=[('readonly', self.light_green), ('active', self.light_green)])
        comboStyle.map('TCombobox', activebackground=[('readonly', self.light_green), ('active', self.light_green)])
        comboStyle.map('TCombobox', fieldbackground=[('readonly', self.light_green), ('active', self.light_green)])

        for i in range(0, 5):
            frame.columnconfigure(i, weight=1)
            frame.rowconfigure(i, weight=1)

        frame.mainMenuButton = tk.Button(frame, text="Back To Main Menu", bg=self.light_green, fg=self.yellow,
                                         font=self.f, command=lambda:self.back_to_main_menu(),
                                         activebackground=self.light_green, activeforeground=self.yellow)
        frame.mainMenuButton.grid(column=1, row=0, columnspan=3)

        frame.wordLengthLabel = tk.Label(frame, text="Word Length:", font=self.f, bg=self.light_green, fg=self.yellow,
                                         relief="raised")
        frame.wordLength = ttk.Combobox(frame, textvariable=self.columns, width=2,
                                        font=self.f, values=sizes, state="readonly")
        frame.wordLength.current(2)
        frame.wordLengthLabel.grid(column=1, row=1)
        frame.wordLength.grid(column=2, row=1)

        frame.triesLabel = tk.Label(frame, text="How Many Tries:", font=self.f, bg=self.light_green, fg=self.yellow,
                                    relief="raised")
        frame.tries = ttk.Combobox(frame, textvariable=self.rows, width=2,
                                   font=self.f, state="readonly", values=attempts)
        frame.tries.current(3)
        frame.triesLabel.grid(column=1, row=2)
        frame.tries.grid(column=2, row=2)

        frame.hardmodeLabel = tk.Label(frame, text="Hard Mode:", font=self.f, bg=self.light_green, fg=self.yellow,
                                       relief="raised")
        frame.hardmode = ttk.Combobox(frame, textvariable=self.hardMode, width=4,
                                      font=self.f, state="readonly", values=enableHardMode)
        frame.hardmode.current(1)
        frame.hardmodeLabel.grid(column=1, row=3)
        frame.hardmode.grid(column=2, row=3)

        sendButton = tk.Button(frame, text="Start Game", bg=self.light_green, fg=self.yellow,
                               font=self.f, command=lambda: self.start_game(),
                                activebackground=self.light_green, activeforeground=self.yellow)
        sendButton.grid(column=1, row=4, columnspan=3)
        return frame

    def start_game(self):
        rows = int(self.rows.get())
        columns = int(self.columns.get())
        hardMode = True if self.hardMode.get() == "True" else False
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        from src.GUI.GameWindow import GameWindow
        GameWindow(self.master, rows=rows, columns=columns, hardmode=hardMode)

    def back_to_main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        from src.GUI.MainMenu import MainMenu
        MainMenu(self.master)
