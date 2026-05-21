from pydantic import BaseModel


class StudentSchema(BaseModel):

    name: str

    marks: int



class UserSchema(BaseModel):

    username: str

    email: str

    password: str