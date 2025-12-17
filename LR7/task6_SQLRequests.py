import sqlite3

DB_NAME = 'university.db'


def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students")

    conn.commit()
    conn.close()


def add_student_with_params(first_name, last_name, age, course, average_grade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO students (first_name, last_name, age, course, average_grade)
        VALUES (:first_name, :last_name, :age, :course, :grade)
    ''', {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'course': course,
        'grade': average_grade
    })

    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    print(f"Студент {first_name} {last_name} добавлен (ID: {student_id})")
    return student_id


def get_students_by_course(course):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE course = ?', (course,))
    students = cursor.fetchall()
    conn.close()

    print(f"Студенты {course} курса: {len(students)} чел.")
    return students


def demonstrate_parametrized_queries():
    init_database()

    print("\nДобавление нового студента:")
    new_id = add_student_with_params(
        first_name="Анна",
        last_name="Смирнова",
        age=20,
        course=3,
        average_grade=4.8
    )

    second_course = get_students_by_course(3)
    for student in second_course:
        print(f"  - {student[1]} {student[2]}")


demonstrate_parametrized_queries()
