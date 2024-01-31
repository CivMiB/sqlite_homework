from tkinter import ttk
import tkinter as tk
import sqlite3
import os


# Создаём класс основного окна
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Устанавливаем параметры окна
        self.title('File Commander')
        self.geometry('480x300+50+50')
        self.resizable(0, 0)
        self.put_frames()

    # Создаём фреймы основного окна
    def put_frames(self):
        self.add_left_panel = Table(self).place(x=0, y=0, width=480, height=300)

class Table(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # определяем столбцы
        self.columns = ('id', 'firstname', 'lastname', 'age')

        self.tree = ttk.Treeview(columns=self.columns, show="headings")
        self.tree.pack(fill='both', expand=1)

        # определяем заголовки
        self.tree.heading("id", text="Номер п.п.")
        self.tree.heading("firstname", text="Имя")
        self.tree.heading("lastname", text="Фамилия")
        self.tree.heading("age", text="Возраст")

        # настраиваем столбцы
        self.tree.column("#1", stretch=tk.NO, anchor='c', width=80)
        self.tree.column("#2", stretch=tk.NO, anchor='c', width=150)
        self.tree.column("#3", stretch=tk.NO, anchor='c', width=150)
        self.tree.column("#4", stretch=tk.NO, anchor='c', width=100)

        # Созданём соединение с базой данных
        with sqlite3.connect('people.db') as conn:
            # Подключаем курсор для выполнения запросов
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM mytable')
            for row in cursor.fetchall():
                self.tree.insert("", tk.END, values=row)


def load_db():
    # Задаём имя файла
    db_filename = 'people.db'
    # Создаём булевую переменную с проверкой на отсутствие файла db_filename
    db_is_new = not os.path.exists(db_filename)
    # Созданём соединение с базой данных
    with sqlite3.connect('people.db') as conn:
        # Подключаем курсор для выполнения запросов
        cursor = conn.cursor()
        # Если файл отсутствует, то:
        if db_is_new:
            # Создаём таблицу mytable в БД
            cursor.execute('''CREATE TABLE mytable (
                           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                           firstname TEXT,
                           lastname TEXT,
                           age INTEGER);''')
            # Передаём данные из словаря в таблицу
            cursor.executemany('INSERT INTO mytable (firstname, lastname, age) VALUES (?,?,?)',
                               dict_for_start.values())



if __name__ == "__main__":
    # Создаём словарь со стартовыми данными
    dict_for_start = {
        '1': ('Иван', 'Казаков', 40),
        '2': ('Владимир', 'Яковлев', 30),
        '3': ('Александр', 'Александров', 34)
    }
    # Запускаем функцию загрузки БД
    load_db()
    app = App()
    app.mainloop()

