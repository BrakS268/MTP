import sqlite3
import os


def create_database():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        course INTEGER,
        average_grade REAL
    )
    ''')
    print("Таблица 'students' создана")

    conn.commit()
    conn.close()

    if os.path.exists('university.db'):
        size = os.path.getsize('university.db')
        print(f"Размер файла БД: {size} байт")

    return True


create_database()
