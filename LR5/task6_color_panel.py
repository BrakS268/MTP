import tkinter as tk
from tkinter import colorchooser


def color_changer():
    root = tk.Tk()
    root.title("Dыбор цвета")
    root.geometry("400x300")

    color_display = tk.Label(root, bg="gray", width=40, height=10, bd=2)
    color_display.pack(pady=20)

    def choose_color():
        color_code = colorchooser.askcolor(title="Выберите цвет")[1]
        if color_code:
            color_display.config(bg=color_code)

    choose_btn = tk.Button(
        root,
        text="Выбрать цвет из палитры",
        command=choose_color,
        bg="lightgreen"
    )
    choose_btn.pack(pady=10)

    root.mainloop()


color_changer()
