import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont


class Graph:

    def __init__(self, root):

        label1 = tk.Label(root)
        label1["text"] = "Парабола Нейля"
        label1.place(x=150, y=0, width=200, height=30)
        label1["font"] = tkFont.Font(size=16, weight='bold')

        label2 = tk.Label(root)
        label2["text"] = "y\u00B2 = a\u00B2x\u00B3"
        label2.place(x=210, y=40, width=80, height=25)
        label2["font"] = tkFont.Font(size=14, slant='italic')
        label2["fg"] = "#a40000"

        label3 = tk.Label(root)
        label3["text"] = "a ="
        label3.place(x=0, y=80, width=70, height=25)

        label4 = tk.Label(root)
        label4["text"] = "Діапазон ="
        label4.place(x=0, y=120, width=70, height=30)

        label8 = tk.Label(root)
        label8["text"] = "["
        label8.place(x=63, y=120, width=25, height=30)

        label5 = tk.Label(root)
        label5["text"] = ";"
        label5.place(x=120, y=120, width=42, height=30)

        label6 = tk.Label(root)
        label6["text"] = ")"
        label6.place(x=170, y=120, width=70, height=25)

        label7 = tk.Label(root)
        label7["text"] = "Крок ="
        label7.place(x=0, y=160, width=70, height=25)

        domain1 = tk.Entry(root)
        domain1["borderwidth"] = "1px"
        domain1.place(x=80, y=120, width=51, height=30)

        domain2 = tk.Entry(root)
        domain2["borderwidth"] = "1px"
        domain2.place(x=150, y=120, width=50, height=30)

        parameter = tk.Entry(root)
        parameter["borderwidth"] = "1px"
        parameter.place(x=80, y=80, width=120, height=30)

        step = tk.Entry(root)
        step["borderwidth"] = "1px"
        step.place(x=80, y=160, width=121, height=30)

        def build_function():

            try:
                float_domain1 = float(domain1.get())
                float_domain2 = float(domain2.get())
                float_parameter = float(parameter.get())
                float_step = float(step.get())
            except ValueError:
                messagebox.showerror('Помилка', 'Помилка: деякі значення відсутні або неправильно введені')
                return

            if float_domain1 > float_domain2:
                messagebox.showerror('Помилка', 'Помилка: неправильно введений діапазон функції')
                return

            if float_domain1 < 0 or float_domain2 < 0:
                messagebox.showerror('Помилка', 'Помилка: функція не визначена для від\u0027ємних значень')
                return
            if float_step == 0 or float_step < 0:
                messagebox.showerror('Помилка', 'Помилка: неправильно введений крок функції')
                return

            plt.figure("Парабола Нейля")
            x = np.arange(float_domain1, float_domain2, float_step)
            y = float_parameter * np.power(x, 3 / 2)
            plt.axhline(y=0, c="black", label="y=0")
            plt.grid()
            plt.plot(x, y)
            plt.plot(x, -y)
            plt.show()

        button = tk.Button(root)
        button["text"] = "Побудувати графік"
        button.place(x=170, y=200, width=140, height=36)
        button["cursor"] = "hand2"
        button["command"] = build_function


if __name__ == "__main__":
    root = tk.Tk()
    app = Graph(root)
    root.title('Парабола Нейля')
    root.geometry("500x250")
    root.resizable(False, False)
    photo = tk.PhotoImage(file='Function-PNG.png')
    root.iconphoto(False, photo)
    root.mainloop()

