import sqlite3
import csv



def create_test_database():
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

    cursor.execute("DELETE FROM students")

    test_students = [
        ('Иван', 'Петров', 20, 2, 4.2),
        ('Мария', 'Иванова', 21, 3, 4.7),
        ('Алексей', 'Сидоров', 19, 1, 3.9),
        ('Ольга', 'Кузнецова', 22, 4, 4.5),
        ('Дмитрий', 'Васильев', 20, 2, 3.8)
    ]

    cursor.executemany('''
        INSERT INTO students (first_name, last_name, age, course, average_grade)
        VALUES (?, ?, ?, ?, ?)
    ''', test_students)

    conn.commit()
    conn.close()



def export_to_csv():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()

    conn.close()

    with open('students.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['ID', 'Имя', 'Фамилия', 'Возраст', 'Курс', 'Средний балл'])

        for student in students:
            writer.writerow(student)

    print(f"Данные экспортированы в файл 'students.csv'")
    print(f"Экспортировано записей: {len(students)}")


create_test_database()
export_to_csv()

