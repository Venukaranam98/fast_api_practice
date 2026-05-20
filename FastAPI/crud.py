from sqlalchemy.orm import Session

from models import Student

def get_students(db: Session):

    return db.query(

        Student

    ).all()


def get_student(

    db: Session,

    student_id: int

):

    return db.query(

        Student

    ).filter(

        Student.id == student_id

    ).first()

def create_student(

    db: Session,

    student_data

):

    new_student = Student(

        name=student_data.name,

        marks=student_data.marks

    )

    db.add(new_student)

    db.commit()

    return new_student


def update_student(

    db: Session,

    student_id: int,

    student_data

):

    student = db.query(

        Student

    ).filter(

        Student.id == student_id

    ).first()

    student.marks = student_data.marks

    db.commit()

    return student


def delete_student(

    db: Session,

    student_id: int

):

    student = db.query(

        Student

    ).filter(

        Student.id == student_id

    ).first()

    db.delete(student)

    db.commit()

    return student