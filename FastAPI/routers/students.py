from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from models import Student

from schemas import StudentSchema

import crud


router = APIRouter()



@router.post("/students")

def create_student(

    student: StudentSchema,

    db: Session = Depends(get_db)

):

    crud.create_student(

        db,

        student

    )

    return {

        "message": "Student created successfully"

    }



@router.get("/students")

def get_students(

    db: Session = Depends(get_db)

):

    
    return crud.get_students(db)




@router.get("/students/{student_id}")

def get_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    return crud.get_student(

        db,

        student_id

    )



@router.put("/students/{student_id}")

def put_students(

    student_id: int,

    student_data: StudentSchema,

    db: Session = Depends(get_db)

):

    crud.update_student(

        db,

        student_id,

        student_data

    )

    return {

        "message": "Student updated Successfully"

    }


@router.delete("/students/{student_id}")

def delete_students(

    student_id: int,

    db: Session = Depends(get_db)

):

    crud.delete_student(

        db,

        student_id

    )

    return {

        "message": "Deleted Student Successfully"

    }