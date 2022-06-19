# три студента создаем список у кого какие книги

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///sqlite.db", echo=True)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    pages_count = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    student = relationship('Student', foreign_keys='Book.student_id', backref='books')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# student1 = Student(firstname="Name1", lastname="Surname1")
# student2 = Student(firstname="Name2", lastname="Surname2")
# student3 = Student(firstname="Name3", lastname="Surname3")
# book1 = Book(title="Book1", pages_count=120, student=student1)
# book2 = Book(title="Book2", pages_count=78, student=student2)
# book3 = Book(title="Book3", pages_count=59, student=student3)
# #
# session.add_all([student1, student2, student3, book1, book2, book3])
# session.commit()

students_books = session.query(Student, Book).join(
    Book, Student.id == Book.student_id).all()

print('firstname', 'lastname', 'book_title', 'pages_count', sep=' ! ')
for row in students_books:
    print(row[0].firstname, row[0].lastname, row[1].title, row[1].pages_count, sep=' ! ')


