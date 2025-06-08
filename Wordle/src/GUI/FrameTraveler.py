import tkinter as tk


class FrameTraveler(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def go_to_main_menu(self):
        from src.GUI.MainMenu import MainMenu
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        MainMenu(master=self.master)

    def go_to_game_window(self, rows=6, columns=5, hardmode=False):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        from src.GUI.GameWindow import GameWindow
        GameWindow(master=self.master, rows=rows, columns=columns, hardmode=hardmode)

    def go_to_customize_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        from src.GUI.CustomizeGame import CustomizeGame
        CustomizeGame(master=self.master)

    def exit_game(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        self.master.destroy()
