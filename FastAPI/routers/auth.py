from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from models import User

from schemas import UserSchema

from hashing import hash_password

router = APIRouter()

@router.post("/register")

def register_user(

    user: UserSchema,

    db: Session = Depends(get_db)

):

    hashed_password = hash_password(

        user.password

    )


    new_user = User(

        username=user.username,

        email=user.email,

        password=hashed_password

    )


    db.add(new_user)

    db.commit()


    return {

        "message": "User registered successfully"

    }