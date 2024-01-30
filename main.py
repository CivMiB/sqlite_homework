'''Создать графическую программу, с использованием Tkinter, которая с выводит список имен, фамилий и их возвраст
из базы данных sqlite. При запуске программы, должен создаваться (если ее нет) файл базы данных people.db
и таблица соответственно. База данных должна заполняться в первый раз из словаря. Реализовать все проверки
на исключения и максимально документировать весь код.'''

from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import os
import shutil


# Создаём класс основного окна
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Устанавливаем параметры окна
        self.title('File Commander')
        self.geometry('1000x630+50+50')
        self.resizable(0, 0)
        self.put_frames()

    # Создаём фреймы основного окна
    def put_frames(self):
        self.add_left_panel = LeftPanel(self).place(x=0, y=0, width=500, height=570)



if __name__ == "__main__":
    app = App()
    app.mainloop()

