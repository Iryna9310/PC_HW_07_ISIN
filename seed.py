import random
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from conf.db import session
from conf.models import Teacher, Student, Subject, Grade

fake = Faker('uk-UA')

def insert_students(num_students):
    """Функція для додавання студентів"""
    for _ in range(num_students):
        student = Student(
            first_name=fake.first_name(),      # Генерація випадкового імені
            last_name=fake.last_name(),        # Генерація випадкового прізвища
            email=fake.email(),                # Генерація випадкової електронної пошти
            phone=fake.phone_number(),         # Генерація випадкового номера телефону
            address=fake.address()             # Генерація випадкової адреси
        )
        session.add(student)

def insert_teachers(num_teachers):
    """Функція для додавання викладачів"""
    for _ in range(num_teachers):
        teacher = Teacher(
            first_name=fake.first_name(),      # Генерація випадкового імені
            last_name=fake.last_name(),        # Генерація випадкового прізвища
            email=fake.email(),                # Генерація випадкової електронної пошти
            phone=fake.phone_number(),         # Генерація випадкового номера телефону
            address=fake.address(),            # Генерація випадкової адреси
            start_work=fake.date_between(start_date='-5y')  # Генерація дати початку роботи (останні 5 років)
        )
        session.add(teacher)

def insert_subjects(num_subjects):
    """Функція для додавання предметів"""
    subjects = ['Математика', 'Фізика', 'Хімія', 'Біологія', 'Історія']
    for i in range(num_subjects):
        teacher = session.query(Teacher).order_by(func.random()).first()  # Вибираємо випадкового викладача
        subject = Subject(
            name=subjects[i],                 # Вибір назви предмета зі списку
            teacher_id=teacher.id             # Призначення випадкового викладача для предмета
        )
        session.add(subject)

def insert_grades(num_grades):
    """Функція для додавання оцінок"""
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for _ in range(num_grades):
            subject = random.choice(subjects)  # Вибір випадкового предмета
            grade = Grade(
                student_id=student.id,        # Призначення студента для оцінки
                subject_id=subject.id,        # Призначення предмета для оцінки
                grade=random.randint(60, 100),  # Генерація випадкової оцінки
                date_received=fake.date_between(start_date='-1y', end_date='today')  # Генерація випадкової дати отримання
            )
            session.add(grade)

if __name__ == '__main__':
    try:
        insert_students(30)  # Додамо від 30 студентів
        insert_teachers(random.randint(3, 5))   # Додамо від 3 до 5 викладачів
        insert_subjects(random.randint(5, 8))   # Додамо від 5 до 8 предметів
        session.commit()
        insert_grades(20)    # Додамо до 20 оцінок кожному студентові
        session.commit()
    except SQLAlchemyError as e:
        print("Помилка SQLAlchemy:", e)
        session.rollback()
    finally:
        session.close()