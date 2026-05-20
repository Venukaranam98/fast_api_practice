from pydantic import BaseModel


class StudentSchema(BaseModel):

    name: str

    marks: int