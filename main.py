from faker import Faker
import random
import psycopg2
from psycopg2 import sql

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1111",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Ініціалізуємо Faker
fake = Faker()

# Додамо групи
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    cursor.execute(
        sql.SQL("INSERT INTO groups (group_name) VALUES (%s)"),
        [group_name]
    )

# Додамо викладачів
teachers = [fake.name() for _ in range(5)]
for teacher_name in teachers:
    cursor.execute(
        sql.SQL("INSERT INTO teachers (teacher_name) VALUES (%s)"),
        [teacher_name]
    )

# Додамо предмети з випадковим призначенням викладачів
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Geography']
for subject_name in subjects:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute(
        sql.SQL("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)"),
        [subject_name, teacher_id]
    )

# Додамо студентів у випадкові групи
for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, len(groups))
    cursor.execute(
        sql.SQL("INSERT INTO students (student_name, group_id) VALUES (%s, %s)"),
        [student_name, group_id]
    )

# Додамо оцінки для студентів з усіх предметів
for student_id in range(1, 31):
    for subject_id in range(1, 8):
        grade = round(random.uniform(2, 5), 1)
        date_received = fake.date_between(start_date='-3y', end_date='today')
        cursor.execute(
            sql.SQL("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)"),
            [student_id, subject_id, grade, date_received]
        )

# Застосовуємо зміни до бази даних
conn.commit()
# Закриваємо з'єднання
cursor.close()
conn.close()
