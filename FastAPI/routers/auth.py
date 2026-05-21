from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from models import User

from schemas import UserSchema,LoginSchema

from hashing import hash_password,verify_password

from jwt_handler import create_access_token,verify_access_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="login"

)

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


@router.post("/login")

def login_user(

    user: LoginSchema,

    db: Session = Depends(get_db)

):

    db_user = db.query(

        User

    ).filter(

        User.email == user.email

    ).first()


    if not db_user:

        return {

            "message": "User not found"

        }


    if not verify_password(

        user.password,

        db_user.password

    ):

        return {

            "message": "Invalid password"

        }


    access_token = create_access_token(

        data={

            "sub": db_user.email

        }

    )


    return {

        "access_token": access_token,

        "token_type": "bearer"

    }


def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    email = verify_access_token(token)


    if email is None:

        return {

            "message": "Invalid token"

        }


    user = db.query(

        User

    ).filter(

        User.email == email

    ).first()


    return user