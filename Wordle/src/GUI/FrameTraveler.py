import tkinter as tk


class FrameTraveler(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def unload(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()

    def go_to_main_menu(self):
        self.unload()
        from src.GUI.MainMenu import MainMenu
        MainMenu(master=self.master)

    def go_to_game_window(self, rows=6, columns=5, hardmode=False, history=False, replay=list):
        self.unload()
        from src.GUI.GameWindow import GameWindow
        GameWindow(master=self.master, rows=rows, columns=columns, hardmode=hardmode, history=history, replay=replay)

    def go_to_customize_window(self):
        self.unload()
        from src.GUI.CustomizeGame import CustomizeGame
        CustomizeGame(master=self.master)

    def go_to_run_history(self):
        self.unload()
        from src.GUI.RunHistory import RunHistory
        RunHistory(master=self.master)

    def exit_game(self):
        self.unload()
        self.master.destroy()
