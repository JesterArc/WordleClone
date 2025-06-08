from src.GUI import MainMenu
import tkinter as tk

if __name__ == "__main__":

    window = tk.Tk()
    window.title("Wordle Clone")
    window.geometry(f"800x800")
    window.resizable(height=False, width=False)
    MainMenu(window)
    window.mainloop()

