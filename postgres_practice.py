from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2


app = FastAPI()


conn = psycopg2.connect(

    host="localhost",

    database="student_db",

    user="postgres",

    password="venu123",

    port="5432"

)


cursor = conn.cursor()


class Student(BaseModel):

    name: str

    marks: int


@app.post("/students")

def create_student(student: Student):

    cursor.execute(

        '''

        INSERT INTO students(

            name,

            marks

        )

        VALUES(%s, %s)

        ''',

        (

            student.name,

            student.marks

        )

    )

    conn.commit()


    return {

        "message": "Student created successfully"

    }


@app.get("/students")

def get_students():

    cursor.execute(

        '''

        SELECT * FROM students

        '''

    )


    students = cursor.fetchall()


    return students


@app.get("/students/{student_id}")

def get_student(student_id: int):

    cursor.execute(

        '''

        SELECT * FROM students

        WHERE id = %s

        ''',

        (student_id,)

    )


    student = cursor.fetchone()


    return student


@app.put("/students/{student_id}")

def update_student(

    student_id: int,

    student: Student

):

    cursor.execute(

        '''

        UPDATE students

        SET marks = %s

        WHERE id = %s

        ''',

        (

            student.marks,

            student_id

        )

    )


    conn.commit()


    return {

        "message": "Student updated successfully"

    }


@app.delete("/students/{student_id}")

def delete_student(student_id: int):

    cursor.execute(

        '''

        DELETE FROM students

        WHERE id = %s

        ''',

        (student_id,)

    )


    conn.commit()


    return {

        "message": "Student deleted successfully"

    }