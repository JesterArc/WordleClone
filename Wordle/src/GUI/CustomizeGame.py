import tkinter as tk
from tkinter import ttk, font, messagebox
from .FrameTraveler import FrameTraveler


class CustomizeGame(FrameTraveler):
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
        enableHardMode = ["On", "Off"]

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

        mainMenuButton = tk.Button(frame, width=20, text="Back To Main Menu", bg=self.light_green, fg=self.yellow,
                                   font=self.f, command=lambda: self.go_to_main_menu(),
                                   activebackground=self.light_green, activeforeground=self.yellow)
        mainMenuButton.grid(column=1, row=0, columnspan=3)

        wordLengthLabel = tk.Label(frame, width=15, text="Word Length:", font=self.f, bg=self.light_green,
                                   fg=self.yellow, relief="raised")
        wordLength = ttk.Combobox(frame, textvariable=self.columns, width=4, justify='center',
                                  font=self.f, values=sizes, state="readonly")
        wordLength.current(2)
        wordLengthLabel.grid(column=1, row=1)
        wordLength.grid(column=2, row=1)

        triesLabel = tk.Label(frame, width=15, text="How Many Tries:", font=self.f, bg=self.light_green,
                              fg=self.yellow, relief="raised")
        tries = ttk.Combobox(frame, textvariable=self.rows, width=4, justify='center',
                             font=self.f, state="readonly", values=attempts)
        tries.current(3)
        triesLabel.grid(column=1, row=2)
        tries.grid(column=2, row=2)

        hardModeLabel = tk.Label(frame, width=15, text="Hard Mode:", font=self.f, bg=self.light_green,
                                 fg=self.yellow, relief="raised")
        hardMode = ttk.Combobox(frame, textvariable=self.hardMode, width=4, justify='center',
                                font=self.f, state="readonly", values=enableHardMode)
        hardMode.current(1)
        hardModeLabel.grid(column=1, row=3)
        hardMode.grid(column=2, row=3)

        hardModeTooltip = tk.Button(frame, text="i", width=3,
                                    font=font.Font(size=10, family="Comic Sans MS", weight="bold"),
                                    bg=self.light_green, fg=self.yellow, activebackground=self.light_green,
                                    activeforeground=self.yellow, relief="ridge",
                                    command=lambda: tk.messagebox.showinfo(
                                        title="Hard Mode Explained",
                                        message="Any revealed hints must be used in subsequent guesses"
                                                "\nIf a letter is marked yellow, you must include it somewhere"
                                                "\nIf a letter is marked green, it must be in that spot"))
        hardModeTooltip.grid(column=3, row=3)

        sendButton = tk.Button(frame, width=20, text="Start Game", bg=self.light_green, fg=self.yellow, font=self.f,
                               command=lambda: self.go_to_game_window(int(self.rows.get()), int(self.columns.get()),
                                                                      True if self.hardMode.get() == "On" else False),
                               activebackground=self.light_green, activeforeground=self.yellow)
        sendButton.grid(column=1, row=4, columnspan=3)
        return frame
