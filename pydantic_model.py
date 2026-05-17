from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Student(BaseModel):
    name : str
    marks : int

@app.post("/students")
def post_student(student:Student):
    return student
    
