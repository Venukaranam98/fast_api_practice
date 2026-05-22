from fastapi import FastAPI

from database import engine
from database import Base

import models

from routers.students import router
from routers.auth import router as auth_router
from routers.posts import router as posts_router


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
app.include_router(posts_router)