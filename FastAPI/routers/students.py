from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from models import Student

from schemas import StudentSchema


router = APIRouter()



@router.post("/students")

def create_student(

    student: StudentSchema,

    db: Session = Depends(get_db)

):

    new_student = Student(

        name=student.name,
        marks=student.marks

    )

    db.add(new_student)

    db.commit()

    return {

        "message": "Student created successfully"

    }




@router.get("/students")

def get_students(

    db: Session = Depends(get_db)

):

    students = db.query(

        Student

    ).all()

    return students




@router.get("/students/{student_id}")

def get_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    student = db.query(

        Student

    ).filter(

        Student.id == student_id

    ).first()

    return student




@router.put("/students/{student_id}")

def put_students(

    student_id: int,

    student_data: StudentSchema,

    db: Session = Depends(get_db)

):

    student = db.query(

        Student

    ).filter(

        Student.id == student_id

    ).first()

    student.marks = student_data.marks

    db.commit()

    return {

        "message": "Student updated Successfully"

    }




@router.delete("/students/{student_id}")

def delete_students(

    student_id: int,

    db: Session = Depends(get_db)

):

    student = db.query(

        Student

    ).filter(

        Student.id == student_id

    ).first()

    db.delete(student)

    db.commit()

    return {

        "message": "Deleted Student Successfully"

    }