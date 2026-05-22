from pydantic import BaseModel


class StudentSchema(BaseModel):

    name: str

    marks: int



class UserSchema(BaseModel):

    username: str

    email: str

    password: str

class LoginSchema(BaseModel):

    email: str

    password: str


class PostSchema(BaseModel):

    title: str

    content: str