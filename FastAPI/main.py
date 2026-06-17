from fastapi import FastAPI

from database import engine
from database import Base
from pydantic import BaseModel


import models

from routers.students import router
from routers.auth import router as auth_router
from routers.posts import router as posts_router
from fastapi import FastAPI



# Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
app.include_router(posts_router)

@app.get("/health")
def health():
    return {"status": "ok"}


class UserCreate(BaseModel):
    name: str
    email: str


@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created",
        "user": user.model_dump()
    }