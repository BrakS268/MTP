import tkinter as tk
from tkinter import ttk
import time



def progressbar():
    root = tk.Tk()
    root.title("Прогрессбар")
    root.geometry("300x150")

    progress_var = tk.IntVar(value=0)

    progress = ttk.Progressbar(root, variable=progress_var, maximum=100, length=250)
    progress.pack(pady=20)

    label = tk.Label(root, text="0%")
    label.pack()

    def simulate_loading():
        for i in range(101):
            progress_var.set(i)
            label.config(text=f"{i}%")
            root.update()
            time.sleep(0.03)

    start_btn = tk.Button(root, text="Начать загрузку", command=simulate_loading)
    start_btn.pack(pady=10)

    root.mainloop()


progressbar()
