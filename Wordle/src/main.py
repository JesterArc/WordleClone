from src.GUI.MainMenu import MainMenu
import tkinter as tk

if __name__ == "__main__":

    window = tk.Tk()
    window.title("Wordle Clone")
    window.geometry("600x600")

    for i in range(0, 11):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)
    MainMenu(window)
    window.mainloop()

