import tkinter as tk
from tkinter import messagebox


def show_hello():
    messagebox.showinfo("Приветствие", "Привет!")


def create_hello_window():
    root = tk.Tk()
    root.title("Task 1")
    root.geometry("300x200")
    root.resizable(True, True)

    hello_button = tk.Button(
        root,
        text="Привет!",
        command=show_hello,
        bg="lightblue",
        fg="darkblue",
        font=("Arial", 14, "bold"),
        width=15,
        height=2
    )

    hello_button.pack(pady=50)
    root.mainloop()


create_hello_window()
