from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    #Модель для таблиці студентів

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)             # Ім'я студента
    last_name = Column(String)              # Прізвище студента
    email = Column(String)                  # Електронна пошта студента
    phone = Column(String)                  # Номер телефону студента
    address = Column(String)                # Адреса студента
    grades = relationship("Grade", back_populates="student")  # Зв'язок з таблицею оцінок

class Group(Base):
    #Модель для таблиці груп

    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)                   # Назва групи
    students = relationship("Student", back_populates="group")  # Зв'язок з таблицею студентів

class Teacher(Base):
    #Модель для таблиці викладачів

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)             # Ім'я викладача
    last_name = Column(String)              # Прізвище викладача
    email = Column(String)                  # Електронна пошта викладача
    phone = Column(String)                  # Номер телефону викладача
    address = Column(String)                # Адреса викладача
    start_work = Column(DateTime)          # Дата початку роботи викладача
    subjects = relationship("Subject", back_populates="teacher")  # Зв'язок з таблицею предметів

class Subject(Base):
    #Модель для таблиці предметів

    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)                   # Назва предмету
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")  # Зв'язок з таблицею викладачів
    grades = relationship("Grade", back_populates="subject")      # Зв'язок з таблицею оцінок

class Grade(Base):
    #Модель для таблиці оцінок

    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))  # ID студента
    subject_id = Column(Integer, ForeignKey('subjects.id'))  # ID предмету
    grade = Column(Integer)                 # Оцінка
    date_received = Column(DateTime)        # Дата отримання оцінки
    student = relationship("Student", back_populates="grades")  # Зв'язок з таблицею студентів
    subject = relationship("Subject", back_populates="grades")  # Зв'язок з таблицею предметів